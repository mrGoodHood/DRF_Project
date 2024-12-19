from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('main', '0006_remove_perevaladd_coards_perevaladd_height_and_more'),
    ]
    operations = [
        migrations.AlterField(
            model_name='perevalimages',
            name='img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]