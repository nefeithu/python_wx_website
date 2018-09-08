from django.contrib import admin

# Register your models here.
from blog.models import Article

import sys;

reload(sys);
sys.setdefaultencoding("utf8")


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title',  'pub_date']


admin.site.register(Article, ArticleAdmin)
