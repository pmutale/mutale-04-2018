from django.conf.urls import url

from resume.views import ResumeView, Resume

app_name = 'resume'

urlpatterns = [
    url('resume_data/', ResumeView.as_view(), name='resume_data'),
    url('resume/', Resume.as_view(), name='resume')
]