# Generated by Django 3.2.9 on 2021-12-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listings_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Collectibles & Art', 'Collectibles & Art'), ('Fashion', 'Fashion'), ('Motors', 'Motors'), ('Sporting Good', 'Sporting Goods'), ('Health & Beauty', 'Health & Beauty'), ('Books, Movies & Music', 'Books, Movies & Music'), ('Business & Industrial', 'Business & Industrial'), ('Home & Garden', 'Home & Garden'), ('Others', 'Others')], default='Others', max_length=60),
        ),
    ]
