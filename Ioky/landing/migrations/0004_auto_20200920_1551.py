# Generated by Django 3.0.7 on 2020-09-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20200920_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Почта спросившего'),
        ),
    ]
