from cancer_screening.admin_site import cancer_screening_admin
from cancer_subject.admin_site import cancer_subject_admin
from django.conf.urls import url, include
from django.contrib import admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_base.views import LogoutView, LoginView
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_registration.admin_site import edc_registration_admin
from edc_sync.admin import edc_sync_admin

from .views import HomeView, AdministrationView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', edc_appointment_admin.urls),
    url(r'^admin/', cancer_subject_admin.urls),
    url(r'^admin', cancer_screening_admin.urls),
    url(r'^admin/', edc_lab_admin.urls),
    url(r'^admin/', edc_identifier_admin.urls),
    url(r'^admin/', edc_metadata_admin.urls),
    url(r'^admin/', edc_registration_admin.urls),
    url(r'^admin/', edc_sync_admin.urls),
    url(r'^admininistration/', AdministrationView.as_view(),
        name='administration_url'),
    url('subject/',
        include('cancer_subject.urls')),
    url('screening/',
        include('cancer_screening.urls')),
    url(r'^appointment/',
        include('edc_appointment.urls')),
    url(r'^edc/', include('edc_base.urls')),
    url(r'^edc_consent/', include('edc_consent.urls')),
    url(r'^edc_device/', include('edc_device.urls')),
    url(r'^edc_lab/', include('edc_lab.urls')),
    url(r'^edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
    url(r'^edc_label/', include('edc_label.urls')),
    url(r'^edc_metadata/', include('edc_metadata.urls')),
    url(r'^edc_protocol/', include('edc_protocol.urls')),
    url(r'^edc_registration/',
        include('edc_registration.urls')),
    url(r'^edc_sync/', include('edc_sync.urls')),
    url(r'^edc_visit_schedule/',
        include('edc_visit_schedule.urls')),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    url(r'', HomeView.as_view(), name='home_url'),
]
