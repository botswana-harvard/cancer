from django.db import models


class EnrollmentSiteManager(models.Manager):

    def get_by_natural_key(self, site_name):
        return self.get(site_name=site_name)
