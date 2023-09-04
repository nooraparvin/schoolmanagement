from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)

    # wiki_link = models.URLField()

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# class Material(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name


class UserOrder(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    purpose = models.CharField(max_length=20)
    # materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
