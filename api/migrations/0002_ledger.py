# Generated by Django 3.2.5 on 2021-07-22 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('ledger_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
