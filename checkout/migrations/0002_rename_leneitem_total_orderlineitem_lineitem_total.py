# Generated by Django 3.2.6 on 2021-09-16 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='leneitem_total',
            new_name='lineitem_total',
        ),
    ]
