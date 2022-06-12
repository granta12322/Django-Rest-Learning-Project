# Generated by Django 4.0.5 on 2022-06-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('venue', models.CharField(default='9 Bruce Street', max_length=200)),
                ('start_time', models.DateTimeField(default='09/11/2022')),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]