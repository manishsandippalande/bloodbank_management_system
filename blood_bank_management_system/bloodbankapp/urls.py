from django.urls import path
from bloodbankapp import views
urlpatterns = [
    path('', views.home),
    path('patients', views.addpatient),
    path('donors', views.adddonor),
    path('dashboard', views.dashboard),
    path('deletepatient/<pid>', views.deletepatient),
    path('deletedonor/<did>', views.deletedonor),
    path('updatepatient/<pid>', views.updatepatient),
    path('updatepatient_method/<pid>', views.updatepatient_method),
    path('updatedonor/<did>', views.updatedonor),
    path('updatedonor_method/<did>', views.updatedonor_method),
    path('about', views.aboutpage)

]