# Generated by Django 3.0.5 on 2020-06-12 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_portal', '0009_task_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
