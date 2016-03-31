from django.contrib import admin
from website.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('phone','age')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)
admin.site.register(PostProxy)


