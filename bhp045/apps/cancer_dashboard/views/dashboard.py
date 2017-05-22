from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

# from edc.subject.registration.models import RegisteredSubject
from ..classes import SubjectDashboard
#from cancer_subject.models import SubjectConsent


@login_required
def dashboard(request, **kwargs):
    dashboard = SubjectDashboard(
        dashboard_type=kwargs.get('dashboard_type'),
        dashboard_id=kwargs.get('dashboard_id'),
        dashboard_model=kwargs.get('dashboard_model'),
        dashboard_category=kwargs.get('dashboard_category'),
        registered_subject=kwargs.get('registered_subject'),
        show=kwargs.get('show'),
        dashboard_type_list=['subject'],
        )
    dashboard.set_context()
    return render_to_response(
        'subject_dashboard.html',
        dashboard.context.get(),
        context_instance=RequestContext(request))

# def dashboard(request, **kwargs):
#
#     if kwargs.get('dashboard_type') == 'subject':
#         if kwargs.get('subject_identifier'):
#             subject_identifier = kwargs.get('subject_identifier')
#         elif kwargs.get('pk'):
#             #if SubjectConsent.objects.get(pk=unicode(kwargs.get('pk'))).exists():
#             #    subject_consent = SubjectConsent.objects.get(pk=unicode(kwargs.get('pk')))
#             pass
#         elif kwargs.get('registered_subject'):
#             registered_subject = RegisteredSubject.objects.get(pk=kwargs.get('registered_subject'))
#             subject_identifier = registered_subject.subject_identifier
#         else:
#             subject_identifier = ''
#         if RegisteredSubject.objects.filter(subject_identifier=subject_identifier).exists():
#             registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_identifier)
#         dashboard = SubjectDashboard(**kwargs)
#         dashboard.create(
#             registered_subject=registered_subject,
#             visit_code=kwargs.get('visit_code'),
#             visit_instance=kwargs.get("visit_instance"))
# #        dashboard.context.add(
# #            subject_consent=subject_consent)
#     else:
#         raise ValueError('Unknown dashboard_type, must be \'subject\'. Got %s' % kwargs.get('dashboard_type'))
#     return render_to_response(
#         dashboard.template,
#         dashboard.get_context(),
#         context_instance=RequestContext(request))