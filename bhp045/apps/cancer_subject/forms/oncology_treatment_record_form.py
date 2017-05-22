from django import forms

from edc.constants import YES, NO

from .base_subject_model_form import BaseSubjectModelForm
from ..models import OncologyTreatmentRecord, OTRChemo, OTRRadiation, OTRSurgical


# OncologyTreatmentRecord
class OncologyTreatmentRecordForm (BaseSubjectModelForm):

    class Meta:
        model = OncologyTreatmentRecord


#OTRChemo
class OTRChemoForm (BaseSubjectModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['chemo_delays'] == YES and not cleaned_data['why_delayed']:
            raise forms.ValidationError('If doses have been delayed, what is the reason for the delay')
        if cleaned_data['chemo_delays'] == NO and cleaned_data['why_delayed']:
            raise forms.ValidationError('NO doses where delayed, do not provide any delay reasons')
        if cleaned_data['chemo_reduced'] == YES and not cleaned_data['why_reduced']:
            raise forms.ValidationError('If doses have been reduced, why were the doses reduced')
        if cleaned_data['chemo_reduced'] == NO and cleaned_data['why_reduced']:
            raise forms.ValidationError('NO doses reduced, do not provide any reasons for reducing dose')
        cleaned_data = super(OTRChemoForm, self).clean()
        return cleaned_data

    class Meta:
        model = OTRChemo


#OTRRadiation
class OTRRadiationForm (BaseSubjectModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data

    #validating radiation
        if cleaned_data['radiation_details'] == 'Yes' and not cleaned_data['concomitant'] and not cleaned_data['amount_radiation']:
            raise forms.ValidationError('If patient radiation details are available, please provide remaining details on form')
        cleaned_data = super(OTRRadiationForm, self).clean()
        return cleaned_data

    class Meta:
        model = OTRRadiation


#OTRSurgical
class OTRSurgicalForm (BaseSubjectModelForm):

    class Meta:
        model = OTRSurgical
