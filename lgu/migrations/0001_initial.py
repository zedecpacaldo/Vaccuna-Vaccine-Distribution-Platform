# Generated by Django 3.1.6 on 2021-02-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalGovernmentUnit',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.user')),
                ('name', models.CharField(max_length=50)),
                ('registrant_map', models.FileField(blank=True, null=True, upload_to='static/maps/')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('daily_capacity', models.IntegerField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.addressfield')),
                ('lgu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccination_sites', to='lgu.localgovernmentunit')),
            ],
        ),
        migrations.CreateModel(
            name='PriorityLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.addressfield')),
                ('lgu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priority_locations', to='lgu.localgovernmentunit')),
            ],
        ),
    ]
