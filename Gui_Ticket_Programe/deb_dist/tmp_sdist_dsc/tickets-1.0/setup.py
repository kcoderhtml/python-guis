import os
from setuptools import setup
from nvpy import nvpy

setup(
    name = "tickets",
    version = "1.0",
    author = "Kieran A. Klukas",
    author_email = "kieran@klukas.net",
    description = "Demo of Booking Tickets",
    license = "BSD",
    url = "https://github.com/cpbotha/nvpy",
    packages=['tickets'],
    entry_points = {
        'gui_scripts' : ['myscript = myscript.myscript:main']
    },
    data_files = [
        ('share/applications/', ['tickets.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
