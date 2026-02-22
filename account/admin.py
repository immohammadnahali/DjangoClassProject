from django.contrib import admin
from . import models

admin.site.register(models.new_user)

#
# @admin.register(Product):
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'category')
#     list_filter = ('category',)
#
# admin.site.register(Category)
