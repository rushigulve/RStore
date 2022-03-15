from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='shopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('productView/<int:myid>',views.productView,name='ProductView'),
    path('tracker/',views.tracker,name='Tracker'),
    path('search/',views.search,name='Search'),
    path('checkout/',views.checkout,name='Checkout '),
]