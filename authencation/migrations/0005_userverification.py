# Generated by Django 4.2.7 on 2024-05-12 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authencation', '0004_user_otp_sent_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_code', models.CharField(blank=True, max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
