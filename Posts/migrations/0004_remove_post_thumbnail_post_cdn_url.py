# Generated by Django 4.0.2 on 2022-03-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_alter_post_content_alter_post_publish_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='post',
            name='cdn_url',
            field=models.CharField(default='', max_length=350),
            preserve_default=False,
        ),
    ]
