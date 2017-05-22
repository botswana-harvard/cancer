from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('edc.core.model_data_inspector.views.model_group_describer',
    url(r'^model_describer/', 'model_group_describer', name="model_describer_url_name"),
    )


urlpatterns += patterns('apps.cancer_stats.views',
    url(r'^$', 'index', name="stats_home_url"),
    )
