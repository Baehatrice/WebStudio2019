# Generated by Django 2.2.2 on 2019-06-27 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impassionuser', '0004_impassionuser_cardinal_number'),
        ('board', '0002_auto_20190623_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impassionuser.Impassionuser')),
            ],
        ),
    ]
