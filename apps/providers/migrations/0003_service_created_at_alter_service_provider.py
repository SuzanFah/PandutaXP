# Generated by Django 4.2.17 on 2024-12-29 07:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_alter_provider_user_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider'),
        ),
    ]
