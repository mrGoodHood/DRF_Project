from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_activitiestypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perevalareas',
            name='id_parent',
        ),
        migrations.AddField(
            model_name='perevalareas',
            name='pereval',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='main.perevaladd'),
            preserve_default=False,
        ),
    ]