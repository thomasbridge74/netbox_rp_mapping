# Generated by Django 4.0.4 on 2022-06-08 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_rp_mapping', '0004_remove_rpgroupentry_remark_rpgroupentry_acl_command_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rpgroupentry',
            unique_together={('group_name', 'sequence_no')},
        ),
    ]
