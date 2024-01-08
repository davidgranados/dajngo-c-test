from django.contrib import admin

from creators.models import Content, Creator

admin.site.register(Creator)
admin.site.register(Content)
