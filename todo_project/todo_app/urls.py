from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, TagViewSet

router = DefaultRouter()
router.register(r'todo-items', TodoItemViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)), # API endpoints
    path('', TemplateView.as_view(template_name="home.html"), name='index'),  # Root URL
    
]

