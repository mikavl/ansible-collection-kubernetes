#!/usr/bin/env python3

import urllib.request
import re

class FilterModule(object):

    def filters(self):
        return {
            "github_latest": self.github_latest,
        }

    def github_latest(self, repository):
        url = "https://github.com/{0}/releases/latest".format(repository)
        regex = 'href="/{0}/releases/tag/v([0-9]+\.[0-9]+\.[0-9]+)"'.format(repository)

        with urllib.request.urlopen(url) as response:
            content = response.read().decode(response.headers.get_content_charset())
            result = re.search(regex, content)
            return result.group(1)
