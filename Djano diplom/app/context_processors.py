from app.models import Section

def navbar(request):
    categories = Section.objects.all()
    return {'navbar_categories': categories}