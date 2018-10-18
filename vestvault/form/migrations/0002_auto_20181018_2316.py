# Generated by Django 2.1.2 on 2018-10-18 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent_stake', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('token_name', models.CharField(max_length=150)),
                ('token_supply', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='holder',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Token'),
        ),
    ]