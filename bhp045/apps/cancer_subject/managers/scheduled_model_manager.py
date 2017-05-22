from django.db import models


class ScheduledModelManager(models.Manager):
    """Manager for all scheduled models (those with a subject_visit fk)."""
    def get_by_natural_key(self, report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk):
        SubjectVisit = models.get_model('cancer_subject', 'SubjectVisit')
        subject_visit = SubjectVisit.objects.get_by_natural_key(report_datetime, visit_instance, appt_status, code, subject_identifier_as_pk)
        return self.get(subject_visit=subject_visit)
