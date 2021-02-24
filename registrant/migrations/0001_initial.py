# Generated by Django 3.1.6 on 2021-02-23 18:46

import core.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lgu', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.user')),
                ('is_household', models.BooleanField(default=False)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.addressfield')),
                ('lgu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrants', to='lgu.localgovernmentunit')),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('had_covid', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('NS', 'Not sure')], default='NO', max_length=3)),
                ('live_with_covid', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('NS', 'Not sure')], default='NO', max_length=3)),
                ('registration_status', models.CharField(choices=[('G', 'Granted'), ('D', 'Denied'), ('W', 'Waitlisted'), ('P', 'Pending')], default='P', max_length=3)),
                ('vaccination_status', models.IntegerField(default=0)),
                ('first_vaccination_datetime', models.DateTimeField(null=True)),
                ('second_vaccination_datetime', models.DateTimeField(null=True)),
                ('is_frontline_worker', models.BooleanField(default=False)),
                ('is_frontline_personnel', models.BooleanField(default=False)),
                ('is_uniformed_personnel', models.BooleanField(default=False)),
                ('is_teacher_or_social_worker', models.BooleanField(default=False)),
                ('is_government_worker', models.BooleanField(default=False)),
                ('is_overseas_filipino_worker', models.BooleanField(default=False)),
                ('is_employed', models.BooleanField(default=False)),
                ('cancer', models.BooleanField(default=False)),
                ('chronic_kidney_disease', models.BooleanField(default=False)),
                ('pregnant', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('respiratory_illness', models.BooleanField(default=False)),
                ('cardiovascular_disease', models.BooleanField(default=False)),
                ('asthma', models.BooleanField(default=False)),
                ('high_blood_pressure', models.BooleanField(default=False)),
                ('organ_transplant', models.BooleanField(default=False)),
                ('kidney_disease', models.BooleanField(default=False)),
                ('sickle_cell_disease', models.BooleanField(default=False)),
                ('down_syndrome', models.BooleanField(default=False)),
                ('cerebrovascular_disease', models.BooleanField(default=False)),
                ('seizure_disorder', models.BooleanField(default=False)),
                ('blood_disease', models.BooleanField(default=False)),
                ('priority_group', models.IntegerField(choices=[(1, 'A1'), (2, 'A2'), (3, 'A3'), (4, 'A4'), (5, 'A5'), (6, 'B1'), (7, 'B2'), (8, 'B3'), (9, 'B4'), (10, 'B5'), (11, 'B6'), (12, 'C')], default=core.models.PriorityGroup['C'])),
                ('lgu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='individuals', to='lgu.localgovernmentunit')),
                ('registrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individuals', to='registrant.registrant')),
                ('vaccination_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='individuals', to='lgu.vaccinationsite')),
            ],
        ),
    ]
