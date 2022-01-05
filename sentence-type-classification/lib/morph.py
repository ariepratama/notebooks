import subprocess
from typing import Text
import re


def parse(text: Text, morphind_loc="lib/morphind/MorphInd.pl"):
    """
    Do morphological parsing with Morphind. for example:
    menggunakan => ^meN+guna<n>+kan_VSA$
    :param text:
    :param morphind_loc:
    :return:
    """
    cleaned_text = re.sub("[^a-zA-Z0-9 ]", "", text)
    cleaned_text = cleaned_text.lower()
    cmd = f"echo {cleaned_text} | perl {morphind_loc}"
    return subprocess.check_output(cmd, shell=True).decode("utf-8")[:-1]
