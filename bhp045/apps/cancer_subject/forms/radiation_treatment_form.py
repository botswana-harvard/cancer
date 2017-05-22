from django import forms
from .base_subject_model_form import BaseSubjectModelForm
from ..models import RadiationTreatment


class RadiationTreatmentForm (BaseSubjectModelForm):

    class Meta:
        model = RadiationTreatment
