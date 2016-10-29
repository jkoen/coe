from __future__ import unicode_literals

from django.db import models

# Create your models here.
from datetime import date
from .choices import Countries
from .choices import Location
from .choices import Status
from .choices import Services_required

class Offering_request(models.Model):
    platform = models.ForeignKey('Platform')
    offering = models.ForeignKey('Offering')
    insight_quote = models.IntegerField(default=0000)
    customer_name = models.CharField(max_length=120, default='Not Applicable')
    country = models.CharField(max_length=14, choices=Countries)
    deal_value = models.IntegerField(default=0000)
    request_date = models.DateField() ### Need to add default=date.today
    requester_name = models.CharField(max_length=35)
    requester_email = models.EmailField()
    requester_mobile_number = models.CharField(max_length=14)
    approval_manager_name = models.CharField(max_length=35)
    approval_manager_email = models.EmailField()
    presales_name = models.CharField(max_length=35)
    presales_email = models.EmailField()
    solution_support = models.CharField(max_length=3, choices=Services_required)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=13, choices=Location)
    solution_design = models.FileField(upload_to='solution_design/%Y-%m-%d')
    testplan = models.FileField(upload_to='testplan/%Y-%m-%d', blank=True, null=True)
    request_description = models.TextField()
    audience_description = models.TextField()


class Platform(models.Model):
    name = models.CharField(max_length=100)
    offerings = models.ManyToManyField(
        'Offering',
        blank=True,
        help_text='List of COE offerings to show for this platform'
    )

    def __unicode__(self):
        return self.name


class Offering(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class PlatformOffering(models.Model):
    """Configuration for an offering on a platform.

    This model exists to configure an offering for a particular platform only.
    It's important to understand that because we don't want to create a
    relation between Request and this PlatformOffering model, because a
    PlatformOffering may not exist at any time for a particular
    platform/offering combination.
    """
    platform = models.ForeignKey(Platform)
    offering = models.ForeignKey(Offering)
    hide_fields = models.CharField(
        max_length=200,
        help_text='List of fields to hide for this combination.',
        blank=True,
        default='',
    )

    class Meta:
        unique_together = (
            ('platform', 'offering'),
        )

    def __unicode__(self):
        return u'%s / %s' % (self.platform, self.offering)

