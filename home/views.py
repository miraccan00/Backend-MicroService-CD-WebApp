import subprocess
from pathlib import Path
from django.shortcuts import render
from .models import MicroServices,TrackMicroServiceVersion
import os
import logging
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    services = MicroServices.objects.all()
    if request.method == 'POST':
        for service in services:
            name = request.POST.get(service.name)
            version = request.POST.get('service_version_{}'.format(service.id))
            if name and version:
                old_version = service.version
                service.version = version
                service.save()
                trackms = TrackMicroServiceVersion(service=service, old_version=old_version, new_version=version)
                trackms.save()
                logger.info("Service version updated: service_name=%s, old_version=%s, new_version=%s", service.name, old_version, version)
            else:
                logger.warning("Skipping service update: service_name=%s, service_version=%s", name, version)
    context = {
        'services': services,
    }
    return render(request, 'home/index.html', context)



def service_version(request):
    trackmicroservices = TrackMicroServiceVersion.objects.all().order_by('-date')
    context = {
        'trackmicroservices': trackmicroservices,
    }
    return render(request, 'home/service_version.html', context=context)
