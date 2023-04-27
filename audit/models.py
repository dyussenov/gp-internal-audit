from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(unique=True, max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.FloatField()
    amortization = models.IntegerField()
    operation_life = models.IntegerField()
    receive_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()

    def save(self, *args, **kwargs):
        self.expiration_date = datetime.datetime.now() + datetime.timedelta(days=self.operation_life * 30)

        # call the save() method of the parent
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
