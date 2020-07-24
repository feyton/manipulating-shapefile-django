# Generated by Django 3.0.8 on 2020-07-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, upload_to='species/')),
                ('districts', models.ManyToManyField(blank=True, related_name='species', to='index.District')),
            ],
        ),
    ]
