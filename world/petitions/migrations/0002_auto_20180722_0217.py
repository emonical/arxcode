# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-22 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("petitions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Petition",
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
                ("closed", models.BooleanField(default=False)),
                (
                    "topic",
                    models.CharField(
                        max_length=120, verbose_name="Short summary of the petition"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Description of the petition."),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PetitionParticipation",
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
                ("is_owner", models.BooleanField(default=False)),
                ("signed_up", models.BooleanField(default=False)),
                ("unread_posts", models.BooleanField(default=False)),
                (
                    "dompc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dominion.PlayerOrNpc",
                    ),
                ),
                (
                    "petition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="petitions.Petition",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PetitionPost",
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
                ("in_character", models.BooleanField(default=True)),
                ("text", models.TextField(blank=True)),
                (
                    "dompc",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dominion.PlayerOrNpc",
                    ),
                ),
                (
                    "petition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="petitions.Petition",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="brokeredsale",
            name="crafting_material_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dominion.CraftingMaterialType",
            ),
        ),
        migrations.AddField(
            model_name="petition",
            name="dompcs",
            field=models.ManyToManyField(
                related_name="petitions",
                through="petitions.PetitionParticipation",
                to="dominion.PlayerOrNpc",
            ),
        ),
        migrations.AddField(
            model_name="petition",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="petitions",
                to="dominion.Organization",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="petitionparticipation",
            unique_together=set([("petition", "dompc")]),
        ),
    ]
