# Generated by Django 4.0.5 on 2022-06-12 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TestApp', '0002_alter_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organiser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_used', models.BooleanField(default=False)),
                ('original_list_price', models.BooleanField(default=10)),
                ('is_original_listing', models.BooleanField(default=False)),
                ('is_for_sale', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestApp.event')),
            ],
        ),
    ]