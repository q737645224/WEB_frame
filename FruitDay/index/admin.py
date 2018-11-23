from django.contrib import admin

# Register your models here.

from index.models import *

class GoodsAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('goodsType',)
    list_display = ('title','price','spec')


admin.site.register(GoodsType)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(Users)