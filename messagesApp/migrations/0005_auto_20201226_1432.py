# Generated by Django 3.1.3 on 2020-12-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesApp', '0004_auto_20201226_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
