# Generated by Django 3.1.5 on 2021-01-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='descriptarMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=200)),
                ('llave', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='encriptarMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(max_length=200)),
                ('llave', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='encriptar',
        ),
    ]
