"""sweet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, CategoriesListView, TagsListView, CommentCreateView, api_root

router = DefaultRouter()
router.register('products', ProductViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title='Shop API',
        default_version='v1',
        description='My shop\'s API'
    ), public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls')),
    path('api/v1/docs/', schema_view.with_ui()),
    path('', api_root),
    path('api/v1/categories/', CategoriesListView.as_view(), name='categories-list'),
    path('api/v1/tags/', TagsListView.as_view(), name='tags-list'),
    path('api/v1/comments/', CommentCreateView.as_view(), name='create-comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
