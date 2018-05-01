# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ResumeModel(models.Model):
    job_title = models.CharField(max_length=128, null=True, blank=True)
    job_description = models.CharField(max_length=1064, null=True, blank=False)



