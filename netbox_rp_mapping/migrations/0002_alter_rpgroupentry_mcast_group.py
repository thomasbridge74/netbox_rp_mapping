# Generated by Django 4.0.4 on 2022-05-29 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0057_created_datetimefield'),
        ('netbox_rp_mapping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpgroupentry',
            name='mcast_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mcast_groups', to='ipam.prefix'),
        ),
    ]
