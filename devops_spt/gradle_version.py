"""Automate management of Gradle versions"""
from re import MULTILINE, search
from json import loads
from platform import system
from subprocess import PIPE, run
from requests import get
from external_version import ExternalVersion

class GradleVersion(ExternalVersion):
    """Concrete class for managing Gradle dependency versions"""

    @staticmethod
    def existing():
        """Return installed Gradle version"""
        output = run(['gradlew.bat' if system() == 'Windows' else 'gradlew', \
                      '-v'], shell=False, text=True, stdout=PIPE).stdout
        version = search('^Gradle (.+)$', output, MULTILINE)
        return version.group(1)

    @staticmethod
    def latest():
        """Return latest Gradle version available"""
        req = get('https://services.gradle.org/versions/current')
        full_json = loads(req.content.decode())
        # json parsing guidance: https://stackoverflow.com/a/7771071
        return full_json['version']

    @staticmethod
    def update(verbose=False):
        """Update installed Gradle version to latest if necessary"""
        old = GradleVersion.existing()
        new = GradleVersion.latest()
        if verbose:
            print('existing Gradle ==> ' + old)
            print('latest Gradle   ==> ' + new)
        if old == new:
            if verbose:
                print('Gradle update not necessary')
        else:
            # Gradle update guidance:
            #    blog.nishtahir.com/2018/04/15/
            #       how-to-properly-update-the-gradle-wrapper
            run(args=['gradlew.bat' if system() == 'Windows' else 'gradlew', \
                      'wrapper', '--gradle-version', new, \
                      '--distribution-type', 'bin'], \
                shell=False)
