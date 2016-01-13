from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone

from tools.decorators import dashboard_level_required

from .models import *


@dashboard_level_required
def dash_home_view(request):

    return render_to_response('dash_home.html', {
        'posts': FrontPost.objects.order_by('-updated'),
    }, context_instance=RequestContext(request))
