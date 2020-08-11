from django.db import models
from django.urls import reverse


class Discipline(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('classes:discipline_detail', args=[self.pk])


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    year = models.IntegerField(default=1)
    discipline = models.ManyToManyField(to=Discipline)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Professor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    discipline = models.OneToOneField(to=Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
