from django.db import models
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from DgRun.models import SitesDatabase,RelayData
from DgRun.resources import *


from django.utils.translation import gettext_lazy as _

class Over_Run(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Over 10 Hours')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'GeneratorRunMinutes'

    def lookups(self, request, model_admin):

        return (
            ('10', _('10 Hours')),
            ('4', _('4 Hours')),
        )

    def queryset(self, request, queryset):


        if self.value() == '10': 
            return queryset.filter(GeneratorRunMinutes__gt=1439)
        elif self.value() == '4':
            return queryset.filter(GeneratorRunMinutes__gte=100)








# this will clear site database table
def delete_all_Sites(modeladmin, request, queryset):
    queryset = SitesDatabase.objects.all().delete()
    delete_all_Relay_Data.short_description = "Clear All Entries"

@admin.register(SitesDatabase)
class SitesDatabase(ImportExportModelAdmin):
    list_display = ['Site','LegacySiteID','SiteName','Cluster','FE','Configuration']
    list_filter = ['Cluster','Configuration']
    search_fields = ['Site', 'LegacySiteID', 'SiteName', 'FE']
    actions = [delete_all_Sites]
    resource_class = SiteResource


# this will clear relay database table
def delete_all_Relay_Data(modeladmin, request, queryset):
    queryset = RelayData.objects.all().delete()
    delete_all_Relay_Data.short_description = "Clear All Entries"

@admin.register(RelayData)
class RelayDataAadmin(ImportExportModelAdmin):
    list_display = ['LegacySiteID','SiteName','GeneratorRunMinutes']
    search_fields = ['LegacySiteID', 'SiteName']
    date_hierarchy = 'StartDate'
    actions = [delete_all_Relay_Data]
    list_filter = (Over_Run,)




admin.site.site_header = "IoT"
admin.site.site_title = "IoT"