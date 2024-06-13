from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Course, Lesson, Section
# Create your views here.


class CoursesListView(ListView):
    model = Course
    template_name = 'formations/courses_list.html'
    context_object_name = 'courses'
    paginate_by = 6


class CourseDetailView(DetailView):
    model = Course
    template_name = 'formations/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = Section.objects.filter(course=self.object)
        return context


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'formations/lesson_detail.html'
    context_object_name = 'lesson'

    def get_object(self):
        # Override get_object to make sure the correct lesson is retrieved based on the course and lesson slug
        return Lesson.objects.get(slug=self.kwargs['slug'], section__course__slug=self.kwargs['course_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object.section.course
        context['sections'] = Section.objects.filter(course=course)
        return context