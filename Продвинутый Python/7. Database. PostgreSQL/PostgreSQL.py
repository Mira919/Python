# Написать функции для работы с таблицами:
# 1)Создание таблиц: таблица студенты, таблица курсы, таблица связи студентов и курсов
# 2)Добавление студента
# 3)Добавление курса
# 4)Вывод информации о студенте по его ID
# 5)Добавление двух и более студентов и запись их на курс
# 6)Выводит студентов определенного курса

import psycopg2 #для работы с PosrgreSQL
conn = psycopg2.connect(dbname='test_db', user='test_user', #для соединения с бд
                        password='1234', host='localhost')
cur = conn.cursor()

# создает таблицы student, course, student_course
def create_db():
    cur.execute("""
                    create table if not exists student (
                    id serial PRIMARY KEY,
                    name varchar(100) not null,
                    gpa numeric(10,2),
                    birth timestamp with time zone
                    );
                """)
    print('Таблица student создана')
    cur.execute("""
                    create table if not exists course (
                    id serial PRIMARY KEY,
                    name varchar(100) not null
                    );
                """)
    print('Таблица course создана')
    cur.execute("""
                    create table if not exists student_course (
                    id serial PRIMARY KEY,
                    student_id INTEGER REFERENCES student(id),
                    course_id INTEGER REFERENCES course(id)
                    );
                """)
    print('Таблица student_course создана')

# создает студента
def add_student(student):
    cur.execute('''
        insert into student (name,gpa,birth) values (%s,%s,%s) returning id;
        ''', (student['name'], student['gpa'], student['birth']))
    result = cur.fetchone()[0]
    print(f"Студент(ка) {student['name']} добавлен(а)")
    return result

# создает курсы
def add_course(course):
    cur.execute('''
        insert into course (name) values (%s);
        ''', (course, ))
    print(f'Курс {course} создан')

# выводит информацию студента по ID
def get_student(student_id):
    cur.execute('''
        select * from student where id = %s;
        ''', (student_id, ))
    print(f'Информация о студенты с ID {student_id}:')
    print(cur.fetchall())

# создает студентов и записывает их на курс (студенты в виде списка)
def add_students(course_id, students):
    for student in students: # раскрывает список
        id_student = add_student(student)# студент добавляется и в id_student записывается id созданного студента
        cur.execute('''
                        insert into student_course (student_id, course_id) values (%s,%s);
                    ''', (id_student, course_id))
        print(f"Студент(ка) {student['name']} добавлен(а) на курс {course_id}")

# возвращает студентов определенного курса
def get_students_in_course(course_id):
    cur.execute("""
                select student.id, student.name, course.name from student_course
                join student on student.id = student_course.student_id
                join course on course.id = student_course.course_id
                where student_course.course_id = %s;
                    """, (course_id,))
    print(f'Список студентов курса {course_id}:')
    result = cur.fetchall()
    print(result)

# create_db()

# add_student({'name':'Miroslav Sinistin', 'gpa':3.9, 'birth':'1987-01-13'})

# add_course('Экономическая теория')
# add_course('Философия')
# add_course('Логика')

# get_student(2)

# add_students(1,({'name': 'Иван Виноградов', 'gpa': 3.6, 'birth': '1986-11-09'},
#                 {'name': 'Наталья Степанова', 'gpa': 4.0, 'birth': '1984-06-15'},
#                 {'name': 'Анастасия Глаголева', 'gpa': 1.0, 'birth': '1985-05-31'}))

# get_students_in_course(1)

conn.commit()


