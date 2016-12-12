# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-12 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BiographyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_biography', models.TextField(blank=True, max_length=512, verbose_name='Biography')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='people.Biography')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_biography_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ordering')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='LinkTypeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, help_text='Use this field to define a simple identifier that can be used to style the different link types (i.e. assign social media icons to them)', max_length=256, verbose_name='Slug')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='people.LinkType')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_linktype_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Nationalities',
            },
        ),
        migrations.CreateModel(
            name='NationalityTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='people.Nationality')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_nationality_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roman_first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='First name')),
                ('roman_last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last name')),
                ('non_roman_first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Non roman first name')),
                ('non_roman_last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Non roman last name')),
                ('gender', models.CharField(blank=True, choices=[(b'male', 'male'), (b'female', 'female')], max_length=16, null=True, verbose_name='Gender')),
                ('title', models.CharField(blank=True, choices=[(b'Dr', 'Dr'), (b'Prof', 'Prof'), (b'Prof Dr', 'Prof Dr')], max_length=16, null=True, verbose_name='Title')),
                ('chosen_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Chosen name')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('ordering', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ordering')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Nationality', verbose_name='Nationality')),
                ('picture', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='Picture')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='PersonPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='people_personpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('display_type', models.CharField(choices=[(b'small', 'small'), (b'big', 'big')], max_length=256, verbose_name='Display type')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person', verbose_name='Person')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Role')),
                ('role_description', models.TextField(blank=True, max_length=4000, verbose_name='Role description')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='people.Role')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_role_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ShortBiography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='short_biography_person', to='people.Person', verbose_name='User Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ShortBiographyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_biography', models.TextField(blank=True, max_length=255, verbose_name='Short bio')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='people.ShortBiography')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_shortbiography_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Role', verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='link',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.LinkType', verbose_name='Link type'),
        ),
        migrations.AddField(
            model_name='link',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person', verbose_name='Person'),
        ),
        migrations.AddField(
            model_name='biography',
            name='person',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='long_biography_person', to='people.Person', verbose_name='User Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='shortbiographytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='roletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='nationalitytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='linktypetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='biographytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
