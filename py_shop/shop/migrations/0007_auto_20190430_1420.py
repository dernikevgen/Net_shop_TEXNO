# Generated by Django 2.2 on 2019-04-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190430_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Выполняется', 'Выполняется'), ('Оплачен', 'Оплачен')], default='Принят в обработку', max_length=120),
        ),
    ]