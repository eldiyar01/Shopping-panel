# Generated by Django 3.1.4 on 2021-01-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purchase', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('size', models.IntegerField()),
                ('type', models.CharField(choices=[('GR', 'gramme'), ('ML', 'milligrams'), ('PCS', 'peaces'), ('LN', 'length')], default='GR', max_length=3)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date', to='panel.date')),
            ],
        ),
    ]
