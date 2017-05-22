import dateutil.parser
from datetime import timedelta
from django.db import models


class HaartMedRecordManager(models.Manager):
    def get_by_natural_key(self, created, report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk):
        if isinstance(created, basestring):
            created = dateutil.parser.parse(created)
        margin = timedelta(microseconds=999)
        HaartMedRecord = models.get_model('cancer_subject', 'HaartMedRecord')
        SubjectVisit = models.get_model('cancer_subject', 'SubjectVisit')
        subject_visit = SubjectVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk)
        haart_med_record = HaartMedRecord.objects.get(subject_visit=subject_visit)
        return self.get(created__range=(created - margin, created + margin), haart_med_record=haart_med_record)
