from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='ActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('add_time', models.TimeField(auto_now_add=True)),
                ('beautyTitle', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=250)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField()),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'модератор взял в работу'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default=('new', 'новый'), max_length=10)),
                ('level_winter', models.CharField(max_length=255)),
                ('level_summer', models.CharField(max_length=255)),
                ('level_autumn', models.CharField(max_length=255)),
                ('level_spring', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parent', models.IntegerField()),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('img', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]