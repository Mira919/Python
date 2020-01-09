import hashlib

def generator(file):
    with open(file, 'r') as f:
        for line in f:
            str = line.encode('utf-8')
            hash_str = hashlib.md5(str)
            yield hash_str.hexdigest()

for hash_str in generator('Python.txt'):
    print(hash_str)


