from edc.base.model.models import BaseListModel


class ResultsToRecord (BaseListModel):
    pass

    class Meta:
        app_label = "cancer_list"
        verbose_name = "Results To Record"
        verbose_name_plural = "Results To Record"
