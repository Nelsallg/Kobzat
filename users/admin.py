# from django.contrib import admin
# from app.models import CustomUser
# from django.contrib.auth.admin import UserAdmin
# from django.forms import TextInput, Textarea
# # Register your models here.

# class UserAdminConfig(UserAdmin):
#     model = CustomUser
#     search_fields = ('email', 'first_name',)
#     list_filter = ('email', 'first_name', 'is_active', 'is_staff')
#     # ordering = ('-start_date',)
#     list_display = ('email', 'first_name',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('email', 'first_name',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         # ('Personal', {'fields': ('about',)}),
#     )
#     # formfield_overrides = {
#     #     CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     # }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )

# admin.site.register(CustomUser, UserAdminConfig)