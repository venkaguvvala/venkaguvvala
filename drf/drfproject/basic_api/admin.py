from django.contrib import admin
from .models import DRFPost
# Register your models here.

#class DRFPostAdmin(admin.ModelAdmin):
#    list_display=['id','name','author','uploaded','rating']

#admin.site.register(DRFPostAdmin)
admin.site.register(DRFPost)
