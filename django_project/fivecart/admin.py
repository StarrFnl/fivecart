from django.contrib import admin

# Register your models here.
from .models import User, Company, BookWriter, Book, Report

admin.site.register(User)
admin.site.register(Company)
admin.site.register(BookWriter)
admin.site.register(Book)
admin.site.register(Report)
