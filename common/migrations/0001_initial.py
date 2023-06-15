# Generated by Django 4.2.2 on 2023-06-15 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Институт')),
            ],
            options={
                'verbose_name': 'Институт',
                'verbose_name_plural': 'Институты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Кафедра')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.institute', verbose_name='Институт')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'ordering': ['id'],
            },
        ),
    ]