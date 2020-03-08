# Generated by Django 3.0.4 on 2020-03-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('marks', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('isImportant', models.BooleanField(default=False)),
                ('chapter', models.IntegerField()),
                ('time', models.IntegerField()),
                ('repeated', models.IntegerField()),
            ],
        ),
    ]
