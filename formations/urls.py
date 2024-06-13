from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoursesListView.as_view(), name='courses_list'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]