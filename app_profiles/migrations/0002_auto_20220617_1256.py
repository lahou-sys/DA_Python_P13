# Generated by Django 3.0 on 2022-06-17 12:56
from django.apps import apps
from django.db import migrations


def migrate_profiles(apps, schema_editor):
    try:
        OldModel = apps.get_model('oc_lettings_site', 'ProfileOld')
    except LookupError:
        return   
    NewProfile = apps.get_model('app_profiles', 'Profile')
    NewProfile.objects.bulk_create(
        NewProfile( user=old_object.user, favorite_city=old_object.favorite_city)
        for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('app_profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profiles)
    ]