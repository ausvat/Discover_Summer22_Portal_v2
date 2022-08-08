from django.urls import path

from portal.apps.projects.views import project_create, project_detail, project_edit, project_list, project_members, \
    project_owners

urlpatterns = [
    path('', project_list, name='project_list'),
    path('create', project_create, name='project_create'),
    path('<int:project_id>', project_detail, name='project_detail'),
    path('<int:project_id>/edit', project_edit, name='project_edit'),
    path('<int:project_id>/members', project_members, name='project_members'),
    path('<int:project_id>/owners', project_owners, name='project_owners'),
]
