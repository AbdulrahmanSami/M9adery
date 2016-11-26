# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0005_auto_20161031_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to=b'', verbose_name='\u0635\u0648\u0631\u0629 \u0627\u0644\u062a\u0635\u0646\u064a\u0641')),
            ],
        ),
        migrations.DeleteModel(
            name='BookCategories',
        ),
        migrations.AddField(
            model_name='block',
            name='description',
            field=models.TextField(blank=True, help_text='\u0627\u062e\u062a\u064a\u0627\u0631\u064a', verbose_name='\u0648\u0635\u0641 \u0627\u0644\u0628\u0644\u0648\u0643'),
        ),
        migrations.AlterField(
            model_name='block',
            name='cover',
            field=models.ImageField(default='http://riddim-donmagazine.com/wp-content/uploads/2015/12/Concrete-Block.jpg', upload_to=b'', verbose_name='\u0635\u0648\u0631\u0629 \u0627\u0644\u0628\u0644\u0648\u0643'),
        ),
    ]
