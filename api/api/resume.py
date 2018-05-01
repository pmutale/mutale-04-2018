from api import MutaleAPI


class Resume(MutaleAPI):
    def get_resume_specs(self, url_pattern):
        """
        Retrieve the payment specifications.
        :param url_pattern:
        :return: list of dicts like:
            [{
             "job_description":  "Alot of text",
             "job_title": "Managing director",
             "experience_1": Experience
            }]
        """
        resource = '/{0}'.format(url_pattern)
        result = self._get(resource)
        return result
