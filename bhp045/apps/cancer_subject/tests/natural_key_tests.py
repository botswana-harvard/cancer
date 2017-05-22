import re
import pprint
from datetime import datetime
from django.core import serializers
from bhp_crypto.classes import FieldCryptor
from django.db.models import get_app, get_models
from bhp_base_test.classes import BaseNaturalKeyTests
from bhp_lab_tracker.classes import lab_tracker
from bhp_sync.classes import SerializeToTransaction, DeserializeFromTransaction
from bhp_variables.models import StudySpecific, StudySite
from bhp_variables.tests.factories import StudySpecificFactory, StudySiteFactory
from bhp_registration.models import RegisteredSubject
from bhp_consent.tests.factories import ConsentCatalogueFactory
from bhp_appointment.models import Appointment
from bhp_appointment.tests.factories import ConfigurationFactory
from bhp_visit.tests.factories import MembershipFormFactory, ScheduleGroupFactory, VisitDefinitionFactory
from bhp_content_type_map.classes import ContentTypeMapHelper
from bhp_content_type_map.models import ContentTypeMap
from cancer_subject.models import SubjectVisit, SubjectConsent, EnrollmentChecklist
from cancer_subject.tests.factories import SubjectConsentFactory, EnrollmentChecklistFactory, SubjectVisitFactory, BaseRiskAssessmentFactory


class NaturalKeyTests(BaseNaturalKeyTests):

    app_label = 'cancer_subject'
    subject_consent = SubjectConsent
    consent_catalogue_name = 'Cancer V1'
    visit_model = SubjectVisit

    def test_p3(self):
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
        visit_tracking_content_type_map = ContentTypeMap.objects.get(content_type__model='testvisit')
        visit_definition = VisitDefinitionFactory(code='1000', title='Enrollment', visit_tracking_content_type_map=visit_tracking_content_type_map)
        visit_definition.schedule_group.add(schedule_group)

        print 'consent a subject'
        subject_consent = SubjectConsentFactory(study_site=study_site)
        print subject_consent.subject_identifier
        print 'get subject registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_consent.subject_identifier)
        print 'enroll subject'
        EnrollmentChecklistFactory(registered_subject=registered_subject)

        instances = []

        print 'test natural key / get_by_natural_key on subject_visit'
        appointment = Appointment.objects.get(registered_subject=registered_subject, visit_definition__code='1000')
        subject_visit = SubjectVisitFactory(appointment=appointment)
        instances.append(subject_visit)

        base_risk_assessment = BaseRiskAssessmentFactory(subject_visit=subject_visit)
        instances.append(base_risk_assessment)

        print 'test serialization.'
        self.serialize_deserialize(instances)
