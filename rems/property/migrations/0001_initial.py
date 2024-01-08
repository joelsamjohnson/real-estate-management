# Generated by Django 4.2.9 on 2024-01-08 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('document_proofs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_type', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], max_length=10)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=3)),
                ('size', models.DecimalField(decimal_places=2, help_text='Size in square feet', max_digits=8)),
                ('image', models.ImageField(upload_to='property_images/')),
                ('property_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='property.property')),
            ],
        ),
    ]