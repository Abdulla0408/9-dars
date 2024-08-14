from django.urls import path
from .views import (
    ListCreateContactAPIView, RetrieveUpdateDestroyContactAPIView,
    ListCreateServiceAPIView, RetrieveUpdateDestroyServiceAPIView,
    ListCreatePortfolioAPIView, RetrieveUpdateDestroyPortfolioAPIView,
    ListCreateTestimonialAPIView, RetrieveUpdateDestroyTestimonialAPIView,
    ListCreateBlogPostAPIView, RetrieveUpdateDestroyBlogPostAPIView
    )

urlpatterns = [
    path('contact/list_or_create/', ListCreateContactAPIView.as_view(), name="list_create_contact"),
    path('contact/retrieve_or_update_or_destroy/<slug:slug>/', RetrieveUpdateDestroyContactAPIView.as_view(), name="read_update_delete_contact"),
 path('service/list_or_create/', ListCreateServiceAPIView.as_view(), name="list_create_service"),
    path('service/retrieve_or_update_or_destroy/<slug:slug>/', RetrieveUpdateDestroyServiceAPIView.as_view(), name="read_update_delete_service"),
 path('portfolio/list_or_create/', ListCreatePortfolioAPIView.as_view(), name="list_create_portfolio"),
    path('portfolio/retrieve_or_update_or_destroy/<slug:slug>/', RetrieveUpdateDestroyPortfolioAPIView.as_view(), name="read_update_delete_portfolio"),
 path('testimonial/list_or_create/', ListCreateTestimonialAPIView.as_view(), name="list_create_testimonial"),
    path('testimonial/retrieve_or_update_or_destroy/<slug:slug>/', RetrieveUpdateDestroyTestimonialAPIView.as_view(), name="read_update_delete_testimonial"),
 path('blogpost/list_or_create/', ListCreateBlogPostAPIView.as_view(), name="list_create_blogpost"),
    path('blogpost/retrieve_or_update_or_destroy/<slug:slug>/', RetrieveUpdateDestroyBlogPostAPIView.as_view(), name="read_update_delete_blogpost"),
]