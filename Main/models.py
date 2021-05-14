from django.contrib import admin
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    patronymic = models.CharField(max_length=30, null=True)
    birth_year = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_day = models.IntegerField(null=True)
    mob_number = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


admin.site.register(Person)


class VK_acc(models.Model):
    city = models.CharField(max_length=30, null=True)
    school = models.CharField(max_length=30, null=True)
    university = models.CharField(max_length=50, null=True)
    id_person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


admin.site.register(VK_acc)


class VK_net(models.Model):
    who = models.ForeignKey("VK_acc", on_delete=models.CASCADE, related_name="+")
    on_whom = models.ForeignKey("VK_acc", on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.who} on {self.on_whom}"


admin.site.register(VK_net)


class Instagram_acc(models.Model):
    id_person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


admin.site.register(Instagram_acc)


class Instagram_net(models.Model):
    who = models.ForeignKey("Instagram_acc", on_delete=models.CASCADE, related_name="+")
    on_whom = models.ForeignKey("Instagram_acc", on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.who} on {self.on_whom}"


admin.site.register(Instagram_net)


class VK_group(models.Model):
    vk_accs = models.ManyToManyField(VK_acc, related_name="+")
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name}"


admin.site.register(VK_group)
