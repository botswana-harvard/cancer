# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel


class LabResultChemistry(BaseScheduledVisitModel):

    chem_drawn_date = models.DateField(
        verbose_name="Date of chemistry specimen draw:",
        blank=True,
        null=True,
        max_length=25,
        help_text="",
        )

    alanine = models.DecimalField(
        verbose_name="Alanine aminotransferase (ALT or SGPT):",
        max_digits=6,
        blank=True,
        null=True,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(9000)],
        help_text="U/L"
        )

    aspartate = models.DecimalField(
        verbose_name="Aspartate aminotransferase (AST or SGOT):",
        max_digits=6,
        blank=True,
        null=True,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(9000)],
        help_text="U/L"
        )

    bilirubin = models.DecimalField(
        verbose_name="Bilirubin:",
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=True,
        null=True,
        help_text="mg/dL"
        )

    creatinine = models.DecimalField(
        verbose_name="Creatinine:",
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(9000)],
        blank=True,
        null=True,
        help_text="umol/L"
        )

    lactate = models.DecimalField(
        verbose_name="Lactate Dehydrogenase (LDH):",
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(9000)],
        blank=True,
        null=True,
        help_text="IU/L"
        )
    #v2 added comments field for when form has "-3" input
    comments = models.TextField(
        verbose_name="Comments:",
        max_length=100,
        null=True,
        blank=True,
        help_text="if other data not recorded, explain why",
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_labresultchemistry_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: Chemistry"
        verbose_name_plural = "Lab Result: Chemistry"
