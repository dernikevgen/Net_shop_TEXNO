# Generated by Django 2.2 on 2019-05-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190430_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sail',
            field=models.CharField(choices=[('Наличными', 'Наличными'), ('Картой', 'Картой')], default='Наличными', max_length=40),
        ),
    ]
