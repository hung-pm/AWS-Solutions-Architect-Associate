import sys
import logging

from xmfixer import XMindFileFixer

fixed_files = []
failed_files = []

file_path = "/Users/phamminhhung/PycharmProjects/XmindProject/input/Database copy.xmind"

fixed_file = XMindFileFixer(file_path).fix()
if fixed_file:
    fixed_files.append(fixed_file)
else:
    failed_files.append(file_path)