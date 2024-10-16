from django.contrib import admin
from .models import NewUser,Task
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ("email",)

# Custom User Change Form
class NewUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = NewUser
        fields = ("email", "password", "is_admin","is_active",)


class Admin(UserAdmin):
    form = NewUserChangeForm
    add_form = NewUserCreationForm
    list_display = ['id','email','is_admin',"is_active",]
    list_filter = ["is_admin",]
    fieldsets = (
        ('User Credentials',{'fields':('email','password')}),
        ('Permissions',{'fields':('is_admin',)}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2',),
        }),

    )
    search_fields  = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(NewUser,Admin)
admin.site.register(Task)

# Register your models here.
