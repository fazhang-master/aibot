# Generated by Django 4.2.11 on 2024-04-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_id', models.IntegerField(verbose_name='上传者ID')),
                ('img', models.FileField(upload_to='', verbose_name='上传内容')),
                ('status', models.SmallIntegerField(choices=[(1, '学习中'), (2, '已学完')], verbose_name='状态')),
            ],
        ),
        migrations.AlterModelOptions(
            name='chathistory',
            options={},
        ),
    ]