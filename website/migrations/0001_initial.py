# Generated by Django 4.1.7 on 2023-03-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_line', models.CharField(max_length=100, verbose_name='Tag Line')),
                ('summary', models.CharField(max_length=250, verbose_name='Summary')),
                ('birthday', models.DateField(null=True, verbose_name='DOB')),
                ('age', models.IntegerField(null=True)),
                ('website', models.URLField(null=True)),
                ('degree', models.CharField(choices=[('High School', 'High School'), ('Bac', 'Bachelour'), ('Master', 'Master')], max_length=50, null=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('freelance', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
