from django.urls import path, include
from rest_framework import routers
from .views import GraphVisualizationViewSet, my_view

# Create a router and register the GraphVisualizationViewSet with it
router = routers.DefaultRouter()
router.register(r'graph-visualizations', GraphVisualizationViewSet)

urlpatterns = [
    # Your other URL patterns go here if any
    path('', include(router.urls)),
    path('index/', my_view, name="index"),
]
