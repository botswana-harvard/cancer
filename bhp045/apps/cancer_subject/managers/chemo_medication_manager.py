import dateutil.parser
from datetime import timedelta
from django.db import models


class ChemoMedPlanManager(models.Manager):
    def get_by_natural_key(self, created, report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk):
        if isinstance(created, basestring):
            created = dateutil.parser.parse(created)
        margin = timedelta(microseconds=999)
        ChemoMedPlan = models.get_model('cancer_subject', 'ChemoMedPlan')
        SubjectVisit = models.get_model('cancer_subject', 'SubjectVisit')
        subject_visit = SubjectVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk)
        chemo_med_plan = ChemoMedPlan.objects.get(subject_visit=subject_visit)
        return self.get(created__range=(created - margin, created + margin), chemo_med_plan=chemo_med_plan)


class ChemoMedRecordManager(models.Manager):
    def get_by_natural_key(self, created, report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk):
        if isinstance(created, basestring):
            created = dateutil.parser.parse(created)
        margin = timedelta(microseconds=999)
        OTRChemo = models.get_model('cancer_subject', 'OTRChemo')
        SubjectVisit = models.get_model('cancer_subject', 'SubjectVisit')
        subject_visit = SubjectVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk)
        otr_chemo = OTRChemo.objects.get(subject_visit=subject_visit)
        return self.get(created__range=(created - margin, created + margin), otr_chemo=otr_chemo)
