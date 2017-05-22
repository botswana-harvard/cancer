from django.contrib import admin

from edc.lab.lab_packing.admin import BasePackingListAdmin, BasePackingListItemAdmin

from .classes import SubjectRequisitionModelAdmin
from .models import SubjectRequisition, PackingList, PackingListItem
from ..cancer_lab.forms import SubjectRequisitionForm, PackingListForm, PackingListItemForm


class SubjectRequisitionAdmin(SubjectRequisitionModelAdmin):

    form = SubjectRequisitionForm

admin.site.register(SubjectRequisition, SubjectRequisitionAdmin)


class PackingListAdmin(BasePackingListAdmin):

    form = PackingListForm
    requisition = [SubjectRequisition, ]
    packing_list_item_model = PackingListItem

admin.site.register(PackingList, PackingListAdmin)


class PackingListItemAdmin(BasePackingListItemAdmin):

    form = PackingListItemForm
    requisition = [SubjectRequisition, ]

admin.site.register(PackingListItem, PackingListItemAdmin)
