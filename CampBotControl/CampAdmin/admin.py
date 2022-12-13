from django.contrib import admin

from .models import TypeEducation, Faculties, Profile, Data, Users

@admin.register(Users)
class ClientsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Users._meta.get_fields()]
    list_editable = ('is_active','admin', 'department',)
    search_fields = ('first_name','last_name','city','is_active',)
    list_filter = ('date_reg',)
    empty_value_display = '-пусто-'

@admin.register(TypeEducation)
class TypeOfEducationAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Faculties)
class FacultiesAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('pk','type_education','faculties', 'profile','descriptions',)
    list_editable = ('type_education','faculties', 'profile','descriptions')
    search_fields = ('type_education','faculties','profile','descriptions',)
    list_filter = ('type_education',)
    empty_value_display = '-пусто-'
