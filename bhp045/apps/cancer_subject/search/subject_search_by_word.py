from django.db.models import Q

from edc.dashboard.search.classes import BaseSearchByWord
from ..models import SubjectConsent


class SubjectSearchByWord(BaseSearchByWord):

    name = 'word'
    search_model = SubjectConsent
    order_by = ['-created']
    template = 'subjectconsent_include.html'

    @property
    def qset(self):
        qset = (
            Q(subject_identifier__icontains=self.search_value) |
            Q(first_name__icontains=self.search_value) |
            Q(last_name__icontains=self.search_value) |
            Q(identity__icontains=self.search_value)
            )
        return qset
