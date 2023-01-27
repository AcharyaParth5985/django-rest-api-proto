from django.contrib import admin
from user import models as m
from django.contrib.auth.admin import UserAdmin as UserAdmin_
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import ModelAdmin

# Register your models here.
# @admin.register(m.User)
# class UserAdmin(UserAdmin_):
#     fieldsets = (
#         (
#             None,
#             {
#                 "fields": (
#                     "username",
#                     "password",
#                     "phone_number",
#                     "role",
#                 )
#             },
#         ),
#         (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )

#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "phone_number", "password1", "password2"),
#             },
#         ),
#     )


@admin.register(m.Admin)
class AdminUserAdmin(UserAdmin_):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                    "phone_number",
                )
            },
        ),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "phone_number", "password1", "password2"),
            },
        ),
    )


@admin.register(m.Student)
class StudentAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone_number", "marks")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "marks",
                ),
            },
        ),
    )


@admin.register(m.Volunteer)
class VolunteerAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone_number", "job_numbers")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "job_numbers",
                ),
            },
        ),
    )


@admin.register(m.DeptOfficer)
class DeptOfficerAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone_number", "dept")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "dept",
                ),
            },
        ),
    )


# TODO : add filters and stuff
@admin.register(m.Company)
class CompanyAdmin(ModelAdmin):
    list_display = (
        "name",
        "email_id",
        "hr_name",
        "industry_type",
        "company_type",
    )


# TODO : add filters and stuff
@admin.register(m.CurrentOpening)
class CurrentOpeningsAdmin(ModelAdmin):
    list_display = (
        "job_title",
        "opening_year",
        "nature_of_job",
        "vacancy_count",
        "min_package",
        "gender_preference",
    )
