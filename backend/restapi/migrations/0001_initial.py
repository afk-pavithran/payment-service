# Generated by Django 3.2 on 2021-04-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txnid', models.CharField(max_length=50)),
                ('mihpayid', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=30)),
                ('payment_source', models.CharField(max_length=50)),
            ],
        ),
    ]
