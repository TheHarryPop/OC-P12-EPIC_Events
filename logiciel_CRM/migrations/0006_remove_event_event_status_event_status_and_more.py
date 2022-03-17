# Generated by Django 4.0.3 on 2022-03-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logiciel_CRM', '0005_alter_event_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_status',
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('IN PROGRESS', 'In progress'), ('ENDED', 'Ended')], default='IN PROGRESS', max_length=64, verbose_name='status'),
        ),
        migrations.DeleteModel(
            name='EventStatus',
        ),
    ]
