from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# crea el admin de forma predeterminda
# admin.site.register(Question)

# customized
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # add choice into question
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['publication_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # change list view, add more fields
    list_display = ('question_text', 'publication_date', 'was_published_recently')
    list_filter = ['publication_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)