# Generated by Django 4.2.2 on 2024-10-30 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='your email address', max_length=254, unique=True, verbose_name='email')),
                ('full_name', models.CharField(help_text='Full name', max_length=200, verbose_name="client's full name")),
                ('comment', models.TextField(help_text='leave oyur comment here', max_length=100)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Mailing_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Текст письма')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='mailing name')),
                ('type', models.TextField(blank=True, choices=[('short_list', 'only headers'), ('long_list', 'headers and brief summary'), ('long_read', 'full text in the mailing')], null=True, verbose_name='mailing type')),
                ('start_time', models.DateTimeField(verbose_name='Start of the mailing')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='End of the mailing')),
                ('periodicity', models.CharField(choices=[('daily', 'Once a day'), ('weekly', 'once a week'), ('monthly', 'Once a month')], max_length=10, verbose_name='How often')),
                ('status', models.CharField(choices=[('created', 'Created'), ('active', 'active'), ('completed', 'completed')], max_length=10, verbose_name='Status')),
                ('client', models.ManyToManyField(to='mailing.client', verbose_name='Clients')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing_message', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Mailing',
                'verbose_name_plural': 'Mailings',
            },
        ),
        migrations.CreateModel(
            name='Last_Mailing_Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Not_Attempted', 'Not sent yet'), ('Success', 'Successful attempt'), ('failed', 'Attempt failed')], max_length=20, verbose_name='Sent Status')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='Server response')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Mailing')),
            ],
            options={
                'verbose_name': 'Mailing status',
                'verbose_name_plural': 'Mailings status',
            },
        ),
    ]
