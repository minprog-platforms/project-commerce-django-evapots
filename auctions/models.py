from django.contrib.auth.models import AbstractUser
from django.db import models

## !! Note !! 
## each time change something run:
## (1) python3 manage.py makemigrations
## (2) python3 manage.py migrate

CATEGORIES = (
    ('Electronics', 'Electronics'),
    ('Collectibles & Art', 'Collectibles & Art'),
    ('Fashion', 'Fashion'),
    ('Motors', 'Motors'),
    ('Sporting Good', 'Sporting Goods'),
    ('Health & Beauty', 'Health & Beauty'),
    ('Books, Movies & Music', 'Books, Movies & Music'),
    ('Business & Industrial', 'Business & Industrial'),
    ('Home & Garden', 'Home & Garden'),
    ('Others', 'Others'),
)

# model: details about each user application
class User(AbstractUser):
    pass

# model: details about bids
class Bids(models.Model):
    new_bid = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, max_length=64, on_delete=models.CASCADE, related_name="user_bid")
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user} placed bid for ({self.new_bid})"

# model: details about comments on auction listings
class Comments(models.Model):
    comment_title = models.CharField(max_length=64)
    comment = models.TextField(max_length=300)
    user = models.ForeignKey(User, max_length=64, on_delete=models.CASCADE, related_name="user_comment")
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user} ({self.comment})"

# model: details about auction listings
class Listings(models.Model):
    listing_title = models.CharField(max_length=64)
    description = models.TextField(max_length=500, blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(blank=True, max_length=100)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    closed = models.BooleanField(default=False)
    category = models.CharField(max_length=60, choices=CATEGORIES, default=CATEGORIES[9][1])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")
    bids = models.ManyToManyField(Bids, blank=True, related_name="bids")
    comments = models.ManyToManyField(Comments, blank=True, related_name="comments")
    watchlist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.listing_title} is being sold by {self.owner}"
