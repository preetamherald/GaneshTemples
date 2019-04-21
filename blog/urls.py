from django.conf.urls import url
from django.urls import path
from blog import views

urlpatterns=[
    path('',views.home,name='home'),
    url(r'^stories/$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView,name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
    url(r'^like/(?P<pk>\d+)$', views.like_post, name ='like_post'),
    url(r'^temples/$',views.TempleListView.as_view(),name='temple_list'),
    path('assets/images/main-800x600.jpg/',views.my_image1),
    path('assets/images/background4.jpg',views.my_image2),
]