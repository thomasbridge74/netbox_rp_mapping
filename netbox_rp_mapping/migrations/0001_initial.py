# Generated by Django 4.0.4 on 2022-05-29 09:54

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('ipam', '0057_created_datetimefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticRP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('rp_acl_name', models.CharField(max_length=64, unique=True)),
                ('override', models.BooleanField(default=True)),
                ('rp_address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ip_address', to='ipam.ipaddress')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('rp_address',),
            },
        ),
        migrations.CreateModel(
            name='RPGroupEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('sequence_no', models.PositiveBigIntegerField()),
                ('remark', models.BooleanField()),
                ('comments', models.CharField(max_length=128)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcast_rp', to='netbox_rp_mapping.staticrp')),
                ('mcast_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mcast_groups', to='ipam.prefix')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('group_name', 'sequence_no'),
            },
        ),
    ]
