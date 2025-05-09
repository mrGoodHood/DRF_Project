from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_remove_perevalareas_id_parent_perevalareas_pereval'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coards',
        ),
        migrations.AlterField(
            model_name='perevaluser',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_pereval', to='main.perevaladd'),
        ),
        migrations.AlterField(
            model_name='perevaluser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_users', to=settings.AUTH_USER_MODEL),
        ),
    ]