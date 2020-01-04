from.import views

from django.urls import path

from django.conf import settings
from django.urls import include
from django.conf.urls.static import static


urlpatterns  = [
    path('',views.PostList.as_view(),name ="home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
    path("index",views.upload_file,name="learndjango"),
    path("displays",views.display,name = "display"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)