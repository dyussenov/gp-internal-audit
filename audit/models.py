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

    def __str__(self):
        return self.name


class Storage(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    receive_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    current_price = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        self.expiration_date = datetime.datetime.now() + datetime.timedelta(days=self.item.operation_life * 30)

        price = self.item.price
        amortization = self.item.amortization
        self.current_price = price - price/100*amortization

        super(Storage, self).save(*args, **kwargs)

    def __str__(self):
        return self.item.name
