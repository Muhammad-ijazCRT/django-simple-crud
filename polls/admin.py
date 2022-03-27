from django.contrib import admin

from polls.models import Student

# Register your models here.
@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone']