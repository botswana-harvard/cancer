import factory
from bhp_base_model.tests.factories import BaseUuidModelFactory
from cancer_subject.models import BaseRiskAssessment
from cancer_subject.tests.factories import SubjectVisitFactory


class BaseRiskAssessmentFactory(BaseUuidModelFactory):
    FACTORY_FOR = BaseRiskAssessment

    subject_visit = factory.SubFactory(SubjectVisitFactory)
