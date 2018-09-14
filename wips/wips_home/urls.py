from django.urls import path
from django.conf.urls import url
from wips_home import views

urlpatterns = [
	path('', views.base, name='base'),
	#path('', views.block_list, name='block_list'),
	url(r'^post/(?P<pk>\d+)/$', views.block_list, name='block_list'),
	#path('post/<int:pk>', views.block_list, name='block_list'),
	#path('post/<int:pk>', views.block_list_post, name='block_list_post'),

	]