from .classes import SubjectDashboard

#regex = {}
#regex['dashboard_type'] = 'subject'
#regex['dashboard_model'] = 'subject_consent'
# regex['subject_identifier'] = '045-[0-9]{9,11}-[0-9]{1}'
# regex['visit_code'] = '\w+'
# regex['visit_instance'] = '[0-9]{1}'
# subject_dashboard = SubjectDashboard()
#urlpatterns = SubjectDashboard.get_urlpatterns('apps.cancer_dashboard.views', regex, visit_field_names=['subject_visit', ])
# regex['subject_identifier'] = '045-[0-9]{3}-[0-9]{4}'
# urlpatterns += subject_dashboard.get_urlpatterns('apps.cancer_dashboard.views', regex, visit_field_names=['subject_visit', ])

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = []
for pattern in SubjectDashboard.get_urlpatterns():
    urlpatterns.append(
        url(pattern,
            login_required(SubjectDashboard.as_view()),
            name=SubjectDashboard.dashboard_url_name)
        )
