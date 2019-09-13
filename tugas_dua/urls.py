from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewIndex, name ="index"),
    path('image/view/<id>', views.viewImage, name ="image"),
    path('image/view/<id>/zoom-out', views.viewZoomOutImage, name ="zoom-out"),
    path('image/view/<id>/zoom-in', views.viewZoomInImage, name ="zoom-in"),
    path('image/view/<id>/flip-vertical', views.viewFlipVerticalImage, name ="flip-vertical"),
    path('image/view/<id>/flip-horizontal', views.viewFlipHorizontalImage, name ="flip-horizontal"),
    path('image/view/<id>/rotate/<degree>', views.viewRotateImage, name ="rotate"),
]