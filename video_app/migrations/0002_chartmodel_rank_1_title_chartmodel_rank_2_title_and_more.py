# Generated by Django 4.1.4 on 2022-12-21 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartmodel',
            name='rank_1_title',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='1위 제목'),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='rank_2_title',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='2위 제목'),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='rank_3_title',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='3위 제목'),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='rank_4_title',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='4위 제목'),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='rank_5_title',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='5위 제목'),
        ),
    ]
