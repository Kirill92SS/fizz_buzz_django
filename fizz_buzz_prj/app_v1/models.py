from django.db import models


class FizzBuzz(models.Model):
    number = models.IntegerField(db_index=True)
    data = models.CharField(default='FizzBuzz', max_length=10)

    def __str__(self):
        return self.data


class Fizz(models.Model):
    number = models.IntegerField(db_index=True)
    data = models.CharField(default='Fizz', max_length=10)

    def __str__(self):
        return self.data


class Buzz(models.Model):
    number = models.IntegerField(db_index=True)
    data = models.CharField(default='Buzz', max_length=10)

    def __str__(self):
        return self.data
