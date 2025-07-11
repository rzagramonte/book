# Generated by Django 5.2.3 on 2025-06-30 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('genres', models.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='color_type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='archetype_rankings',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic_cloudinary_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='primary_archetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.archetype'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('cover_image_url', models.URLField()),
                ('cover_image_cloudinary_id', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('archetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.archetype')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group_pic_url', models.URLField(blank=True, null=True)),
                ('group_pic_cloudinary_id', models.CharField(blank=True, max_length=255, null=True)),
                ('archetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.archetype')),
                ('books_read', models.ManyToManyField(blank=True, related_name='read_in_groups', to='core.book')),
                ('current_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_in_groups', to='core.book')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='members', to='core.group'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('cloudinary_id', models.CharField(blank=True, max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_ai', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='ColorType',
        ),
    ]
