import dateutil.parser
from datetime import timedelta
from django.db import models


class RadiationTreatmentRecordManager(models.Manager):
    def get_by_natural_key(self, created, report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk):
        if isinstance(created, basestring):
            created = dateutil.parser.parse(created)
        margin = timedelta(microseconds=999)
        RadiationTreatment = models.get_model('cancer_subject', 'RadiationTreatment')
        SubjectVisit = models.get_model('cancer_subject', 'SubjectVisit')
        subject_visit = SubjectVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk)
        radiation_treatment = RadiationTreatment.objects.get(subject_visit=subject_visit)
        return self.get(created__range=(created - margin, created + margin), radiation_treatment=radiation_treatment)
