from django.shortcuts import render
from formations.models import Course


# Create your views here.
def home(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "pages/index.html", context)