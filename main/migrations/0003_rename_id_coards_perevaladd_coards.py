from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_initial'),
    ]
    operations = [
        migrations.RenameField(
            model_name='perevaladd',
            old_name='id_coards',
            new_name='coards',
        ),
    ]