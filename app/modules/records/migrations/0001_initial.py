# Generated by Django 2.1.5 on 2019-01-25 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('engagement', '0001_initial'),
        ('guild', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('participation', 'Participation'), ('registration', 'Registration')], max_length=32)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engagement.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuildLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('add_user', 'Add User'), ('remove_user', 'Remove User')], max_length=32)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guild.Guild')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('started_survey', 'Started Survey'), ('completed_survey', 'Completed Survey')], max_length=32)),
                ('date', models.DateField(auto_now=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engagement.Survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]