from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin


class HomeView(EdcBaseViewMixin, AppConfigViewMixin, TemplateView):

    name = 'cancer'
    listboard_template_name = 'cancer/listboard.html'
    dashboard_template_name = 'cancer/dashboard.html'
    base_template_name = 'cancer/base.html'
    listboard_url_name = 'cancer:listboard_url'
    dashboard_url_name = 'cancer/dashboard_url'
    admin_site_name = 'cancer_admin'
    url_namespace = 'cancer'
    template_name = 'cancer/home.html'
    home_url_name = 'cancer/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(navbar_item_selected='home')
        return context
