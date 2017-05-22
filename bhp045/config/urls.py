from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import django_databrowse

from django.db.models import get_models
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover

from edc.subject.rule_groups.classes import site_rule_groups
#from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.data_manager.classes import data_manager
from edc.dashboard.section.classes import site_sections
from edc.subject.visit_schedule.classes import site_visit_schedules

from apps.cancer.cancer_app_configuration.classes import CancerAppConfiguration
CancerAppConfiguration().prepare()
site_visit_schedules.autodiscover()
site_visit_schedules.build_all()
site_rule_groups.autodiscover()
#site_lab_tracker.autodiscover()
data_manager.prepare()
site_sections.autodiscover()
dajaxice_autodiscover()
admin.autodiscover()

APP_NAME = settings.APP_NAME

for model in get_models():
    try:
        django_databrowse.site.register(model)
    except:
        pass

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/logout/$', RedirectView.as_view(url='/{app_name}/logout/'.format(app_name=APP_NAME))),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^{app_name}/section/statistics/'.format(app_name=APP_NAME),
         include('apps.cancer_stats.urls'), name="stats_url_name"),
 )

urlpatterns += patterns('',
    url(r'^{app_name}/dashboard/'.format(app_name=APP_NAME),
        include('apps.{app_name}_dashboard.urls'.format(app_name=APP_NAME))),
)

urlpatterns += patterns(
    '',
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

urlpatterns += patterns(
    '',
    url(r'^databrowse/(.*)', login_required(django_databrowse.site.root)),
)

urlpatterns += patterns(
    '',
    url(r'^audit_trail/', include('edc.audit.urls'), name="audit_trail_url_name"),
)

urlpatterns += patterns('',
    url(r'^{app_name}/login/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.login',
        name='{app_name}_login'.format(app_name=APP_NAME)),
    url(r'^{app_name}/logout/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.logout_then_login',
        name='{app_name}_logout'.format(app_name=APP_NAME)),
    url(r'^{app_name}/password_change/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.password_change',
        name='password_change_url'.format(app_name=APP_NAME)),
    url(r'^{app_name}/password_change_done/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'.format(app_name=APP_NAME)),
)
urlpatterns += patterns('',
    url(r'^{app_name}/section/'.format(app_name=APP_NAME),
        include('edc.dashboard.section.urls'), name='section'),
)

urlpatterns += patterns('',
    url(r'^{app_name}/$'.format(app_name=APP_NAME),
        RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
    url(r'', RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
    )

#urlpatterns += staticfiles_urlpatterns()
