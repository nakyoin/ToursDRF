# Generated by Django 4.1.7 on 2023-03-30 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laba', '0003_votes_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Excourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
            options={
                'verbose_name': 'Экскурсия',
                'verbose_name_plural': 'Экскурсии',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=100, max_digits=100)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('service', models.CharField(max_length=100)),
                ('peoples', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('priceoftour', models.DecimalField(decimal_places=100, max_digits=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laba.countries')),
                ('excource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laba.excourses')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.RemoveField(
            model_name='films',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='films',
            name='category',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='commfilm',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='user',
        ),
        migrations.DeleteModel(
            name='Actors',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Films',
        ),
        migrations.DeleteModel(
            name='Votes',
        ),
        migrations.AddField(
            model_name='profile',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laba.tour'),
        ),
    ]
