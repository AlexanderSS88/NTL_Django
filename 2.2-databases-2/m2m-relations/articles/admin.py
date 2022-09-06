from django.contrib import admin
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        number = 0
        for form in self.forms:
            if number > 1:
                raise ValidationError('Более одного главного раздела!')
            if form.cleaned_data.get('is_main'):
                number += 1
            if form.cleaned_data.get('DELETE'):
                continue
        if number == 0:
            raise ValidationError('Выберите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]



