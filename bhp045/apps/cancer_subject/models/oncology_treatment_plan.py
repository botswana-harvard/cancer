from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from ..choices.oncology_treatment import CHEMO_INTENT, CANCER_TREATMENT_GOAL
from .base_scheduled_visit_model import BaseScheduledVisitModel


class OncologyTreatmentPlan (BaseScheduledVisitModel):

    """ ca004 """
    #This is a new question with options from chemo_intent
    treatment_goal = models.CharField(
        verbose_name="What is the goal of cancer treatment?",
        max_length=15,
        choices=CANCER_TREATMENT_GOAL,
        )

    treatment_plan = models.CharField(
        verbose_name="Has a treatment plan been determined?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    chemotherapy = models.CharField(
        verbose_name="Is chemotherapy planned?",
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
        help_text="",
        )
    #This question remains the same but two options have been removed to new Q: treatment_goal
    #To do:
    #Data migration for responses here to move them to newQ
    chemo_intent = models.CharField(
         verbose_name="What was the intent of giving chemotherapy?",
         max_length=25,
         choices=CHEMO_INTENT,
         null=True,
         blank=True,
         help_text="",
         )

    radiation_plan = models.CharField(
        verbose_name="Is radiation therapy planned?",
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
        help_text="",
        )

#     radiation_treatments = models.CharField(
#         verbose_name="How many radiation treatments are planned?",
#         max_length=15,
#         null=True,
#         blank=True,
#         help_text="",
#         )

    surgical_plan = models.CharField(
        verbose_name="Is surgical therapy planned?",
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
        help_text="",
        )

    planned_operation = models.CharField(
        verbose_name="Describe planned operation",
        max_length=150,
        null=True,
        blank=True,
        help_text="",
        )

    comments = models.CharField(
        verbose_name="Comments",
        null=True,
        blank=True,
        max_length=350,
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return "%s" % self.subject_visit

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Oncology Treatment Plan"
