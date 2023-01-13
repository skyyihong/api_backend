from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from book.models import Book
from book.serializer import BookModelSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import ListAPIView


# Create your views here.

class BookModelViewSet1(ModelViewSet):
    '''
        自定义限流demo
    '''
    throttle_classes = [ScopedRateThrottle]  # 指定自定义scope的限流类
    throttle_scope = "test"  # 必须填写自定义的scope值
    authentication_classes = []
    permission_classes = []
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookModelViewSet2(ModelViewSet):
    # 认证和权限的demo
    authentication_classes = [JSONWebTokenAuthentication, ]  # 字段jwt的认证类来进行认证
    permission_classes = [AllowAny, ]  # jw认证,需要配合权限类才能工作
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookModelViewSet3(ModelViewSet):
    # 过滤的demo
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [AllowAny, ]
    filter_backends = (DjangoFilterBackend,)  # 局部配置过滤器
    filterset_fields = ("price", "stock", "sold")  # 允许进行过滤的字段

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


from rest_framework.filters import OrderingFilter


class BookModelViewSet4(ModelViewSet):
    # 排序的demo    http://127.0.0.1/api/book/ordering=-id 以id进行降序排序
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [AllowAny, ]
    filter_backends = (OrderingFilter,)  # 局部配置过滤器
    order_fileds = ['id', 'name', "price", "stock", "sold"]
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class MyPageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"  # 前端传的查询字符串中代表每一页条目的变量名称
    page_query_param = "page"  # 前端传的查询字符串中代表第几页的变量名称
    max_page_size = 4  # 每页最大的条目数,即便前端传过来的值大于max_page_size,也以max_page_size的值显示
    page_size = 3  # 默认的每页的条目数


class MyPageNumberPagination(LimitOffsetPagination):
    default_limit = 3  # 默认的每页的条目数
    limit_query_param = 'limit'  # 前端传的查询字符串中代表每一页条目的变量名称
    offset_query_param = 'offset'  # 前端传的查询字符串中代表第几页的变量名称
    max_limit = 10  # 默认的每页的条目数


class BookModelViewSet5(ModelViewSet):
    serializer_class = BookModelSerializer
    # 分页的demo    http://127.0.0.1/api/book/?size=5&page=2 显示第二页并且每页显示5条数据
    authentication_classes = []
    permission_classes = []
    # pagination_class = PageNumberPagination
    pagination_class = MyPageNumberPagination
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):
        res = super().list(self, request, *args, **kwargs)
        1 / 0
        return res
