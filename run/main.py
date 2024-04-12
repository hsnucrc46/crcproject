from rich import print
from rich.markdown import Markdown

with open("src/INTRO.md", encoding="utf8") as readme:
    markdown = Markdown(readme.read())
print(markdown)
