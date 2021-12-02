from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category", views.category, name="category"),
    path("<str:category>", views.category_index, name="category_index"),
    path("<str:listing>", views.listing_page, name="listing_page"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create")
]
