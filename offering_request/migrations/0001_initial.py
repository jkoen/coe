# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-19 12:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offering_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insight_quote', models.IntegerField(default=0)),
                ('customer_name', models.CharField(default='Not Applicable', max_length=120)),
                ('country', models.CharField(choices=[(b'Afghanistan', b'Afghanistan'), (b'Albania', b'Albania'), (b'Algeria', b'Algeria'), (b'Andorra', b'Andorra'), (b'Angola', b'Angola'), (b'Austria', b'Austria'), (b'Bahrain', b'Bahrain'), (b'Belgium', b'Belgium'), (b'Bolivia', b'Bolivia'), (b'Botswana', b'Botswana'), (b'Burundi', b'Burundi'), (b'Croatia', b'Croatia'), (b'Cyprus', b'Cyprus'), (b'Czech Republic', b'Czech Republic'), (b'Denmark', b'Denmark'), (b'Djibouti', b'Djibouti'), (b'Egypt', b'Egypt'), (b'Ethiopia', b'Ethiopia'), (b'Finland', b'Finland'), (b'France', b'France'), (b'Gabon', b'Gabon'), (b'United Kingdom', b'United Kingdom'), (b'Gambia', b'Gambia'), (b'Georgia', b'Georgia'), (b'Germany', b'Germany'), (b'Ghana', b'Ghana'), (b'Greece', b'Greece'), (b'Guinea', b'Guinea'), (b'Hungary', b'Hungary'), (b'Iceland', b'Iceland'), (b'Ireland', b'Ireland'), (b'Israel', b'Israel'), (b'Isle of', b'Isle of'), (b'Italy', b'Italy'), (b'Jordan', b'Jordan'), (b'Kenya', b'Kenya'), (b'Kuwait', b'Kuwait'), (b'Lebanon', b'Lebanon'), (b'Lesotho', b'Lesotho'), (b'Liberia', b'Liberia'), (b'Liechtenstein', b'Liechtenstein'), (b'Lithuania', b'Lithuania'), (b'Luxembourg', b'Luxembourg'), (b'Macao', b'Macao'), (b'Madagascar', b'Madagascar'), (b'Malawi', b'Malawi'), (b'Malaysia', b'Malaysia'), (b'Maldives', b'Maldives'), (b'Mali', b'Mali'), (b'Malta', b'Malta'), (b'Martinique', b'Martinique'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Mayotte', b'Mayotte'), (b'Morocco', b'Morocco'), (b'Mozambique', b'Mozambique'), (b'Namibia', b'Namibia'), (b'Nauru', b'Nauru'), (b'Nepal', b'Nepal'), (b'Netherlands', b'Netherlands'), (b'Nicaragua', b'Nicaragua'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'Norway', b'Norway'), (b'Oman', b'Oman'), (b'Pakistan', b'Pakistan'), (b'Philippines', b'Philippines'), (b'Poland', b'Poland'), (b'Portugal', b'Portugal'), (b'Puerto Rico', b'Puerto Rico'), (b'Qatar', b'Qatar'), (b'Reunion', b'Reunion'), (b'Romania', b'Romania'), (b'Rwanda', b'Rwanda'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Senegal', b'Senegal'), (b'Serbia', b'Serbia'), (b'Russia', b'Russia'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Slovakia', b'Slovakia'), (b'Slovenia', b'Slovenia'), (b'Somalia', b'Somalia'), (b'South Africa', b'South Africa'), (b'Spain', b'Spain'), (b'Sri Lanka', b'Sri Lanka'), (b'Sudan', b'Sudan'), (b'Swaziland', b'Swaziland'), (b'Sweden', b'Sweden'), (b'Switzerland', b'Switzerland'), (b'Tonga', b'Tonga'), (b'Tunisia', b'Tunisia'), (b'Turkey', b'Turkey'), (b'Uganda', b'Uganda'), (b'Ukraine', b'Ukraine'), (b'United Arab', b'United Arab'), (b'Yemen', b'Yemen'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe')], max_length=14)),
                ('deal_value', models.IntegerField(default=0)),
                ('request_date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[(b'OPEN UNALLOCATED', b'Open Unallocated'), (b'OPEN ALLOCATED', b'Open Allocated'), (b'SUCCESSFUL', b'Successful'), (b'UNSUCCESSFUL', b'Unsuccessful'), (b'CANCELLED', b'Cancelled')], default='NEW', max_length=12)),
                ('order_number', models.IntegerField(default=0)),
                ('requester_name', models.CharField(max_length=35)),
                ('requester_email', models.EmailField(max_length=254)),
                ('requester_mobile_number', models.CharField(max_length=14)),
                ('approval_manager_name', models.CharField(max_length=35)),
                ('approval_manager_email', models.EmailField(max_length=254)),
                ('presales_name', models.CharField(max_length=35)),
                ('presales_email', models.EmailField(max_length=254)),
                ('solution_support', models.CharField(choices=[(b'YES', b'Yes'), (b'NO', b'No')], max_length=3)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(choices=[(b'EDC', b'EDC Zaltbommel'), (b'CUSTOMER', b'Customer Premises')], max_length=13)),
                ('solution_design', models.FileField(upload_to='solution_design/%Y-%m-%d')),
                ('testplan', models.FileField(blank=True, null=True, upload_to='testplan/%Y-%m-%d')),
                ('request_description', models.TextField()),
                ('audience_description', models.TextField()),
                ('offering', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='offering_request.Offering')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('offerings', models.ManyToManyField(blank=True, help_text='List of COE offerings to show for this platform', to='offering_request.Offering')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hide_fields', models.CharField(blank=True, default='', help_text='List of fields to hide for this combination.', max_length=200)),
                ('offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offering_request.Offering')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offering_request.Platform')),
            ],
        ),
        migrations.AddField(
            model_name='offering_request',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offering_request.Platform'),
        ),
        migrations.AlterUniqueTogether(
            name='platformoffering',
            unique_together=set([('platform', 'offering')]),
        ),
    ]
