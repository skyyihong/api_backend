from django.urls import path, re_path
from api import views
from rest_framework.routers import SimpleRouter
from api.views import BookModelViewSet1, BookModelViewSet2, BookModelViewSet3, BookModelViewSet4, BookModelViewSet5

router = SimpleRouter()
router.register("book1", BookModelViewSet1, basename="book1")
router.register("book2", BookModelViewSet2, basename="book2")
router.register("book3", BookModelViewSet3, basename="book3")
router.register("book4", BookModelViewSet4, basename="book4")
router.register("book5", BookModelViewSet5, basename="book5")
urlpatterns = [
                  # re_path('^$', views.Test.as_view()),
              ] + router.urls
