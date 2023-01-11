from django.urls import path, re_path
from api import views
from rest_framework.routers import SimpleRouter
from api.views import BookModelViewSet

router = SimpleRouter()
router.register("book", BookModelViewSet, basename="book")
urlpatterns = [
                  # re_path('^$', views.Test.as_view()),
              ] + router.urls
