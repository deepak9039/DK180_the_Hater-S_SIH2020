from django.urls import path,include
from . import views
urlpatterns = [
    path("feed/",views.JobListView.as_view(),name="feed"),
    path('addjob/',views.addjob,name="addjob"),
    path("sport/",views.sport,name="sport"),
    # path("job_view/",views.job_view,name="job_view"),
    path("<int:pk>/",views.view_job ,name="job"),
    path("delete/<int:pk>/",views.delete_job ,name="delete_job"),
    path("update/<int:pk>/",views.update_job ,name="update_job"),
    path("apply/<int:pk>/",views.apply_job ,name="apply_job"),
    path('applied_job/',views.applied_job,name='applied_job'),
    path('company_application/',views.company_application,name='company_application'),

]
