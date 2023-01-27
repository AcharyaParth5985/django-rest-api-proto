from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as UserManager_
from typing import Optional, Iterable

# from user import managers
from user.roles import Role
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from typing import List, Any


def number_validator(value: Any) -> None:
    if len(value) != 10:
        raise ValidationError(
            _("Phone Number must be 10 digit long"),
        )
    if not all(i.isdigit() for i in value):
        raise ValidationError(_("Only numbers are allowed"))


# Create your models here.
class User(AbstractUser):
    """
    `User` table contains ALL the users in the system.
    other classes like `Admin` `Student` `Volunteer` inherit from this class
    and are saved as a pointer to original `User` in table with other properties
    saved in their own table

    Hence, the _base_role is Undefined, Roles can be found at `users.roles.Role`
    """

    _base_role = Role.UNDEFINED
    _predefined_permissions: List[str] = []

    role = models.PositiveSmallIntegerField(choices=Role.choices)
    phone_number = models.CharField(max_length=10, validators=[number_validator])

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ) -> None:
        self.role = self._base_role
        saved_user = super().save(force_insert, force_update, using, update_fields)
        # assigning permissions AFTER the user is added in the database
        self.user_permissions.add(
            *[Permission.objects.get(codename=i) for i in self._predefined_permissions]
        )
        return saved_user


class Admin(User):
    _base_role = Role.ADMIN

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ) -> None:
        self.is_staff = True
        self.is_superuser = True
        return super().save(force_insert, force_update, using, update_fields)


class Student(User):
    _base_role = Role.STUDENT
    marks = models.IntegerField()
    _predefined_permissions = ["view_student"]

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Volunteer(User):
    _base_role = Role.VOLUNTEER
    job_numbers = models.PositiveSmallIntegerField()
    _predefined_permissions = ["view_volunteer"]

    class Meta:
        verbose_name = "Volunteer"
        verbose_name_plural = "Volunteers"


class DeptOfficer(User):
    _base_role = Role.DEPT_OFFICER
    dept = models.TextField()
    _predefined_permissions = ["view_deptofficer"]

    class Meta:
        verbose_name = "Department Officer"
        verbose_name_plural = "Department Officers"
