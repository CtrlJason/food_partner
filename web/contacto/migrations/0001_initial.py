# Generated by Django 4.2.16 on 2024-10-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('celular', models.IntegerField(null=True)),
                ('correo', models.EmailField(max_length=254)),
                ('asunto', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
