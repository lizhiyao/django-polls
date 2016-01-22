from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Date',               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]


# 方式一
admin.site.register(Choice)


# 方式二
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 添加一个“Filter”侧边栏，可以使人们通过pub_date字段对变更列表进行过滤
    list_filter = ['pub_date']

    # 搜索功能
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)





