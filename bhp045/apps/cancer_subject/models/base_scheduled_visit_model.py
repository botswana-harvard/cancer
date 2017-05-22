from datetime import datetime
from django.db import models

from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future
from edc.entry_meta_data.managers import EntryMetaDataManager

from subject_visit import SubjectVisit
from subject_base_uuid_model import SubjectBaseUuidModel
from ..managers import ScheduledModelManager


class BaseScheduledVisitModel(SubjectBaseUuidModel):

    """ Base model for all scheduled models (adds key to :class:`SubjectVisit`). """

    subject_visit = models.OneToOneField(SubjectVisit)

    entry_meta_data_manager = EntryMetaDataManager(SubjectVisit)

    report_datetime = models.DateTimeField("Today's date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=datetime.today(),
        )

    objects = ScheduledModelManager()

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_report_datetime(self):
        return self.subject_visit.report_datetime

    def get_subject_identifier(self):
        return self.subject_visit.get_subject_identifier()

    def get_visit(self):
        return self.subject_visit

    def natural_key(self):
        return self.subject_visit.natural_key()

    class Meta:
        abstract = True
