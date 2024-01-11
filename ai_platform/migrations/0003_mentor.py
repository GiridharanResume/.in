# Generated by Django 4.1.11 on 2024-01-05 07:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ai_platform', '0002_signup_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
