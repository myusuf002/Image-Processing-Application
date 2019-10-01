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
    path('image/view/<id>/cut/<left>/<top>/<right>/<bottom>/<x>/<y>', views.viewCutImage, name ="cut"),
    path('image/view/<id>/crop/<left>/<top>/<right>/<bottom>', views.viewCropImage, name ="crop"),
    path('image/view/<id>/rgb', views.viewRGBImage, name ="rgb"),
    path('image/view/<id>/hsv', views.viewHSVImage, name ="hsv"),
    path('image/view/<id>/gray', views.viewGrayImage, name ="gray"),
    path('image/view/<id>/histogram', views.viewHistogramImage, name ="histogram"),
]
