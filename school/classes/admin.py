from django.contrib import admin
from .models import Discipline, Student, Professor

# Register your models here.
admin.site.register(Discipline)
admin.site.register(Student)
admin.site.register(Professor)
