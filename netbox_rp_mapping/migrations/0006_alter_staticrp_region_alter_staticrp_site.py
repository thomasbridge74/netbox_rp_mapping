# Generated by Django 4.0.4 on 2022-06-08 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0153_created_datetimefield'),
        ('netbox_rp_mapping', '0005_alter_rpgroupentry_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticrp',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcim.region'),
        ),
        migrations.AlterField(
            model_name='staticrp',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcim.site'),
        ),
    ]