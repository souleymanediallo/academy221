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
