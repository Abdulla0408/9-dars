from rest_framework.serializers import ModelSerializer
from landing.models import Service, Portfolio, Testimonial, BlogPost, Contact


class ServiceSerializers(ModelSerializer):
    class Meta:
        models = Service
        fields = '__all__'


class PortfolioSerializers(ModelSerializer):
    class Meta:
        models = Portfolio
        fields = '__all__'


class TestimonialSerializers(ModelSerializer):
    class Meta:
        models = Testimonial
        fields = '__all__'


class BlogPostSerializers(ModelSerializer):
    class Meta:
        models = BlogPost
        fields = '__all__'


class ContactSerializers(ModelSerializer):
    class Meta:
        models = Contact
        fields = '__all__'


