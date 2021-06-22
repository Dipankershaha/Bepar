from django.contrib import admin
from App_Login.models import User, Profile

# Register your models here.




class CustomProfile(admin.ModelAdmin):
    model = User

    list_display = ['email','is_staff']
    actions = ['make_stuff', 'make_user', 'block', 'unBlock']

    def make_stuff(self,request, queryset):
        queryset.update(is_staff = True)
    def make_user(self,request, queryset):
        queryset.update(is_staff = False)
    def block(self,request, queryset):
        queryset.update(is_active = False)
    def unBlock(self,request, queryset):
        queryset.update(is_active = True)

admin.site.register(User, CustomProfile)
admin.site.register(Profile)