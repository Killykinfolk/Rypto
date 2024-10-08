from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("crypto/", views.crypto, name="crypto"),
    path("crypto/<slug:slug>/", views.crypto_offer, name="offer"),
    path("contact/", views.contact, name="contact"),
]
