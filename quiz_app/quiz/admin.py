from django.contrib import admin

from .models import Option, Question, Quiz

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
