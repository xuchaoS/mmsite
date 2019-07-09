# Generated by Django 2.2.2 on 2019-07-09 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190701_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('flow', models.PositiveIntegerField()),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.Port')),
            ],
        ),
    ]
