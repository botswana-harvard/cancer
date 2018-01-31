from django.contrib import admin
from django.urls.conf import path, include

from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_registration.admin_site import edc_registration_admin

from cancer_subject.admin_site import cancer_subject_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_base.auth.views import LogoutView, LoginView
from edc_metadata.admin_site import edc_metadata_admin
from edc_sync.admin import edc_sync_admin

from .views import HomeView, AdministrationView


urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^admin/', edc_appointment_admin.urls),
    path(r'^admin/', cancer_subject_admin.urls),
    path(r'^admin/', edc_lab_admin.urls),
    path(r'^admin/', edc_identifier_admin.urls),
    path(r'^admin/', edc_metadata_admin.urls),
    path(r'^admin/', edc_registration_admin.urls),
    path(r'^admin/', edc_sync_admin.urls),
    path(r'^admininistration/', AdministrationView.as_view(),
         name='administration_url'),
    path('subject/', include('cancer_dashboard.urls')),
    path(r'^cancer_subject/', include('cancer_subject.urls')),
    path(r'^appointment/', include('edc_appointment.urls')),
    path(r'^edc/', include('edc_base.urls')),
    path(r'^edc_consent/', include('edc_consent.urls')),
    path(r'^edc_device/', include('edc_device.urls')),
    path(r'^edc_label/', include('edc_label.urls')),
    path(r'^edc_metadata/', include('edc_metadata.urls')),
    path(r'^edc_protocol/', include('edc_protocol.urls')),
    path(r'^edc_registration/',
         include('edc_registration.urls')),
    path(r'^edc_sync/', include('edc_sync.urls')),
    path(r'^edc_visit_schedule/',
         include('edc_visit_schedule.urls')),
    path(r'^tz_detect/', include('tz_detect.urls')),
    path('login', LoginView.as_view(), name='login_url'),
    path('accounts/login/', LoginView.as_view(), name='login_url'),
    path(r'', HomeView.as_view(), name='home_url'),
]
