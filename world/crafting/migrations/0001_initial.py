# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-28 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import server.utils.arx_utils

tags_to_delete = [
    "display_by_line",
    "displayable",
]
attributes_to_delete = [
    "recipe",
    "materials",
    "adorns",
    "quality_level",
    "crafted_by",
    # for weapons
    "is_wieldable",
    "armor_class",  # note - filter by typeclass when removing that
    "stealth",
    "sense_difficulty",
    "attack_skill",
    "attack_stat",
    "damage_stat",
    "damage_bonus",
    "attack_type",
    "can_be_parried",
    "can_be_blocked",
    "can_be_dodged",
    "can_be_countered",
    "can_parry",
    "can_riposte",
    "difficulty_mod",
    "ignore_crafted",
    "currently_wielded",
    # wearable
    "currently_worn",
    "slot_limit",
    "penalty",
    "worn_time",  # if we come up with better way for displaying order
    # containers
    "container",
    "max_volume",
    "volume",

]


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dominion', '0045_auto_20190415_2022'),
        ('objects', '0009_remove_objectdb_db_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adornment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adornments', to='objects.ObjectDB')),
            ],
            options={
                'verbose_name_plural': 'Adornments',
                'default_related_name': 'object_materials',
            },
        ),
        migrations.CreateModel(
            name='CraftingMaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=80)),
                ('desc', models.TextField(blank=True, null=True)),
                ('value', models.PositiveIntegerField(blank=0, default=0)),
                ('category', models.CharField(blank=True, db_index=True, max_length=80, null=True)),
                ('acquisition_modifiers', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CraftingRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('difficulty', models.PositiveSmallIntegerField(blank=0, default=0)),
                ('additional_cost', models.PositiveIntegerField(blank=0, default=0)),
                ('ability', models.CharField(blank=True, db_index=True, max_length=80)),
                ('skill', models.CharField(blank=True, db_index=True, max_length=80)),
                ('type', models.CharField(blank=True, max_length=80)),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('allow_adorn', models.BooleanField(default=True)),
                ('baseval', models.IntegerField(default=0, verbose_name='Value used for things like weapon damage, armor rating, etc.')),
                ('known_by', models.ManyToManyField(blank=True, related_name='recipes', to='dominion.AssetOwner')),
            ],
            options={
                'abstract': False,
            },
            bases=(server.utils.arx_utils.CachedPropertiesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CraftingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_quality', models.SmallIntegerField(default=5, verbose_name='Quality without other modifiers')),
                ('refining_progress', models.SmallIntegerField(default=0)),
                ('damage', models.SmallIntegerField(default=0, verbose_name='Current damage, which affects quality')),
                ('object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='crafting_record', to='objects.ObjectDB')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crafting_records', to='crafting.CraftingRecipe')),
            ],
        ),
        migrations.CreateModel(
            name='OwnedMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='dominion.AssetOwner')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='crafting.CraftingMaterialType')),
            ],
            options={
                'verbose_name_plural': 'Owned Materials',
                'default_related_name': 'materials',
            },
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='required_materials', to='crafting.CraftingRecipe')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='required_materials', to='crafting.CraftingMaterialType')),
            ],
            options={
                'verbose_name_plural': 'Recipe Materials Requirements',
                'default_related_name': 'required_materials',
            },
        ),
        migrations.CreateModel(
            name='WeaponStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_skill', models.CharField(blank=True, choices=[('small wpn', 'Small Weapons'), ('medium wpn', 'Medium Weapons'), ('huge wpn', 'Huge Weapons'), ('archery', 'Archery')], default='medium wpn', max_length=80)),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crafting.CraftingRecipe')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WearableStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(blank=True, max_length=80)),
                ('slot_volume', models.PositiveSmallIntegerField(default=0, verbose_name='How much space we take up. 100 is all of it.')),
                ('fashion_mult', models.PositiveIntegerField(default=0, verbose_name='Percentage multiplier when used for fashion')),
                ('penalty', models.SmallIntegerField(default=0, verbose_name='How much the armor impedes movement')),
                ('resilience', models.SmallIntegerField(default=0, verbose_name='How easy the armor is to penetrate')),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crafting.CraftingRecipe')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='adornment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_materials', to='crafting.CraftingMaterialType'),
        ),
    ]
