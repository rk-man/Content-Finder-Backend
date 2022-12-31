from django.urls import path, include

from base.views.userviews import updateUserProfile, getAllProfiles, getProfile, getOtherProfiles, searchUsers

urlpatterns = [
    path("search/<str:query>/", searchUsers, name="search-users"),
    path("other-profiles/", getOtherProfiles, name="get-other-profile"),
    path("content/", include("base.urls.contentUrls")),
    path("<str:pk>/update/", updateUserProfile, name="update-user-profile"),
    path("", getAllProfiles, name="get-all-profiles"),
    path("<str:pk>/", getProfile, name="get-profile")
]
