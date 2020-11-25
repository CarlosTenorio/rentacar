# Generated by Django 3.1.1 on 2020-11-23 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='Year',
            new_name='year',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_order', to='api.extenduser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_signed',
            field=models.DateTimeField(auto_now_add=True, verbose_name='When the order was made'),
        ),
    ]
