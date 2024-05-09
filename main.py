import os
import time

from rich import print
from rich.markdown import Markdown

os.system("cd run")

with open("run/src/INTRO.md", encoding="utf8") as readme:
    markdown = Markdown(readme.read())
print(markdown)

# time.sleep(10)
os.system("python run/underlying/main.py")
os.system("python run/spaceship/main.py")
os.system("python run/123/123.py")
