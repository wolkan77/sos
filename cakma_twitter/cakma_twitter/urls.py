"""civilti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
# Kendi çıkış yap view'ımı yazmak yerine bunu da kullanabilirim
# from django.contrib.auth.views import logout_then_login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from tweets.views import Karsilama, Akis, KayitOl, GirisYap, Profil, CikisYap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Karsilama.as_view(), name="karsilama"),
    path('akis/', login_required(Akis.as_view(), login_url="/giris_yap/"), name="akis"),
    path('kayit_ol/', KayitOl.as_view(), name="kayit"),
    path('giris_yap/', GirisYap.as_view(), name="giris"),
    path('profil/', Profil.as_view(), name="profilim"),
    path('profil/<slug:username>/', Profil.as_view(), name="profil"),
    path('cikis_yap/', CikisYap.as_view(), name="cikis"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
