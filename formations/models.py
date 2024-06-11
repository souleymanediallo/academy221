from django.db import models
from django.conf import settings
from django.utils.text import slugify
from datetime import datetime


class SeoModel(models.Model):
    seo_title = models.CharField(max_length=255, blank=True, default="")
    meta_keywords = models.CharField(max_length=255, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.seo_title or "SEO Metadata"


class Category(SeoModel, models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Course(SeoModel, models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Débutant'),
        ('intermediate', 'Intermédiaire'),
        ('advanced', 'Avancé'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField(blank=True, default="")
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES, default='beginner')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_taught')
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Lesson(SeoModel, models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)