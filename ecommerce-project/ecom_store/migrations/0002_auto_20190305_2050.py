# Generated by Django 2.1.7 on 2019-03-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=None, max_length=400, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='order',
            name='pin_code',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
