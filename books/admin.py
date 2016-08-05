# -*-coding:utf-8 -*-
from django.contrib import admin

# Register your models here.

from books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name', 'last_name')
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date',)#过滤
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)#排序
	#fields = ('title', 'authors', 'publisher', 'publication_date')#自定义编辑表单
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
