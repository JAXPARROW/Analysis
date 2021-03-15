from django.db import models
from django.db.models.fields import CharField


SITE_CONFIGURATION = [
    ("GXX" , "GXX"),
    ("GHX", "GHX"),
    ("GHS", "GHS"),
    ("OHS", "OHS"),
    ("OHX", "OHX"),
    ("OXX", "OXX"),

]


class SitesDatabase(models.Model):
    Site = models.CharField(max_length=10)
    LegacySiteID = models.CharField(max_length=10)
    SiteName = models.CharField(max_length=50)
    Configuration = models.CharField(max_length=4, choices=SITE_CONFIGURATION)
    Cluster = models.CharField(max_length=50)
    FE = models.CharField(max_length=100)
    # noc_operator = models.CharField(max_length=100)
    # fs = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = 'Site Database'
        verbose_name_plural = 'Sites Database'

    def __str__(self):
        return self.SiteName


class RelayData(models.Model):
    StartDate = models.DateField()
    zone = models.CharField(max_length=25)
    LegacySiteID = models.CharField(max_length=25)
    SiteName = models.CharField(max_length=50)
    GeneratorRunDHM = models.CharField(max_length=10)
    GeneratorRunMinutes = models.CharField(max_length=10)
    CummulativeRunningDHM = models.CharField(max_length=10)
    CummulativeRunningMinutes = models.CharField(max_length=10)
    GeneratorStopMinutes = models.CharField(max_length=10)
    GeneratorStopDHM = models.CharField(max_length=10)
    CummulativeStopMinutes = models.CharField(max_length=10)
    CummulativeStopDHM = models.CharField(max_length=10)
    datasourcename	= models.CharField(max_length=10)
    HTT_TrialSite = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Relay Data'
        verbose_name_plural = 'Relay Data'

    def __str__(self):
        return self.SiteName


