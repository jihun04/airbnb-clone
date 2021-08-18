# Generated by Django 3.2.6 on 2021-08-14 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_room_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.roomtype'),
        ),
    ]