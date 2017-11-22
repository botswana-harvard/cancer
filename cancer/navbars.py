from edc_navbar import NavbarItem, site_navbars, Navbar

cancer = Navbar(name='cancer')

cancer.append_item(
    NavbarItem(
        name='consented_subject',
        label='Consents',
        fa_icon='fa-user-plus',
        url_name='cancer_dashboard:consent_listboard_url'))

cancer.append_item(
    NavbarItem(
        name='enrollment_checklist',
        label='Enrollment Checklist',
        fa_icon='fa-user-circle-o',
        url_name='cancer_dashboard:checklist_listboard_url'))

site_navbars.register(cancer)
