# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class Theme(TemplateView):
    template_name = 'theme/theme_2018_home.html'

    def get_context_data(self, **kwargs):
        context = super(Theme, self).get_context_data(**kwargs)
        context['data'] = 'I am a piece of data'
        return context



