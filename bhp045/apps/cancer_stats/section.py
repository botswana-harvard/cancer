from edc.dashboard.section.classes import BaseSectionView, site_sections


class SectionStatisticsView(BaseSectionView):
    section_name = 'statistics'
    section_display_name = 'Statistics'
    section_display_index = 50
    section_template = 'section_statistics.html'
    #dashboard_url_name = 'subject_dashboard_url'

    def contribute_to_context(self, context, request, *args, **kwargs):
        return context

site_sections.register(SectionStatisticsView)
