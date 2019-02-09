"""Automate management of Gradle versions"""
from re import match
from json import loads
from subprocess import call, check_output
from urllib.request import urlopen
from external_version import ExternalVersion

class GradleVersion(ExternalVersion):
    """Concrete class for managing Gradle dependency versions"""

    @staticmethod
    def existing():
        """Return installed Gradle version"""
        # shell=True okay in this case, b/c not building the command from user
        #    input
        output = check_output('gradlew -v | grep "^Gradle" ' + \
                              '| sed "s/^Gradle //"', shell=True, text=True)
        # eliminate the trailing newline from output, only match the version
        pattern = match(r'(.+)', output)
        return pattern.group(1)

    @staticmethod
    def latest():
        """Return latest Gradle version available"""
        with urlopen("https://services.gradle.org/versions/current")\
                as url:
            full_json = loads(url.read().decode())
            # json parsing guidance: https://stackoverflow.com/a/7771071
            return full_json['version']

    @staticmethod
    def update(verbose=False):
        """Update installed Gradle version to latest if necessary"""
        old = GradleVersion.existing()
        new = GradleVersion.latest()
        if verbose:
            print("existing Gradle ==> " + old)
            print("latest Gradle   ==> " + new)
        if old == new:
            if verbose:
                print("Gradle update not necessary")
        else:
            # Gradle update guidance:
            #    blog.nishtahir.com/2018/04/15/
            #       how-to-properly-update-the-gradle-wrapper
            call("gradlew wrapper --gradle-version " + new + \
                 " --distribution-type bin", shell=True)
