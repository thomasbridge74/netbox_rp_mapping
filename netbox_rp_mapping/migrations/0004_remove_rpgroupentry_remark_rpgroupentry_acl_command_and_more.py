# Generated by Django 4.0.4 on 2022-06-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_rp_mapping', '0003_alter_rpgroupentry_options_alter_staticrp_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpgroupentry',
            name='remark',
        ),
        migrations.AddField(
            model_name='rpgroupentry',
            name='acl_command',
            field=models.CharField(default='remark', max_length=9),
        ),
        migrations.AddField(
            model_name='staticrp',
            name='acl_counters',
            field=models.BooleanField(default=False),
        ),
    ]
