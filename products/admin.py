from django.contrib import admin
from .models import Product,Category,File
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','parent','title','isEnable','createdTime']
    list_filter = ['isEnable', 'parent']
    search_fields = ['title']

class FileInlineAdmin(admin.TabularInline):
    model = File
    fields = ['title', 'fileType', 'file', 'isEnable']
    extra = 0

@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_display = ['id','title','isEnable','createdTime']
    list_filter = ['isEnable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin]