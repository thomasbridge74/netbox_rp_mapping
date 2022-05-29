from django.urls import path
from . import views, models
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    # Entries for the RP itself
    path("rp/", views.RPListView.as_view(), name="staticrp_list"),
    path("rp/add/", views.RPEditView.as_view(), name="staticrp_add"),
    path("rp/<int:pk>/", views.RPView.as_view(), name="staticrp"),
    path("rp/<int:pk>/edit/", views.RPEditView.as_view(), name="staticrp_edit"),
    path("rp/<int:pk>/delete/", views.RPDeleteView.as_view(), name="staticrp_delete"),
    path(
        "rp/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="staticrp_changelog",
        kwargs={"model": models.StaticRP},
    ),
    # Entries for the groups belonging to the RP.
    path("rpgroup/", views.RPGroupListView.as_view(), name="rpgroupentry_list"),
    path("rpgroup/add/", views.RPGroupView.as_view(), name="rpgroupentry_add"),
    path("rpgroup/<int:pk>/", views.RPGroupListView.as_view(), name="rpgroupentry"),
    path(
        "rpgroup/<int:pk>/edit", views.RPGroupView.as_view(), name="rpgroupentry_edit"
    ),
    path(
        "rpgroup/<int:pk>/delete",
        views.RPGroupDeleteView.as_view(),
        name="rpgroupentry_delete",
    ),
    path(
        "rpgroup/<int:pk>/changelog",
        ObjectChangeLogView.as_view,
        name="rpgroupentry_changelog",
        kwargs={"model": models.RPGroupEntry},
    ),
)
