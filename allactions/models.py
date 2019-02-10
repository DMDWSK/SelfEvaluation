from django.db import models


class Departments(models.Model):
    class Meta:
        db_table = "Departments"
        ordering = ['id']
    department = models.CharField(max_length=20, default=None)


class Sections(models.Model):
    class Meta:
        db_table = "Sections"
        ordering = ['id']
    section = models.CharField(max_length=20, default=None)
    def sectionfilter(self):
        return Stages.objects.filter(section_id=self.id).first().id


class Stages(models.Model):
    class Meta:
        db_table = "Stages"
        ordering = ['id']
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    stage = models.CharField(max_length=40,  default=None)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)


class Questions(models.Model):
    class Meta:
        db_table = "Questions"
        ordering = ['id']
    question = models.TextField(max_length=255, default=None)
    stage = models.ForeignKey(Stages, on_delete=models.CASCADE)
    department = models.ManyToManyField(Departments)
    hint = models.TextField(max_length=300, null=True, blank=True)


class Grades(models.Model):
    class Meta:
        db_table = "Grades"
        ordering = ['id']
    grade = models.CharField(max_length=60, default=None)
