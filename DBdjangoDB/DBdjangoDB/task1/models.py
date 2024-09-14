from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10000000, decimal_places=2)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name #Вывод по умолчанию, здесь только поле name. Остальные (balance, age) не выводятся

class Game(models.Model):
    title = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=1000000, decimal_places=2)
    size = models.DecimalField(max_digits=1000000000000, decimal_places=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title

