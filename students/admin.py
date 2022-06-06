from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "grade", "major", "address"]
    search_fields = ["name"]

admin.site.register(Student, StudentAdmin)
