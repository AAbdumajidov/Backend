# Generated by Django 4.1.3 on 2022-12-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_create_date_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
