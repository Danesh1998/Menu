# Generated by Django 4.2.7 on 2023-12-07 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='colony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colony_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_name', models.CharField(max_length=50, null=True)),
                ('colony', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.colony')),
            ],
        ),
        migrations.CreateModel(
            name='ward_noo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_no', models.IntegerField(null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.city')),
            ],
        ),
        migrations.CreateModel(
            name='taluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taluk_name', models.CharField(max_length=50, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.district')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.state'),
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.city')),
                ('colony', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.colony')),
                ('dist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.district')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.state')),
                ('taluk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.taluk')),
                ('ward_noo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.ward_noo')),
                ('water', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.water')),
            ],
        ),
        migrations.AddField(
            model_name='colony',
            name='ward_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.ward_noo'),
        ),
        migrations.AddField(
            model_name='city',
            name='taluk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='council.taluk'),
        ),
    ]
