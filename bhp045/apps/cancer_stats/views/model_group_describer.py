from edc.core.model_data_inspector.views.base_model_group_describer import base_model_group_describer


def model_group_describer(request, **kwargs):

    app_list = ['cancer_subject']

    return base_model_group_describer(request, app_list=app_list, **kwargs)
