
from django.urls import path
import dataApp.views as views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('checkDb',views.checkDb,name='checkDb'),
]
