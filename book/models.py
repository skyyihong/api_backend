from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True, verbose_name="书名")
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, blank=False,
                                verbose_name="价格")
    stock = models.SmallIntegerField(default=0, verbose_name="库存")
    sold = models.SmallIntegerField(default=0, verbose_name="已售数量")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = "书详细信息"
        verbose_name_plural = verbose_name
