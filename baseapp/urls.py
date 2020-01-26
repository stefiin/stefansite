"""thesiscode URL Configuration

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
from django.urls import path
from ui.views import home, ibm, atomic, csip, soccer, centivizer, mentor, app, raven, etec, laneway, snowboard, taxi, finance, papers
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('ibm/', ibm, name='ibm'),
    path('atomic/', atomic, name='atomic'),
    path('csip/', csip, name='csip'),
    path('soccer/', soccer, name='soccer'),
    path('centivizer/', centivizer, name='centivizer'),
    path('mentor/', mentor, name='mentor'),
    path('app/', app, name='app'),
    path('raven/', raven, name='raven'),
    path('etec/', etec, name='etec'),
    path('laneway/', laneway, name='laneway'),
    path('snowboard/', snowboard, name='snowboard'),
    path('taxi/', taxi, name='taxi'),
    path('finance/', finance, name='finance'),
    path('papers/', papers, name='papers'),
]
