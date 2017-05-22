from django.db import models
from edc.audit.audit_trail import AuditTrail
from edc.lab.lab_requisition.models import BaseRequisition
from ...cancer_subject.models import SubjectVisit
from packing_list import PackingList


class SubjectRequisition(BaseRequisition):

    subject_visit = models.ForeignKey(SubjectVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    history = AuditTrail()

    def get_visit(self):
        return self.patient_visit

    class Meta:
        app_label = 'cancer_lab'
        verbose_name = 'Patient Lab Requisition'
