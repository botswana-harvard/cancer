import factory
from datetime import datetime
from bhp_registration.tests.factories import RegisteredSubjectFactory
from bhp_base_model.tests.factories import BaseUuidModelFactory
from cancer_subject.models import EnrollmentChecklist


class EnrollmentChecklistFactory(BaseUuidModelFactory):
    FACTORY_FOR = EnrollmentChecklist

    registration_datetime = datetime.today()
    has_diagnosis = 'Yes'
    registered_subject = factory.SubFactory(RegisteredSubjectFactory)
