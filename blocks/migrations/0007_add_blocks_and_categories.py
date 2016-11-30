
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_blocks (apps, schema_editor):
    Block = apps.get_model('blocks','Block')
    if not Block.objects.exists():
        Block.objects.create(title='Foundation Block')
        Block.objects.create(title='Musculoskeletal Block')
        Block.objects.create(title='Respiratory Block')
        Block.objects.create(title='Hematology Block')
        Block.objects.create(title='Cardiovascular Block')
        Block.objects.create(title='Neurosciences Block')
        Block.objects.create(title='Endocrine Block')
        Block.objects.create(title='Urology and Renal Block')
        Block.objects.create(title='Gastroenterology Block')
        Block.objects.create(title='Oncology Block')
        Block.objects.create(title='EBM Block')
        Block.objects.create(title='Family Medicine Block',
                             is_clinical=True)
        Block.objects.create(title='Medicine Block',
                             is_clinical=True)
        Block.objects.create(title='Pediatric Block',
                             is_clinical=True
                             )
        Block.objects.create(title='Surgery Block',
                             is_clinical=True
                             )
        Block.objects.create(title='Obstetrics and Gynecology Block',
                             is_clinical=True
                             )
        Block.objects.create(title='Special Sense & Mental Health Block Book',
                             is_clinical=True
                             )
def add_categories(apps, schema_editor):
    Category = apps.get_model('blocks', 'Category')

    if not Category.objects.exists():
        Category.objects.create(name="anatomy")
        Category.objects.create(name="pathology")
        Category.objects.create(name="pharmacology")
        Category.objects.create(name="physiology")
        Category.objects.create(name="microbiology")
        Category.objects.create(name="immunology")

class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0006_auto_20161126_1245'),
    ]

    operations = [
       migrations.RunPython(
            add_blocks,
            add_categories
       )]