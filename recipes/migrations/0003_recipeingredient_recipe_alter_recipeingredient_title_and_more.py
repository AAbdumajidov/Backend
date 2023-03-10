# Generated by Django 4.1.3 on 2023-01-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_tag_recipe_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='title',
            field=models.CharField(max_length=112),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.IntegerField(choices=[(0, 'Gr'), (1, 'Ml'), (2, 'Dona')]),
        ),
    ]
