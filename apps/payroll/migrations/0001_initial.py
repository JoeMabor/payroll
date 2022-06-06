# Generated by Django 4.0.4 on 2022-05-27 23:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('calendar', models.CharField(choices=[('MONTHLY', 'Monthly'), ('WEEKLY', 'Weekly'), ('BI_WEEKLY', 'Bi-Weekly')], default='MONTHLY', max_length=10)),
                ('begin_at', models.DateField(default=datetime.date(2022, 5, 6))),
                ('end_at', models.DateField(default=datetime.date(2022, 5, 31))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('NOT_PAID', 'Not Paid'), ('PAID', 'Paid')], default='NOT_PAID', max_length=50)),
                ('gross_pay', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('net_pay', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.payroll')),
                ('tax_bracket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.taxbracket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]