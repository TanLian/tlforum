# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

import logging
logger = logging.getLogger(__name__)

def home(request):
    logger.error('......')
    return render_to_response('base.html', {})
