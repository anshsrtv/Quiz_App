from django.contrib import admin
from .models import Quiz, Question, Answer, Attempt

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Attempt)
admin.site.register(Answer)