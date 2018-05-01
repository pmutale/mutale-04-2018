# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from resume.models import ResumeModel


class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ResumeModel, ResumeAdmin)
