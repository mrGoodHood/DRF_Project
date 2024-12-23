from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('main', '0005_alter_perevaladd_status'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='perevaladd',
            name='coards',
        ),
        migrations.AddField(
            model_name='perevaladd',
            name='height',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perevaladd',
            name='latitude',
            field=models.FloatField(default=2.23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perevaladd',
            name='longitude',
            field=models.FloatField(default=2.32),
            preserve_default=False,
        ),
    ]