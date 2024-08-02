# ruff: noqa
import sys

# The file contains helper functions and the mechanism to build the
# .sphinx/requirements.txt file that is needed to set up the virtual
# environment.

# You should not do any modifications to this file. Put your custom
# requirements into the custom_required_modules array in the custom_conf.py
# file. If you need to change this file, contribute the changes upstream.

legacyCanonicalSphinxExtensionNames = [
    "youtube-links",
    "related-links",
    "custom-rst-roles",
    "terminal-output"
    ]


def DeduplicateExtensions(extensionNames: [str]):
    extensionNames = dict.fromkeys(extensionNames)
    resultList = []
    encounteredCanonicalExtensions = []

    for extensionName in extensionNames:
        if extensionName in legacyCanonicalSphinxExtensionNames:
            extensionName = "canonical." + extensionName

        if extensionName.startswith("canonical."):
            if extensionName not in encounteredCanonicalExtensions:
                encounteredCanonicalExtensions.append(extensionName)
                resultList.append(extensionName)
        else:
            resultList.append(extensionName)

    return resultList

if __name__ == "__main__":
    requirements = [
        "furo",
        "pyspelling",
        "sphinx==6.2.1",
        "sphinx-autobuild",
        "sphinx-copybutton",
        "sphinx-design",
        "sphinxcontrib-jquery"
    ]

    # removes duplicate entries
    requirements = list(dict.fromkeys(requirements))
    requirements.sort()

    with open(".sphinx/requirements.txt", 'w') as requirements_file:
        requirements_file.write(
            "# DO NOT MODIFY THIS FILE DIRECTLY!\n"
            "#\n"
            "# This file is generated automatically.\n"
            "# Add custom requirements to the custom_required_modules\n"
            "# array in the custom_conf.py file and run:\n"
            "# make clean && make install\n")

        for requirement in requirements:
            requirements_file.write(requirement)
            requirements_file.write('\n')
