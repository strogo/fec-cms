# Generated by Django 2.2.13 on 2020-09-30 18:19

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0109_auto_20200219_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompage',
            name='conditional_js',
            field=models.CharField(blank=True, choices=[('statistical_summary.js', 'statistical-summary')], help_text='Choose a JS script to add only to this page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_group',
            field=models.CharField(blank=True, choices=[('Press Office', 'Press authors'), ('Information Division', 'Information Division authors')], help_text='Not required: Only choose this if you want this author to show up as part an official author group', max_length=255),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='related_pages',
            field=wagtail.core.fields.StreamField([('related_pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock())), ('external_page', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
