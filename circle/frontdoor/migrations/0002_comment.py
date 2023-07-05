# Generated by Django 4.2.2 on 2023-07-05 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontdoor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontdoor.circle')),
            ],
        ),
    ]
