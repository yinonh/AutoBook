"""LibraryProject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from book_catalog import views as book_catalog_views
from django.conf.urls.static import static
from authentication import views as authentication_views
from homepage import views as homepage_views
from mepage import views as mepage_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.homepage, name='homepage'),
    path('Simple/', book_catalog_views.simple, name="simple"),

    #Book Catalog

    path('book_cataloge/', include('book_catalog.urls')),
    path('Contact/', book_catalog_views.contact, name="contact"),
    path('Filtered/', book_catalog_views.filteredbooks, name="filteredbooks"),


    #Authentication
    path('signup/student/', authentication_views.studentsignupuser, name="signupstudent"),
    path('signup/adult/', authentication_views.adultsignupuser, name="signupadult"),
    path('signup/', authentication_views.signupuser, name="signupuser"),
    path('logoutuser/', authentication_views.logoutuser, name="logoutuser"),
    path('loginU/', authentication_views.loginU, name="loginU"),




    #Me page
    path('Me/', include('mepage.urls')),
    # path('Me/Adult/', mepage_views.meadult, name="meadult"),
    # # path('Me/Adult/Favourites/', mepage_views.meadultfavourites, name="meadultfavourites"),
    # path('Me/Student/', mepage_views.mestudent, name="mestudent"),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
