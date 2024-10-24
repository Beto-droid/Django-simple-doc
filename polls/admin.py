from django.contrib import admin

# Register your models here.

from .models import Question, UserProfile, Choice


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(UserProfile)
admin.site.register(Choice)
