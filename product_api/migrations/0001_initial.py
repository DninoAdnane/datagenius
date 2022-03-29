# Generated by Django 3.2.12 on 2022-03-29 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeRemise', models.CharField(choices=[('Offre', 'Offre'), ('Reduction', 'Reduction')], default='Offre', max_length=10)),
                ('nbAchete', models.IntegerField(blank=True, null=True)),
                ('nbOffer', models.IntegerField(blank=True, null=True)),
                ('tauxRed', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rayon', models.CharField(choices=[('Alimentaire', 'Alimentaire'), ('Textile', 'Textile'), ('Informatique', 'Informatique'), ('Frais', 'Frais'), ('Boucherie', 'Boucherie')], default='Alimentaire', max_length=20)),
                ('remise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_api.remise')),
            ],
        ),
    ]
