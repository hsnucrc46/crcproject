from rich import print
from rich.markdown import Markdown

with open("run/src/INTRO.md") as readme:
    markdown = Markdown(readme.read())
print(markdown)
