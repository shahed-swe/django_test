# Generated by Django 2.2 on 2019-10-03 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191003_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='date',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=1570119775.4505131),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(),
        ),
    ]
