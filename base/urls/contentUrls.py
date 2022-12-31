from django.urls import path
from base.views.contentViews import getAllContent, getContent, createContent, getUserContent, updateContent, getOtherUsersContent, addLikeToContent, getUserLikedContent, getTrendingContent, deleteContent, getSearchResults

urlpatterns = [
    path("search/<str:query>/", getSearchResults),
    path("<str:pk>/delete/", deleteContent, name="delete-content"),
    path("trending/", getTrendingContent, name="get-trending-content"),
    path("user-liked/", getUserLikedContent, name="user-liked-content"),
    path("<str:pk>/like/", addLikeToContent,
         name="add-or-remove-like-to-content"),
    path("other-content/", getOtherUsersContent,
         name="get-other-users-content"),
    path("", getAllContent, name="get-all-content"),
    path("<str:pk>/update/", updateContent, name="update-content"),
    path("create/", createContent, name="create-content"),
    path("<str:pk>/", getContent, name="get-content"),
    path("<str:pk>/user-content/", getUserContent, name="get-user-content")

]
