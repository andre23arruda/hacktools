# Generated by Django 3.1.1 on 2021-02-06 20:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date)),
                ('user', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('questions', models.TextField(default='', help_text='As perguntas devem começar com "-"')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('answered_at', models.DateField(auto_now_add=True)),
                ('answers', models.TextField(default='')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionario.question')),
            ],
        ),
    ]
