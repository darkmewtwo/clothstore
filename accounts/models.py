from django.contrib.auth.models import (AbstractBaseUser, AbstractUser, Group,
                                        Permission, PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Shopper(AbstractUser):
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("shopper permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="shopper_set",
        related_query_name="shopper",
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="shopper_set",
        related_query_name="shopper",
    )
    gender = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=True)
    phone_number = models.PositiveBigIntegerField()
    country_code = models.CharField(max_length=5)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
