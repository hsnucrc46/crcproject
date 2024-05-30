import os
import time
import signal

from rich import print
from rich.markdown import Markdown
from rich.progress import track


def signal_handler(sig, frame):
    print("Keyboard interrupt detected. Exiting gracefully...")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    os.chdir("run")

    with open("src/INTRO.md", encoding="utf8") as readme:
        markdown = Markdown(readme.read())
    print(markdown)
    for step in track(range(10)):
        time.sleep(1)
    os.system("python underlying/main.py")
    os.system("python spaceship/main.py")
    os.system("python 123/123.py")
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting gracefully...")
    exit(0)
