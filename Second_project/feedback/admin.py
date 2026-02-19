from django.contrib import admin
from . models import Feedback
from .urls import app_name


# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'surname',  'rating', ]