from django.contrib import admin
from .models import Student, FeeStructure, Payment

admin.site.register(Student)
admin.site.register(FeeStructure)
admin.site.register(Payment)