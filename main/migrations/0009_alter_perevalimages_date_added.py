from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_id_user_perevaluser_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevalimages',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]