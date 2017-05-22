import factory
from bhp_botswana.tests.factories import BaseBwConsentFactory
from cancer_subject.models import SubjectConsent


class SubjectConsentFactory(BaseBwConsentFactory):
    FACTORY_FOR = SubjectConsent
