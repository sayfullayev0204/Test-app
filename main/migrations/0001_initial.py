# Generated by Django 5.0 on 2024-02-14 03:58

import datetime
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, verbose_name='savol')),
                ('answer_a', models.CharField(max_length=250, verbose_name='a javob')),
                ('answer_b', models.CharField(max_length=250, verbose_name='b javob')),
                ('answer_c', models.CharField(max_length=250, verbose_name='c javob')),
                ('answer_d', models.CharField(max_length=250, verbose_name='d javob')),
                ('true_answer', models.CharField(max_length=250, verbose_name="to'g'ri javob")),
            ],
            options={
                'verbose_name': 'Savol',
                'verbose_name_plural': 'Savollar',
            },
        ),
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('true_answers', models.PositiveIntegerField(default=0)),
                ('percentage', models.PositiveBigIntegerField(default=0)),
                ('is_passed', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_answer', models.CharField(max_length=2)),
                ('true_answer', models.CharField(max_length=2)),
                ('is_true', models.BooleanField(default=False)),
                ('checktest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.checktest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='sarlavha')),
                ('maximum_attemps', models.PositiveIntegerField(verbose_name='maksimum harakatlar soni')),
                ('pass_percentage', models.PositiveIntegerField(default=60)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='boshlanish sanasi')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2024, 2, 16, 3, 58, 45, 975257, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='avtor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='kategoriya')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Testlar',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.test'),
        ),
        migrations.AddField(
            model_name='checktest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checktests', to='main.test'),
        ),
    ]
