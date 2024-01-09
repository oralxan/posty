# Generated by Django 4.2 on 2024-01-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_options_post_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='brand',
            field=models.CharField(max_length=128, null=True, verbose_name='brands'),
        ),
        migrations.AddField(
            model_name='post',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='color',
            field=models.CharField(max_length=128, null=True, verbose_name='colors'),
        ),
        migrations.AddField(
            model_name='post',
            name='horse_power',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name='Название поста'),
        ),
    ]