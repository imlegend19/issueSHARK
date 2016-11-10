from issueshark.backends.basebackend import BaseBackend


class GithubBackend(BaseBackend):
    @property
    def identifier(self):
        return 'bugzilla'

    def __init__(self, tracking_url):
        super().__init__(tracking_url)

    def process(self):
        pass