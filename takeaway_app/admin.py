from django.contrib import admin
from takeaway_app.models import Menu, Food, Slide
# Register your models here.

class foodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'menu']

admin.site.register(Menu)
admin.site.register(Food, foodAdmin)
admin.site.register(Slide)