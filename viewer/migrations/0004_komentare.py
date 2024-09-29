# Generated by Django 4.1 on 2024-09-28 12:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_rename_inzerat_inzeraty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('datum_komentare', models.DateTimeField(default=datetime.datetime.now)),
                ('Inzeraty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.inzeraty')),
            ],
        ),
    ]
