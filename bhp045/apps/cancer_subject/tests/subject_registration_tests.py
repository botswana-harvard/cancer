import re
import pprint
from datetime import datetime, date, timedelta
from django.test import TestCase
from django.db.models import get_app, get_models
from bhp_identifier.exceptions import IdentifierError
from bhp_lab_tracker.classes import lab_tracker
from bhp_variables.models import StudySpecific, StudySite
from bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from bhp_registration.models import RegisteredSubject
from bhp_consent.tests.factories import ConsentCatalogueFactory
from bhp_appointment.models import Appointment
from bhp_appointment.tests.factories import ConfigurationFactory
from bhp_visit.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from bhp_content_type_map.classes import ContentTypeMapHelper
from bhp_content_type_map.models import ContentTypeMap
from cancer_subject.models import SubjectVisit, SubjectConsent, SubjectOffStudy, EnrollmentChecklist
from bhp_identifier.models import SubjectIdentifier, Sequence
from bhp_off_study.exceptions import SubjectOffStudyError, SubjectOffStudyDateError
from factories import SubjectVisitFactory, SubjectOffStudyFactory, SubjectConsentFactory, EnrollmentChecklistFactory, BaseRiskAssessmentFactory


class SubjectRegistrationTests(TestCase):
    app_label = 'cancer_subject'
    subject_consent = SubjectConsent
    consent_catalogue_name = 'cancer V1'
    visit_model = SubjectVisit

    def test_p1(self):
        lab_tracker.autodiscover()
        StudySpecificFactory()
        study_site = StudySiteFactory()
        ConfigurationFactory()
        content_type_map_helper = ContentTypeMapHelper()
        content_type_map_helper.populate()
        content_type_map_helper.sync()
        print 'setup the consent catalogue for app {0}'.format(self.app_label)
        content_type_map = ContentTypeMap.objects.get(content_type__model=self.subject_consent._meta.object_name.lower())
        consent_catalogue = ConsentCatalogueFactory(name=self.consent_catalogue_name, content_type_map=content_type_map)
        consent_catalogue.add_for_app = self.app_label
        consent_catalogue.save()

        print 'setup bhp_visit'
        content_type_map = ContentTypeMap.objects.get(content_type__model=EnrollmentChecklist._meta.object_name.lower())
        membership_form = MembershipFormFactory(content_type_map=content_type_map)
        schedule_group = ScheduleGroupFactory(membership_form=membership_form, group_name='Enrollment')
        visit_definition = VisitDefinitionFactory(code='1000', title='Enrollment')
        visit_definition.schedule_group.add(schedule_group)
        print 'consent a subject (3 days ago)'
        subject_consent = SubjectConsentFactory(study_site=study_site, consent_datetime=datetime.today() - timedelta(days=3))
        print subject_consent.subject_identifier
        print 'get subject registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_consent.subject_identifier)
        print registered_subject
        print 'enroll'
        enrollment_checklist = EnrollmentChecklistFactory(registered_subject=registered_subject)
        print enrollment_checklist
        print 'add a visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000')
        subject_visit = SubjectVisitFactory(appointment=appointment)
        print subject_visit
        print 'add off study'
        subject_off_study = SubjectOffStudyFactory(registered_subject=registered_subject, offstudy_date=date.today() - timedelta(days=0))
        print subject_off_study

        print 'inspect registered_subject, subject_type, name, initials, dob, ...'
        self.assertEquals(registered_subject.subject_type, 'subject')
        self.assertIsNotNone(registered_subject.first_name)
        self.assertIsNotNone(registered_subject.last_name)
        self.assertIsNotNone(registered_subject.initials)
        self.assertIsNotNone(registered_subject.dob)
