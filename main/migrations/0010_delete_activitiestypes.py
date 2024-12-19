from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_perevalimages_date_added'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivitiesTypes',
        ),
    ]