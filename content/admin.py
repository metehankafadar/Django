from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from content.models import CImages, Menu, Content


class ContentImageInLine(admin.TabularInline):
    model = CImages
    extra = 3

class MenuContentInLine(admin.TabularInline):
    model = Content
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'image_tag', 'status', 'create_at']
    list_filter = ['status', 'type']
    inlines = [ContentImageInLine]
    prepopulated_fields = {'slug': ('title',)}


class MenuAdmin(DraggableMPTTAdmin):
    mptt_level_indent = "title"
    list_display = ('tree_actions', 'indented_title', 'status')
    list_filter = ['status']
    inlines = [MenuContentInLine]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
