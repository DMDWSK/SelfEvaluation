from django.db import models


class Permissions(models.Model):
    class Meta:
        db_table = "Permisisons"
    permission = models.CharField(max_length=100, default=None)

class Roles(models.Model):
    class Meta:
        db_table = "Roles"
    role = models.CharField(max_length=60, default=None)
    permission = models.ManyToManyField(Permissions)
