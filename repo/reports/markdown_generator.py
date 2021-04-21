class MarkdownGenerator():

    @classmethod
    def build(cls, repos):
        item = ''.join(
            f'**ID:** {repo.id} **Name:** {repo.name} **Stars:** {repo.stars}\n'
            for repo in repos)
        return f'## REPOS \n\n{item}'
