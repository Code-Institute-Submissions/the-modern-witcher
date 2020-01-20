# Generated by Django 2.2 on 2020-01-20 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_item_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=25)),
                ('rating', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=1)),
                ('review_text', models.TextField(blank=True, max_length=250)),
                ('reviewed_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]