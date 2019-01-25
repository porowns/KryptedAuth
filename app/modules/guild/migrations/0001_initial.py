# Generated by Django 2.1.5 on 2019-01-25 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.CharField(max_length=8)),
                ('date_formed', models.DateField(auto_now=True)),
                ('image', models.URLField()),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guild', to='auth.Group')),
                ('users', models.ManyToManyField(related_name='guilds_in', to=settings.AUTH_USER_MODEL)),
                ('users_managing', models.ManyToManyField(related_name='guilds_managing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuildApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], max_length=16)),
                ('request_date', models.DateField(auto_now=True)),
                ('response_date', models.DateField(blank=True, null=True)),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('response_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications_assigned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('manage_guild_applications', 'Can manage Guild applications'), ('audit_eve_applications', 'Can audit an EVE application')),
            },
        ),
        migrations.CreateModel(
            name='GuildApplicationQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('RESPONSE', 'Response'), ('MODAL', 'Modal')], max_length=16)),
                ('choices', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuildApplicationResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guild.GuildApplication')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guild.GuildApplicationQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='GuildApplicationTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='guild.Guild')),
                ('questions', models.ManyToManyField(blank=True, to='guild.GuildApplicationQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='guildapplication',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guild.GuildApplicationTemplate'),
        ),
    ]