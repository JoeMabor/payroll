# Generated by Django 4.0.4 on 2022-06-06 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_deduction_is_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allowance',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='deduction',
            name='employee',
        ),
        migrations.CreateModel(
            name='EmployeeDeduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, max_length=250, null=True)),
                ('deduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.deduction')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAllowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField(blank=True, max_length=250, null=True)),
                ('allowance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.allowance')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
            options={
                'unique_together': {('employee', 'allowance')},
            },
        ),
    ]