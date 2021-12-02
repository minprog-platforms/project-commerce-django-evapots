# Generated by Django 3.2.9 on 2021-12-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20211202_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='watchlists',
            field=models.ManyToManyField(blank=True, related_name='bids', to='auctions.Watchlists'),
        ),
        migrations.AddField(
            model_name='watchlists',
            name='listing_title',
            field=models.CharField(default='enter listing', max_length=64),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='listings',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='listings',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
    ]
