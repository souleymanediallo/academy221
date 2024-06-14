from django.contrib import admin
from .models import Category, Course, Section, Lesson
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Category, CategoryAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'course']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Section, SectionAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'level', 'category']
    search_fields = ['title']
    list_filter = ['level', 'category', 'teacher', 'published', 'published_at']


admin.site.register(Course, CourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Lesson, LessonAdmin)