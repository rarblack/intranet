from django.contrib import admin
from django.utils import timezone

from .models import Tag, Article, ArticleDetail, Activity


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_by', 'created_at')


class ArticleInline(admin.StackedInline):
    model = Article
    can_delete = False
    verbose_name_plural = 'Article'
    fk_name = 'detail'


@admin.register(ArticleDetail)
class TicketDetailAdmin(admin.ModelAdmin):
    inlines = (ArticleInline, )
    list_display = ('id', 'status', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_article_id', 'status', 'created_by', 'created_at')

    def get_article_id(self, instance):
        return instance.detail_id
    get_article_id.short_description = 'article_id'


