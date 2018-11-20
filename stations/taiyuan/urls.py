from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('queue_fresh/',views.queue_fresh),
    path('queuelength/',views.queue_length),
    path('hall_fresh/',views.hall_fresh),
    path('stationhallcount/',views.stationhall_count),
    path('flow_yesterday/',views.flow_yesterday),
    path('flow_today/',views.flow_today),
    path('flowcount/',views.flow_count),
    path('buffer_before/',views.buffer_before),
    path('buffer_fresh/',views.buffer_fresh),
    path('bufferroom/',views.bufferroom_count),
]