# Generated by Django 4.0.2 on 2022-03-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pp_cdn_url',
            field=models.CharField(default='', max_length=350, unique=True),
            preserve_default=False,
        ),
    ]
