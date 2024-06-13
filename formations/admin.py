from django.contrib import admin
from .models import Category, Course, Section, Lesson
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Category, CategoryAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Section, SectionAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'level', 'category', 'teacher', 'published', 'published_at', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['level', 'category', 'teacher', 'published', 'published_at', 'created_at', 'updated_at']


admin.site.register(Course, CourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Lesson, LessonAdmin)