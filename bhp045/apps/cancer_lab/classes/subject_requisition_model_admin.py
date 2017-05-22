from edc.lab.lab_requisition.admin import BaseRequisitionModelAdmin
from ...cancer_subject.models import SubjectVisit


class SubjectRequisitionModelAdmin (BaseRequisitionModelAdmin):

    visit_model = SubjectVisit
    visit_fieldname = 'subject_visit'
    dashboard_type = 'subject'
