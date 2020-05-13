from django.urls import path
from .views import index , addCity ,deleteCity
from django.views.generic import RedirectView

urlpatterns = [
    path('weView/', index),
    path('', RedirectView.as_view(url="weView/")),
    path('weAdd/', addCity),
    path('weDelete/<int:c_id>', deleteCity),
]
