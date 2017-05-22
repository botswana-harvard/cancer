import factory
from bhp_off_study.tests.factories import BaseOffStudyFactory
from cancer_subject.models import SubjectOffStudy


class SubjectOffStudyFactory(BaseOffStudyFactory):
    FACTORY_FOR = SubjectOffStudy
