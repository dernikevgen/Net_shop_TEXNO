# Generated by Django 2.2 on 2019-04-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190430_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], max_length=40),
        ),
    ]