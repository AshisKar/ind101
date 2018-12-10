# Generated by Django 2.0.8 on 2018-12-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_auto_20181210_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='age',
            field=models.CharField(choices=[('0-6', 'less than 6 Years'), ('7-12', '7 to 12 Years'), ('13-16', '13 to 16 years'), ('17-18', '17 to 18 years'), ('19-21', '19 to 21 Years'), ('22-25', '22 to 25 years'), ('26-32', '26 to 32 years'), ('33-40', '33 to 40 years'), ('41-50', '41 to 50 years'), ('51-60', '51 to 60 years'), ('60-75', '60 to 75 years'), ('75+', 'above 75'), ('0-100', 'all')], help_text='enter age', max_length=15),
        ),
    ]
