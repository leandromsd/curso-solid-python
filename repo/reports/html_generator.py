class HTMLGenerator():

    @classmethod
    def build(cls, repos):
        item = ''.join(
            f'<strong>ID: </strong> {repo.id} <strong>Name: </strong> {repo.name} <strong>Stars: </strong> {repo.stars}<br> \n'
            for repo in repos)
        return f'<p>{item}</p>'
