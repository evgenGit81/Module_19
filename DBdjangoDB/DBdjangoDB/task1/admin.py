from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Buyer)
admin.site.register(Post)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited',)
    search_fields = ('title',)
    list_filter = ("cost", 'age_limited',)
    fieldsets = (
        ('info', {
            'fields':
                ('title', 'description', 'age_limited')
        }),
        ('title', {
            'fields':
                ('cost', 'size')
        }),

    )