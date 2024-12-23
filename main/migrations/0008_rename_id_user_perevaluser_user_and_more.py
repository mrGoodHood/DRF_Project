from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_perevalimages_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevaluser',
            old_name='id_user',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='perevalimages',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.perevaladd'),
        ),
    ]