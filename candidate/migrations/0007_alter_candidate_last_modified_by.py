# Generated by Django 4.2.2 on 2023-06-29 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0006_candidate_last_modified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL),
        ),
    ]
