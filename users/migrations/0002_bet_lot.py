# Generated by Django 3.2.4 on 2021-06-30 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_owner'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lots', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='lots', to='pets.pet', verbose_name='Pet')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bets', to='users.lot', verbose_name='Lot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bets', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
