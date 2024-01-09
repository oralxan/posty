from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'image','created_date','description','price','horse_power','capacity','color','brand')
    list_display_links = ('id','title', 'description', 'image','created_date','description','price','horse_power','capacity','color','brand')
admin.site.register(Post,PostAdmin)
