# Generated by Django 3.2.16 on 2023-01-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='书名')),
                ('author', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
                ('stock', models.SmallIntegerField(default=0, verbose_name='库存')),
                ('sold', models.SmallIntegerField(default=0, verbose_name='已售数量')),
            ],
            options={
                'verbose_name': '书详细信息',
                'verbose_name_plural': '书详细信息',
                'db_table': 'book',
            },
        ),
    ]
