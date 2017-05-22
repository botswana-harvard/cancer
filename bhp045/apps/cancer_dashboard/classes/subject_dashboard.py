from edc.dashboard.subject.classes import RegisteredSubjectDashboard
from edc.subject.registration.models import RegisteredSubject

from apps.cancer_subject.models import (SubjectConsent, SubjectVisit, Locator,
                                        CancerDiagnosis, EnrollmentChecklist, SymptomsAndTesting)


class SubjectDashboard(RegisteredSubjectDashboard):

    view = 'dashboard'
    dashboard_name = 'Subject Dashboard'
    urlpattern_view = 'apps.cancer_dashboard.views'
    dashboard_url_name = 'subject_dashboard_url'
    template_name = 'subject_dashboard.html'
    urlpatterns = [
        RegisteredSubjectDashboard.urlpatterns[0][:-1] + '(?P<appointment_code>{appointment_code})/$'
        ] + RegisteredSubjectDashboard.urlpatterns
    urlpattern_options = dict(
        RegisteredSubjectDashboard.urlpattern_options,
        dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|subject_consent',
        dashboard_type='subject',
        appointment_code=('1000|1300|1600|1900|2200|2500||2800|3100|3400|3700|4000|4300|'
                          '4600|4900|5200|5500|5800|6100|6400|6700|7000'))

    def __init__(self, *args, **kwargs):
        super(SubjectDashboard, self).__init__(*args, **kwargs)
        self.visit_model = SubjectVisit
        self.subject_dashboard_url = 'subject_dashboard_url'
        self.membership_form_category = ['subject_enrollment']
        self.dashboard_type_list = ['subject']
        self.dashboard_models['subject_consent'] = SubjectConsent
        self.dashboard_models['enrollment_checklist'] = EnrollmentChecklist
        self.membership_form_category = ['subject_enrollment']
        self.dashboard_models['visit'] = self._visit_model
        self._locator_model = Locator
        self._requisition_model = None

    def get_context_data(self, **kwargs):
        super(SubjectDashboard, self).get_context_data(**kwargs)
        self.context.update(
            home='cancer',
            search_name='subject',
            subject_dashboard_url=self.get_subject_dashboard_url(),
            title='Subject Dashboard',
            subject_consent=self.consent,
            cancer_diagnosis=self.cancer_diagnosis_model(),
            symptoms_and_testing=self.symptoms_and_testing_model(),
            )
        return self.context

    @property
    def consent(self):
        self._consent = None
        try:
            self._consent = SubjectConsent.objects.get(id=self.dashboard_id)
        except SubjectConsent.DoesNotExist:
            pass
        return self._consent

    @property
    def registered_subject(self):
        if not self._registered_subject:
            pass
            try:
                self._registered_subject = RegisteredSubject.objects.get(pk=self.dashboard_id)
            except RegisteredSubject.DoesNotExist:
                try:
                    self._registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)
                except RegisteredSubject.DoesNotExist:
                    try:
                        self._registered_subject = self.appointment.registered_subject
                    except AttributeError:
                        pass
        return self._registered_subject

    @property
    def subject_identifier(self):
        self._subject_identifier = None
        if self.consent:
            self._subject_identifier = self.consent.subject_identifier
        else:
            pass
        return self._subject_identifier

    def get_subject_dashboard_url(self):
        return 'subject_dashboard_url'

    def set_dashboard_type_list(self):
        self._dashboard_type_list = ['subject']

    def get_subject_identifier(self):
        return self.subject_identifier

    def get_visit_model(self):
        return SubjectVisit

    def cancer_diagnosis_model(self):
        try:
            cancer_diagnosis = CancerDiagnosis.objects.get(subject_visit=self.get_subject_visit().first())
        except CancerDiagnosis.DoesNotExist:
            cancer_diagnosis = None
        return cancer_diagnosis

    def get_subject_visit(self):
        try:
            # subject_visit = self.get_visit_model().objects.filter(subject_identifier=self.registered_subject.subject_identifier).order_by('appointment__visit_definition__code')
            subject_visit = self.get_visit_model().objects.filter(appointment__registered_subject__subject_identifier=self.registered_subject.subject_identifier).order_by('appointment__visit_definition__code')       
        except self.get_visit_model().DoesNotExist:
            subject_visit = None
        return subject_visit

    @property
    def subject_hiv_status(self):
        return None

    def symptoms_and_testing_model(self):
        st = SymptomsAndTesting.objects.filter(subject_visit=self.get_subject_visit())
        if st:
            if st[0].hiv_result == 'Pos':
                self._symptoms_and_testing_model = 'POS'
            elif st[0].hiv_result == 'Neg':
                self._symptoms_and_testing_model = 'NEG'
            elif st[0].hiv_result == 'Ind':
                self._symptoms_and_testing_model = 'IND'
            elif st[0].hiv_result == 'Pending':
                self._symptoms_and_testing_model = 'PEN'
            elif st[0].hiv_result == 'Refusing':
                self._symptoms_and_testing_model = 'REF'
            elif not self._symptoms_and_testing_model:
                self._symptoms_and_testing_model = 'UNK'
            return self._symptoms_and_testing_model
