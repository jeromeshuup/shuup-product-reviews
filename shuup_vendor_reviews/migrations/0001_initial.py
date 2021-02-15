# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-18 21:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import shuup_product_reviews.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shuup", "0057_remove_product_stock_behavior"),
    ]

    operations = [
        migrations.CreateModel(
            name="VendorReview",
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
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="rating",
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="comment"),
                ),
                (
                    "would_recommend",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates whether you would recommend this product to a friend.",
                        verbose_name="Would recommend to a friend?",
                    ),
                ),
                (
                    "status",
                    enumfields.fields.EnumIntegerField(
                        db_index=True,
                        default=1,
                        enum=shuup_product_reviews.enums.ReviewStatus,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "reviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_reviews",
                        to="shuup.Contact",
                        verbose_name="reviewer",
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_reviews",
                        to="shuup.Shop",
                        verbose_name="shop",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_reviews",
                        to="shuup.Supplier",
                        verbose_name="supplier",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VendorReviewAggregation",
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
                    "rating",
                    models.DecimalField(
                        decimal_places=1, default=0, max_digits=2, verbose_name="rating"
                    ),
                ),
                (
                    "review_count",
                    models.PositiveIntegerField(default=0, verbose_name="review count"),
                ),
                (
                    "would_recommend",
                    models.PositiveIntegerField(
                        default=0, verbose_name="users would recommend"
                    ),
                ),
                (
                    "supplier",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_reviews_aggregation",
                        to="shuup.Supplier",
                        verbose_name="supplier",
                    ),
                ),
            ],
        ),
    ]
