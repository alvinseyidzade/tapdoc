"""tapdoc URL Configuration

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
from doctor import views
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.homepage, name='homepage'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctorpage2/', views.doctorpage2, name='doctorpage2'),
    path('doctorpage3/', views.doctorpage3, name='doctorpage3'),
    path('doctorpage4/', views.doctorpage4, name='doctorpage4'),
    path('doctorpage5/', views.doctorpage5, name='doctorpage5'),
    path('muracietform/', views.muracietform, name='muracietform'),
    path('muracietform2/', views.muracietform2, name='muracietform2'),
    path('doctors/', views.doctors, name='doctors'),
    path('logindoc/', views.logindoc, name='logindoc'),
    path('loginclinic/', views.loginclinic, name='loginclinic'),
    path('clinic/', views.clinic, name='clinic'),
    path('clinicpage2/', views.clinicpage2, name='clinicpage2'),
    path('clinicpage3/', views.clinicpage3, name='clinicpage3'),
    path('clinicpage4/', views.clinicpage4, name='clinicpage4'),
    path('clinicpage5/', views.clinicpage5, name='clinicpage5'),
    path('clinic/1/detail', views.clinicdetail, name='clinicdetail'),
    path('clinic/2/detail', views.clinicdetailistanbul, name='clinicdetailistanbul'),
    path('clinic/3/detail', views.clinicdetailvital, name='clinicdetailvital'),
    path('diaqnostika/', views.diaqnostika, name='diaqnostika'),
    path('diaqnostikapage2/', views.diaqnostikapage2, name='diaqnostikapage2'),
    path('diaqnostikapage3/', views.diaqnostikapage3, name='diaqnostikapage3'),
    path('diaqnostikapage4/', views.diaqnostikapage4, name='diaqnostikapage4'),
    path('diaqnostikapage5/', views.diaqnostikapage5, name='diaqnostikapage5'),
    path('xidmetler/', views.xidmetler, name='xidmetler'),
    path('doctor/<int:id>/detail', views.doctordetail, name='doctordetail'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('account/',accounts_views.account , name='account'),
    path('account/doctors',accounts_views.accountdoctors , name='accountdoctors'),
    path('account/settings',accounts_views.accountsettings , name='accountsettings'),
    path('account/settings/security',accounts_views.accountsettingssecurity , name='accountsettingssecurity'),
    path('account/settings/notifications',accounts_views.accountsettingsnotifications , name='accountsettingsnotifications'),
    path('account/settings/docpermissions',accounts_views.accountsettingsdocpermissions , name='accountsettingsdocpermissions'),
    path('account/settings/clinicpermissions',accounts_views.accountsettingsclinicpermissions , name='accountsettingsclinicpermissions'),
    path('account/settings/family',accounts_views.accountsettingsfamily , name='accountsettingsfamily'),
    path('account/settings/history',accounts_views.accountsettingshistory , name='accountsettingshistory'),
    path('account/settings/promotions',accounts_views.accountsettingspromotions , name='accountsettingspromotions'),
    path('account/clinics',accounts_views.accountclinics , name='accountcinics'),
    path('account/aptek',accounts_views.accountaptek , name='accountaptek'),
    path('account/doctordetail',accounts_views.accountdoctordetail , name='accountdoctordetail'),
    path('account/clinicdetail',accounts_views.accountclinicdetail , name='accountclinicdetail'),
    path('account/aptekdetail',accounts_views.accountaptekdetail , name='accountaptekdetail'),
    path('doctor/<int:id>/addtofavor', views.addtofavor, name='addtofavor'),
    path('doctor/<int:id>/removefavor', views.removefavor, name='removefavor'),
    path('doctor/<int:id>/doctoraddtofavor', views.doctoraddtofavor, name='doctoraddtofavor'),
    path('doctor/<int:id>/doctorremovefavor', views.doctorremovefavor, name='doctorremovefavor'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
