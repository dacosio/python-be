from django.urls import path
from django.views.generic import TemplateView

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]