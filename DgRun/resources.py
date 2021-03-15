from import_export import resources

from .models import SitesDatabase

class SiteResource(resources.ModelResource):

    class Meta:
        model = SitesDatabase
        skip_unchanged = True
        report_skipped = True
        # exclude = ('id', )
        fields = ('id','Site','LegacySiteID','SiteName','Configuration','FE','Cluster')
        export_order = ('id','Site','LegacySiteID','SiteName','Configuration','FE','Cluster')
  
