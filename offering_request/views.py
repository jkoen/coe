# Create your views here.
from django import http
from django import shortcuts
from django.core.urlresolvers import reverse
from django.views.generic import detail

from .models import Offering, Platform, PlatformOffering, Offering_request
from .forms import Offering_requestForm


def offering_request(request):
    if request.method == 'POST':
        form = Offering_requestForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return http.HttpResponseRedirect('/coe/thanks/')
    else:
        form = Offering_requestForm()

    context = dict(form=form)

    return shortcuts.render(
        request,
        'offering_request/offering_request_form.html',
        context
    )


class PlatformConfiguration(detail.BaseDetailView):
    model = Platform

    def get(self, request, *args, **kwargs):
        platform = self.get_object()

        return http.JsonResponse({
            # Return the list of allowed offerings for this platform
            'offerings': list(platform.offerings.values_list('pk', 'name'))
        })

class PlatformOfferingConfiguration(detail.BaseDetailView):
    model = PlatformOffering

    def get(self, request, *args, **kwargs):
        platformoffering = PlatformOffering.objects.filter(
            platform__pk=kwargs['platform_pk'],
            offering__pk=kwargs['offering_pk'],
        ).first()

        return http.JsonResponse({
            # Return the list of fields to hide for this platform offering
            'hide_fields': (
                platformoffering.hide_fields.split(',')
                if platformoffering else []
            ),
        })

def thanks(request):
    #instance = RequestOfferinc.objects.get(pk=request.GET['pk'])
    #form_class = Offering_requestForm

    #if request.method == 'POST':
    #    form = form_class(request.POST or None)

    context = dict()

    return shortcuts.render(
        request,
        'offering_request/thanks.html',
        context
    )

