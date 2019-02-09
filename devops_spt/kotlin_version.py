"""Automate management of Kotlin versions"""
from os.path import basename
from subprocess import call, check_output
from urllib.parse import urlparse
from re import match
from requests import get
from external_version import ExternalVersion

class KotlinVersion(ExternalVersion):
    """Concrete class for managing Kotlin dependency versions"""

    @staticmethod
    def existing():
        """Return installed Kotlin version"""
        # shell=True okay in this case, b/c not building the command from user
        #    input
        output = check_output('cat build.gradle.kts' + \
                              ' | grep "^  kotlin(\'jvm\')"' + \
                              ' | sed "s/^  kotlin(\'jvm\') version //"', \
                              shell=True, text=True)
        # eliminate quotes & trailing newline from output, only match the
        #    version
        pattern = match(r'"(.+)"', output)
        return pattern.group(1)

    @staticmethod
    def latest():
        """Return latest Kotlin version available"""
        # Use Requests library to track the redirect, guidance here:
        #    https://bit.ly/2JRvapH
        req = get('https://github.com/JetBrains/kotlin/releases/latest')
        url = urlparse(req.url)
        base = basename(url.path)
        # strip off the leading "v"
        _, rhs = base.split("v", 1)
        return rhs

    @staticmethod
    def update(verbose=False):
        """Update installed Kotlin version to latest if necessary"""
        old = KotlinVersion.existing()
        new = KotlinVersion.latest()
        if verbose:
            print("existing Kotlin ==> " + old)
            print("latest Kotlin   ==> " + new)
        if old == new:
            if verbose:
                print("Kotlin update not necessary")
        else:
            # Guidance: https://stackoverflow.com/a/17141572
            with open('build.gradle.kts', 'r') as infile:
                filedata = infile.read()
            filedata = filedata.replace(old, new)
            # write the same filename out again
            with open('build.gradle.kts', 'w') as outfile:
                outfile.write(filedata)
            call("dos2unix build.gradle.kts", shell=True)
