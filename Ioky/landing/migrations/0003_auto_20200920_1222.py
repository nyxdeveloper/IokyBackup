# Generated by Django 3.0.7 on 2020-09-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20200920_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Текст ответа'),
        ),
    ]
