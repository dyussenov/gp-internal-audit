from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(unique=True, max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=60)
    item_code = models.IntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.FloatField()
    is_amortization = models.BooleanField(default=True)
    amortization = models.IntegerField()
    is_monthly_amortizations = models.BooleanField(default=False)
    operation_life = models.IntegerField()
    image = models.ImageField(upload_to='images/items/', null=True, default=None)

    def __str__(self):
        return self.name


class Storage(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    receive_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    current_price = models.FloatField(default=0.0)
    group = models.CharField(default='1', max_length=44)

    def save(self, *args, **kwargs):
        self.expiration_date = datetime.datetime.now() + datetime.timedelta(days=self.item.operation_life * 30)
        price = self.item.price
        if not self.receive_date and self.item.is_amortization:
            self.current_price = price
            super(Storage, self).save(*args, **kwargs)
        elif self.receive_date:
            months = (datetime.date.today() - self.receive_date) // 30
            amortization_percentage = months.days * self.item.amortization
            self.current_price = price - price / 100 * amortization_percentage
            super(Storage, self).save(*args, **kwargs)
        else:
            self.current_price = price
            super(Storage, self).save(*args, **kwargs)


    def __str__(self):
        return self.item.name
