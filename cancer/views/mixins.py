from django.apps import apps as django_apps


class AppConfigListboardUrlsViewMixin:

    """Adds listboard_url names for all apps"""

    dashboard_url_app_label = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            ambition_subject_dashboard_url_name=django_apps.get_app_config(
                'cancer_subject').dashboard_url_name,
            dashboard_url_name=django_apps.get_app_config(
                self.dashboard_url_app_label).dashboard_url_name,
        )
        return context
