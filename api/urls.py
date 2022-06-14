from django.urls import path
from . import views

api="api/v1.0/market/company"
urlpatterns=[
    path(api+'/getall/', views.getData),
    path(api+'/info/<int:companycode>/', views.infoData, name='infoData'),
    path(api+'/register/', views.regData),
    path(api+'/delete/<int:companycode>', views.delData),
    path(api+'/stock/add/<int:companycode>', views.addData),
    path(api+'/stock/get/<int:companycode>/<startdate>/<endate>', views.delData)
]