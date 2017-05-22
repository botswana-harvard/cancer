import factory
from bhp_visit_tracking.tests.factories import BaseVisitTrackingFactory
from cancer_subject.models import SubjectVisit


class SubjectVisitFactory(BaseVisitTrackingFactory):
    FACTORY_FOR = SubjectVisit
