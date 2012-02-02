from Factivity.annual.models import Activity, Category
from django.contrib import admin

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('username', 'description', 'category', 'date')
    list_filter = ['username', 'category']
    search_fields = ['username']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('short_description','long_description')
    
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Category, CategoryAdmin)