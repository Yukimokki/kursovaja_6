# Generated by Django 4.2.2 on 2024-11-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='mailing name'),
        ),
    ]
