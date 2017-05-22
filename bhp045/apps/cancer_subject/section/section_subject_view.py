from edc.dashboard.section.classes import BaseSectionView, site_sections

from ..search import SubjectSearchByWord
from ..models import SubjectConsent


class SectionSubjectView(BaseSectionView):
    section_name = 'subject'
    section_display_name = 'Subjects'
    section_display_index = 10
    section_template = 'section_cancer_subject.html'
    dashboard_url_name = 'subject_dashboard_url'
    add_model = SubjectConsent
    search = {'word': SubjectSearchByWord}
    show_most_recent = True

site_sections.register(SectionSubjectView)
