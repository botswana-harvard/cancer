from edc.lab.lab_requisition.forms import BaseRequisitionForm
from edc.lab.lab_packing.forms import BasePackingListForm, BasePackingListItemForm
from ..cancer_lab.models import SubjectRequisition, PackingList, PackingListItem


class SubjectRequisitionForm(BaseRequisitionForm):

    def __init__(self, *args, **kwargs):

        super(SubjectRequisitionForm, self).__init__(*args, **kwargs)

        self.fields['item_type'].initial = 'dbs'

    def clean(self):

        cleaned_data = self.cleaned_data

        return cleaned_data

    class Meta:
        model = SubjectRequisition


class PackingListForm (BasePackingListForm):

    def clean(self):

        self.requisition = [SubjectRequisition, ]

        return  super(PackingListForm, self).clean()

    class Meta:
        model = PackingList


# PackingList
class PackingListItemForm (BasePackingListItemForm):

    def clean(self):

        self.requisition = [SubjectRequisition, ]

        return  super(BasePackingListItemForm, self).clean()

    class Meta:
        model = PackingListItem
