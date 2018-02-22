import os
import re


def relative_to_absolute(relative):
    return (os.getcwd() + relative)

def name_from_url(url):
    m = re.search('[^\/]{1,}(?!.)',url)
    return m.group(0)

def file_exists(local_url):
    return os.path.isfile(local_url)