# Generated by Django 5.1.4 on 2024-12-29 20:05

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_run', models.DateTimeField(auto_now=True, verbose_name='Last Run')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('program_path', models.CharField(blank=True, max_length=512, null=True, verbose_name='Program Path')),
                ('status', models.BooleanField(default=False, verbose_name='Not Active Status')),
                ('commands', models.TextField(blank=True, null=True, verbose_name='Commands')),
                ('command_line_args', models.TextField(blank=True, null=True, verbose_name='Command Line Arguments')),
                ('window_type', models.CharField(choices=[('new window', 'New Window'), ('current window', 'Current Window')], default='new window', max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scripts', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
