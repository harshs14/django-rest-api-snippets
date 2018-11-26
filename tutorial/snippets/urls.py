from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token


schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
    re_path(r'^api-token-auth/', obtain_jwt_token),
]
