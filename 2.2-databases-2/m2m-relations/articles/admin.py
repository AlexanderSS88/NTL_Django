from django.contrib import admin
from .models import Article, Tags
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class TagsInlineFormset(BaseInlineFormSet):
    def formset(self):
        for form in self.forms:
# В form.cleaned_data будет словарь с данными каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
# вызовом исключения ValidationError можно указать админке о наличие ошибки
# таким образом объект не будет сохранен,а пользователю выведется соответствующее сообщение об ошибке

            raise ValidationError('Тут всегда ошибка')
        return super().formset()  # вызываем базовый код переопределяемого метода

class TagsInline(admin.TabularInline):
    model = Tags
    formset = TagsInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsInline]



