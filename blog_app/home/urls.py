from django.urls import path
from .views import *


urlpatterns = [
    # User Authentication
    path('register/', view=register, name='register'),
    path('login/', view=user_login, name='login'),
    path('logout/', view=user_logout, name='logout'),

    # profile
    path('profile/', view=profile, name='profile'),
    path('edit_profile/', view=edit_user_profile, name='edit_user_profile'),
    path('user_profile/<int:uid>/', view=user_profile, name='user_profile'),

    # blogs
    path('', view=blogs, name="blogs"),
    path('blog/<str:slug>/', view=blog_detail, name="blog_details"),
    path('add_blog/', view=add_blog, name="add_blog"),
    path('edit_blog_post/<str:slug>/', view=UpdatePostView.as_view(), name="edit_blog_post"),
    path('delete_blog_post/<str:slug>/', view=delete_blog_post, name="delete_blog_post"),
    path('search/', view=search, name="search"),
]
