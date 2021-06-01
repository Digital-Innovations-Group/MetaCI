# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-05 21:19
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("notification", "0008_auto_20180603_2202"),
        ("notification", "0009_auto_20180605_1954"),
        ("notification", "0010_auto_20180605_2029"),
        ("notification", "0011_auto_20180605_2117"),
    ]

    dependencies = [
        ("plan", "0015_auto_20180314_2252"),
        ("notification", "0007_planrepositorynotification"),
        ("repository", "0004_remove_branch_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branchnotification",
            name="branch",
            field=models.ForeignKey(
                db_column="branch_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="repository.Branch",
                verbose_name="branch",
            ),
        ),
        migrations.AlterField(
            model_name="plannotification",
            name="plan",
            field=models.ForeignKey(
                db_column="plan_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="plan.Plan",
                verbose_name="plan",
            ),
        ),
        migrations.AlterField(
            model_name="planrepositorynotification",
            name="planrepository",
            field=models.ForeignKey(
                db_column="planrepository_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="plan.PlanRepository",
                verbose_name="planrepository",
            ),
        ),
        migrations.AlterField(
            model_name="repositorynotification",
            name="repo",
            field=models.ForeignKey(
                db_column="repo_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="repository.Repository",
                verbose_name="repo",
            ),
        ),
        migrations.RenameField(
            model_name="branchnotification", old_name="branch", new_name="target"
        ),
        migrations.RenameField(
            model_name="plannotification", old_name="plan", new_name="target"
        ),
        migrations.RenameField(
            model_name="planrepositorynotification",
            old_name="planrepository",
            new_name="target",
        ),
        migrations.RenameField(
            model_name="repositorynotification", old_name="repo", new_name="target"
        ),
    ]
