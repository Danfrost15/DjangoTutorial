from django.contrib import admin
from .models import Question, Choice,Students_RegNo

admin.site.register(Students_RegNo)
admin.site(Choice)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question,QuestionAdmin)

