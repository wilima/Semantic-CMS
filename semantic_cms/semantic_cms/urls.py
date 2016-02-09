"""semantic_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from semantic import views as semantic_views
from article import views as article_views
# from article.admin import my_admin

router = routers.DefaultRouter()
router.register(r'semantic_node', semantic_views.SemanticNodeViewSet)
router.register(r'semantic_edge', semantic_views.SemanticEdgeViewSet)
router.register(r'articles', article_views.ArticleViewSet)
router.register(r'articles_edge', article_views.ArticleEdgeViewSet)

urlpatterns = [
    url(r'^semantic_admin/', include('semantic_admin.urls', namespace="semantic_admin")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^myadmin/', include(my_admin.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^keywords/', include('keywords.urls')),
    url(r'^api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
