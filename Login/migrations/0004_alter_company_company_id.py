# Generated by Django 4.1.7 on 2023-03-15 20:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_alter_company_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default=uuid.uuid4, max_length=40, unique=True),
        ),
    ]