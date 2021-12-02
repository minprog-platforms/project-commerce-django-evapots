from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from django.contrib import messages
from .models import User, Listings, Bids, Comments, CATEGORIES


def all_categories():
    categories = list(CATEGORIES)
    categories_list = []
    for item in categories:
        categories_list.append(list(item)[0])
    return categories_list

def count_watchlist():
    count = 0
    listings = Listings.objects.all()
    for listing in listings:
        if listing.watchlist == True:
            count = count + 1
    return count

class ListingForm(ModelForm):
  class Meta:
    model = Listings
    fields = ['listing_title', 'current_price', 'description', 'category', 'image']


class BidForm(ModelForm):
  class Meta:
    model = Bids
    fields = ["new_bid"]

class CommentForm(ModelForm):
  class Meta:
    model = Comments
    fields = ["comment_title", "comment"]

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all(), 
        "tot_watchlist": count_watchlist()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password.",
                "tot_watchlist": count_watchlist()
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def category_index(request, category):
     return render(request, "auctions/category_index.html", {
        "category": category,
        "listings": Listings.objects.all(),
        "tot_watchlist": count_watchlist()
    })


def category(request):
     return render(request, "auctions/category.html", {
        "categories": all_categories(),
        "tot_watchlist": count_watchlist()
    })


def listing_page(request, listing):

    indiv_listing = Listings.objects.get(listing_title=listing)
    user = User.objects.get(username=request.user)

    if request.method == "POST":
        if 'button_bid' in request.POST:
            price = float(request.POST["new_bid"])
            bids = indiv_listing.bids.all()
            if price <= indiv_listing.current_price:
                messages.error(request, "Error! Invalid bid amount!")
                return HttpResponseRedirect(reverse("listing_page", args=[listing]))
            form = BidForm(request.POST)
            if form.is_valid():
                bid = form.save(commit=False)
                bid.user = User.objects.get(username=request.user)
                bid.save()
                indiv_listing.bids.add(bid)
                indiv_listing.current_price = price
                indiv_listing.save()
                return HttpResponseRedirect(reverse("listing_page", args=[listing]))
            else:
                return render(request, "auctions/listing_page.html", {
                    "listing": indiv_listing, 
                    "bid_form": BidForm(),
                    "comment_form": CommentForm(),
                    "user": user,
                    "tot_watchlist": count_watchlist()
                })
        elif 'button_comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = User.objects.get(username=request.user)
                comment.save()
                indiv_listing.comments.add(comment)
                indiv_listing.save()
                return HttpResponseRedirect(reverse("listing_page", args=[listing]))
        elif 'button_watchlist' in request.POST:
            if indiv_listing.watchlist == False:
                indiv_listing.watchlist = True
            elif indiv_listing.watchlist == True:
                indiv_listing.watchlist = False
            indiv_listing.save()
            return HttpResponseRedirect(reverse("listing_page", args=[listing]))
    else:
        return render(request, "auctions/listing_page.html", {
                "listing": indiv_listing, 
                "bid_form": BidForm(),
                "comment_form": CommentForm(),
                "user": user,
                "tot_watchlist": count_watchlist()
            })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
    
def create(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Succes! Your listing has been saved!")
            listing = form.save(commit=False)
            listing.owner = user
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                "form": form,
                "tot_watchlist": count_watchlist()
            })
    else:
        return render(request, "auctions/create.html", {
            "form": ListingForm(),
            "tot_watchlist": count_watchlist()
        })

def watchlist(request):
     return render(request, "auctions/watchlist.html", {
        "listings": Listings.objects.all(),
        "tot_watchlist": count_watchlist()
    })



