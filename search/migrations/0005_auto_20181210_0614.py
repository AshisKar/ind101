# Generated by Django 2.0.8 on 2018-12-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20181209_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='age',
            field=models.IntegerField(help_text='enter age', null=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='annual_income_range',
            field=models.IntegerField(help_text='enter annual income', null=True),
        ),
    ]
