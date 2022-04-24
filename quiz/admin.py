from django.contrib import admin
from .models import Question,Course,Result,Student
# Register your models here.
admin.site.register(Question)
admin.site.register(Course)
admin.site.register(Result)
admin.site.register(Student)