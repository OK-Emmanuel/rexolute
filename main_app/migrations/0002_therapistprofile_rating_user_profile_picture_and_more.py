# Generated by Django 5.1.4 on 2025-01-08 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapistprofile',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('client', 'Client'), ('therapist', 'Therapist')], default='client', max_length=10),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateTimeField()),
                ('duration_minutes', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_sessions', to=settings.AUTH_USER_MODEL)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='main_app.therapistprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('reference_id', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('session', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.session')),
            ],
        ),
    ]
