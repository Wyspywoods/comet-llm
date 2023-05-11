#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

from pathlib import Path

from setuptools import find_packages, setup

requirements = ["comet_ml", "typing_extensions>=3.7.4", "dataclasses; python_version<'3.7.0'"]

# read the contents of your PACKAGE file

this_directory = Path(__file__).parent
#long_description = (this_directory / "PACKAGE.md").read_text()


setup(
    author="Comet ML Inc.",
    author_email="mail@comet.ml",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
    ],
    description="Comet logger for LLM",
    install_requires=requirements,
    long_description="Comet SDK for logging LLM chains",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="comet_llm",
    name="comet_llm",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://www.comet.ml",
    version="0.0.1",
    zip_safe=False,
    license="Proprietary",
)