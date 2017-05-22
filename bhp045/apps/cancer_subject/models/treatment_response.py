from django.db import models

from edc.audit.audit_trail import AuditTrail

from ...cancer_list.models import InfoDeterminant

from ..choices.treatment_response import CANCER_RESPONSE
from .base_scheduled_visit_model import BaseScheduledVisitModel


class TreatmentResponse (BaseScheduledVisitModel):

    tx_response_class = models.CharField(
        verbose_name="1. Response to cancer treatment as classified by oncologist / doctor?",
        max_length=95,
        choices=CANCER_RESPONSE,
        help_text="",
        )

    tx_info_determinant = models.ManyToManyField(InfoDeterminant,
        verbose_name="2. Information used by oncologist / doctor to determine treatment response?",
        max_length=45,
        help_text="",
        )

    tx_response_date = models.DateField(
        verbose_name="3. Date of assessment of treatment response:",
        max_length=25,
        )

    tx_response = models.TextField(
        verbose_name=("4. Briefly describe response to treatment and information used to judge "
                      "treatment response: "),
        max_length=350,
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.subject_visit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Treatment Response"
