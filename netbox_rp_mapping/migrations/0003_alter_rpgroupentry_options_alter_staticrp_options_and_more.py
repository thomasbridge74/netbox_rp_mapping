# Generated by Django 4.0.4 on 2022-06-05 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0153_created_datetimefield'),
        ('netbox_rp_mapping', '0002_alter_rpgroupentry_mcast_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rpgroupentry',
            options={'ordering': ('group_name', 'sequence_no'), 'verbose_name_plural': 'RP Group Entries'},
        ),
        migrations.AlterModelOptions(
            name='staticrp',
            options={'ordering': ('rp_address',), 'verbose_name_plural': 'Static RPs'},
        ),
        migrations.AddField(
            model_name='staticrp',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcim.region'),
        ),
        migrations.AddField(
            model_name='staticrp',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcim.site'),
        ),
    ]