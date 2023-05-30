# Generated by Django 4.2 on 2023-04-25 09:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "department_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=100,
                        null=True,
                        verbose_name="部门名",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MyAdmin",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=32,
                        primary_key=True,
                        serialize=False,
                        verbose_name="管理员账号",
                    ),
                ),
                ("user_name", models.CharField(max_length=32, verbose_name="管理员名")),
                ("password", models.CharField(max_length=64, verbose_name="管理员密码")),
            ],
        ),
        migrations.CreateModel(
            name="PrettyNum",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mobile",
                    models.CharField(
                        blank=True, max_length=11, null=True, verbose_name="手机号"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="价格",
                    ),
                ),
                (
                    "level",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "一级"), (2, "二级别"), (3, "三级别")],
                        default=1,
                        null=True,
                        verbose_name="级别",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "占用"), (2, "未占用")],
                        default=2,
                        null=True,
                        verbose_name="状态",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "user_id",
                    models.CharField(
                        max_length=30,
                        primary_key=True,
                        serialize=False,
                        verbose_name="用户账号",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=30,
                        null=True,
                        verbose_name="姓名",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=64,
                        null=True,
                        verbose_name="密码",
                    ),
                ),
                (
                    "age",
                    models.IntegerField(
                        blank=True, default=18, null=True, verbose_name="年龄"
                    ),
                ),
                (
                    "account",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        null=True,
                        verbose_name="账户余额",
                    ),
                ),
                (
                    "creat_time",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(2023, 4, 25, 17, 27, 44, 916583),
                        null=True,
                        verbose_name="入职时间",
                    ),
                ),
                (
                    "gender",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "男"), (2, "女")],
                        null=True,
                        verbose_name="性别",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_set",
                        to="app01.department",
                        verbose_name="所属部门",
                    ),
                ),
            ],
        ),
    ]