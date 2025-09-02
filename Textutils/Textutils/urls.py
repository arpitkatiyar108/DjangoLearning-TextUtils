from django.contrib import admin
from django.urls import path
from . import views   # Import your app views

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),          # Homepage
    path('analyze/', views.analyze, name='analyze'),  # Analyze page
]
