# Generated by Django 4.1.7 on 2023-02-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('email', models.TextField()),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
    ]
