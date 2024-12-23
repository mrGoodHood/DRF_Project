from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='perevaluser',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='perevaluser',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.perevaladd'),
        ),
        migrations.AddField(
            model_name='perevalimages',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.perevaladd'),
        ),
        migrations.AddField(
            model_name='perevaladd',
            name='id_coards',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.coards'),
        ),
        migrations.AddField(
            model_name='perevaladd',
            name='users',
            field=models.ManyToManyField(through='main.PerevalUser', to=settings.AUTH_USER_MODEL),
        ),
    ]