# Generated by Django 2.1.7 on 2019-04-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecallers', '0001_initial'),
        ('candidates', '0005_auto_20190416_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telecaller',
            name='generated_by',
        ),
        migrations.RemoveField(
            model_name='telecaller',
            name='telecaller',
        ),
        migrations.AddField(
            model_name='telecaller',
            name='telecaller',
            field=models.ManyToManyField(blank=True, to='telecallers.Telecallers'),
        ),
    ]
