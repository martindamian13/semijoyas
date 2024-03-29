from django.urls import path
from . import views

urlpatterns = [
    # Espacio vacio para la base
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('product/',views.product, name="product"),
    path('contact/',views.contact, name="contact"),
    path('howto/',views.howto, name="howtobuy"),
    path("product/<int:product_id>", views.detail, name="detail"),
    path("product/<str:categoria>", views.category, name="category"),

    path('update_item', views.updateItem, name="update_item"),
]
