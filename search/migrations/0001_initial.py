# Generated by Django 3.0 on 2019-12-27 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=31, verbose_name='場所')),
                ('overall_count', models.IntegerField(verbose_name='全体の検索回数')),
                ('recent_count', models.IntegerField(verbose_name='最近の検索回数')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=15, verbose_name='場所')),
                ('keyword', models.CharField(max_length=31, verbose_name='検索ワード')),
                ('radius', models.IntegerField(verbose_name='検索半径')),
            ],
        ),
        migrations.CreateModel(
            name='YourLunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=31, verbose_name='お店')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stores', models.CharField(max_length=31, null=True, verbose_name='検索結果')),
                ('search', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='search.Search', verbose_name='検索')),
            ],
        ),
    ]