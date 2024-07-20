from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tour(models.Model):
    night_from = models.TimeField()
    night_till = models.TimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
    price = models.IntegerField()
    adult = models.IntegerField(blank=True, null=True)
    child = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default='1')
