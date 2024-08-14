from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Contact,Service,Portfolio,Testimonial,BlogPost
from .serializers import (
    ContactSerializer, ServiceSerializer, PortfolioSerializer,
    TestimonialSerializer, BlogPostSerializer
    )

class ListCreateContactAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class RetrieveUpdateDestroyContactAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# ================================================================
class ListCreateServiceAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RetrieveUpdateDestroyServiceAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# ==================================================================
class ListCreatePortfolioAPIView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class RetrieveUpdateDestroyPortfolioAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


# ===================================================================
class ListCreateTestimonialAPIView(ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class RetrieveUpdateDestroyTestimonialAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


# ========================================================================
class ListCreateBlogPostAPIView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class RetrieveUpdateDestroyBlogPostAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

