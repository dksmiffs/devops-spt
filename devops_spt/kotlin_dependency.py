"""Automate management of Kotlin versions"""
from os.path import basename
from urllib.parse import urlparse
from re import MULTILINE, search
from requests import get
from .external_dependency import ExternalDependency


class KotlinDependency(ExternalDependency):
    """Concrete class for managing Kotlin dependency"""

    def existing(self):
        """Return installed Kotlin version"""
        with open('build.gradle.kts') as inf:
            filedata = inf.read()
            version = search('^ *kotlin."jvm". version "(.+)"$',
                             filedata, MULTILINE)
            return version.group(1)

    def latest(self):
        """Return latest Kotlin version available"""
        # Use Requests library to track the redirect, guidance here:
        #    https://bit.ly/2JRvapH
        req = get('https://github.com/JetBrains/kotlin/releases/latest')
        url = urlparse(req.url)
        base = basename(url.path)
        # strip off the leading "v"
        _, rhs = base.split("v", 1)
        return rhs

    def update(self, verbose=False):
        """Update installed Kotlin version to latest if necessary"""
        old = self.existing()
        new = self.latest()
        if verbose:
            print('existing Kotlin ==> ' + old)
            print('latest Kotlin   ==> ' + new)
        if old == new:
            if verbose:
                print("Kotlin update not necessary")
        else:
            # Guidance: https://stackoverflow.com/a/17141572
            with open('build.gradle.kts', 'r') as inf:
                filedata = inf.read()
            filedata = filedata.replace(old, new)
            # write the same filename out again
            with open('build.gradle.kts', 'w', newline='\n') as outf:
                outf.write(filedata)
