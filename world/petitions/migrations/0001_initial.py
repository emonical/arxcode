# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-12 03:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dominion", "0001_squashed_dominion"),
    ]

    operations = [
        migrations.CreateModel(
            name="BrokeredSale",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sale_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Action Points"),
                            (1, "Economic Resources"),
                            (2, "Social Resources"),
                            (3, "Military Resources"),
                            (4, "Crafting Materials"),
                        ],
                        default=0,
                    ),
                ),
                ("amount", models.PositiveIntegerField(default=0)),
                ("price", models.PositiveIntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PurchasedAmount",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(default=0)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchased_amounts",
                        to="dominion.PlayerOrNpc",
                    ),
                ),
                (
                    "deal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchased_amounts",
                        to="petitions.BrokeredSale",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="brokeredsale",
            name="buyers",
            field=models.ManyToManyField(
                related_name="brokered_purchases",
                through="petitions.PurchasedAmount",
                to="dominion.PlayerOrNpc",
            ),
        ),
        migrations.AddField(
            model_name="brokeredsale",
            name="crafting_material_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dominion.CraftingMaterialType",
            ),
        ),
        migrations.AddField(
            model_name="brokeredsale",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="brokered_sales",
                to="dominion.PlayerOrNpc",
            ),
        ),
    ]
