# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.encoding import force_text

from django.views import View
from django.views.generic import TemplateView
from api.api.resume import Resume
from resume import models

api = Resume()


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context), **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        output = list(context['data'].values())
        data = {'data': output}
        return data


class ResumeView(JSONResponseMixin, TemplateView):
    template_name = 'theme/theme_2018_home.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['data'] = models.ResumeModel.objects.only('job_description', 'job_title')
        return context

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class Resume(TemplateView):
    template_name = 'resume/resume.html'

    def get_context_data(self, **kwargs):
        context = super(Resume, self).get_context_data(**kwargs)
        params = 'resume_data'
        # data = api.get_resume_specs(params)
        context.update({
            'data': 'tHIS IS A RESUME'
        })
        return context

