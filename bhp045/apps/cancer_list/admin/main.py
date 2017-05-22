from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin
from ..models import WhoIllness, InfoDeterminant, ResultsToRecord, RadiationSideEffects


class WhoIllnessAdmin(BaseModelAdmin):
    pass
admin.site.register(WhoIllness, WhoIllnessAdmin)


class InfoDeterminantAdmin(BaseModelAdmin):
    pass
admin.site.register(InfoDeterminant, InfoDeterminantAdmin)


class ResultsToRecordAdmin(BaseModelAdmin):
    pass
admin.site.register(ResultsToRecord, ResultsToRecordAdmin)


class RadiationSideEffectsAdmin(BaseModelAdmin):
    pass
admin.site.register(RadiationSideEffects, RadiationSideEffectsAdmin)
