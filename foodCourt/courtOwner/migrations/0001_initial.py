# Generated by Django 4.2.5 on 2023-10-11 11:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=500)),
                ('qr', models.ImageField(default='', upload_to='image/QR')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('restro', models.CharField(default='', max_length=100)),
                ('OwnerId', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courtOwner.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('desc', models.CharField(default='', max_length=300)),
                ('photo', models.ImageField(default='', upload_to='image/restraurant')),
                ('rastroId', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courtOwner.restaurants')),
            ],
        ),
    ]