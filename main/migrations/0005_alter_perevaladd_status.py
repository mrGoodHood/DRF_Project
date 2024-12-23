from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('main', '0004_alter_perevaladd_status_alter_perevaladd_title'),
    ]
    operations = [
        migrations.AlterField(
            model_name='perevaladd',
            name='status',
            field=models.CharField(choices=[('new', 'новый'), ('pending', 'модератор взял в работу'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default='new', max_length=10),
        ),
    ]