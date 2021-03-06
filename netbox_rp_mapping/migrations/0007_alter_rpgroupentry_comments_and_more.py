# Generated by Django 4.0.4 on 2022-06-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0057_created_datetimefield'),
        ('netbox_rp_mapping', '0006_alter_staticrp_region_alter_staticrp_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpgroupentry',
            name='comments',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='rpgroupentry',
            name='mcast_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mcast_groups', to='ipam.prefix'),
        ),
    ]
