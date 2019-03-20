# Generated by Django 2.1.7 on 2019-03-20 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0005_auto_20190320_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='interests',
            field=models.ManyToManyField(null=True, to='ford3.Interest'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='occupation_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ford3.Occupation'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='sub_field_of_study_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ford3.SubFieldOfStudy'),
        ),
    ]