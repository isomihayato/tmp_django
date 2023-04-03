from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',              {'fields': ['question_text']}),
        ('Date information',{'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)