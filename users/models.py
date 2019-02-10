# from django.db import models
# from allactions import Departments
#
# # Create your models here.
# class Users(models.Model):
#     class Meta:
#         db_table = "Users"
#
#     name = models.CharField(max_length=60, default=None)
#     surname = models.CharField(max_length=60, default=None)
#     role = models.ForeignKey('RolesModel', on_delete=models.DO_NOTHING)
#     department = models.ManyToManyField()
