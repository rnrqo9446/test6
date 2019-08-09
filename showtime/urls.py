"""showtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import show.views, accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showtime/home/',show.views.home, name='home'),
    path('post/<int:post_id>/', show.views.detail, name='detail'),
    path('showtime/exhibition/', show.views.exhibition, name="exhibition"),
    path('showtime/musical/', show.views.musical, name='musical'),
    path('showtime/concert/', show.views.concert, name='concert'),
    path('showtime/classic/', show.views.musical, name='classic'),
    path('post/<int:post_id>/comment/', show.views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete', show.views.comment_delete, name='comment_delete'),
    path('comment/<int:comment_id>/like/', show.views.post_like, name='post_like'),


    
    # path('home/',show.views.home, name='home'),
    # path('musical/home/',show.views.musical_home,name='musical_home'),
    # path('musical/home/<int:musical_id>/',show.views.musical_detail,name='musical_detail'),
    # path('exhibition/home/',show.views.exhibition_home,name='exhibition_home'),
    # path('exhibition/home/<int:exhibition_id>/',show.views.exhibition_detail,name='exhibition_detail'),
    # path('classic/home/',show.views.classic_home,name='classic_home'),
    # path('classic/home/<int:classic_id>/',show.views.classic_detail,name='classic_detail'),
    # path('concert/home/',show.views.concert_home,name='concert_home'),
    # path('concert/home/<int:concert_id>/',show.views.concert_detail,name='concert_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
