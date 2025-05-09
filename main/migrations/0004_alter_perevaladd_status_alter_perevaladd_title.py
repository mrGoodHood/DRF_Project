from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_rename_id_coards_perevaladd_coards'),
    ]
    operations = [
        migrations.AlterField(
            model_name='perevaladd',
            name='status',
            field=models.CharField(choices=[('new', 'новый'), ('pending', 'модератор взял в работу'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default=('new', 'новый'), max_length=255),
        ),
        migrations.AlterField(
            model_name='perevaladd',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]