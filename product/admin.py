from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.product)
admin.site.register(models.Futurecoursess)
admin.site.register(models.bestteachers)
admin.site.register(models.article)
admin.site.register(models.teach)
admin.site.register(models.test_teacher)
admin.site.register(models.test_info_teacher)
admin.site.register(models.students)
admin.site.register(models.ContactMessage)