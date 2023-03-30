from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('tours/', views.TourApiView.as_view()),
    path('tours/<int:pk>/', views.SingleTourView.as_view()),
    path('tours/crud/<int:pk>/', views.SingleTourChange.as_view()),
    path('countries/', views.CountryApiView.as_view()),
    path('countries/<int:pk>/', views.SingleCountryView.as_view()),
    path('cart/<int:pk>/', views.ProfileApiView.as_view()),
    path('excursions/', views.ExcApiView.as_view()),
    path('excursions/<int:pk>/', views.SingleExcView.as_view()),
]