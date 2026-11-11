from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.home),
    path("about/",views.about),
    path("products/<int:id>/",views.product_deatils),
    path("cheap/",views.cheap_products)
]
