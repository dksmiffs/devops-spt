"""Automate management of Gradle versions"""
from re import MULTILINE, search
from json import loads
from platform import system
from subprocess import PIPE, run
from urllib.request import urlopen
from external_version import ExternalVersion

class GradleVersion(ExternalVersion):
    """Concrete class for managing Gradle dependency versions"""

    # class properties
    _platform = system()
    _gradle_cmd = 'gradlew.bat' if _platform == 'Windows' else 'gradlew'

    @classmethod
    def existing(cls):
        """Return installed Gradle version"""
        output = run(args=[cls._gradle_cmd, '-v'], shell=False, \
                     text=True, stdout=PIPE).stdout
        version = search('^Gradle (.+)$', output, MULTILINE)
        return version.group(1)

    @classmethod
    def latest(cls):
        """Return latest Gradle version available"""
        # Codacy raises B310 on the following line, but appears to have issue
        #    with legacy urllib.urlopen, NOT urllib.request.urlopen.  Also, no
        #    concerns with this usage raised from a reading of the following:
        #       https://docs.python.org/3/library/urllib.request.html
        with urlopen('https://services.gradle.org/versions/current')\
                as url:
            full_json = loads(url.read().decode())
            # json parsing guidance: https://stackoverflow.com/a/7771071
            return full_json['version']

    @classmethod
    def update(cls, verbose=False):
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
            run(args=[cls._gradle_cmd, 'wrapper', '--gradle-version', new, \
                      '--distribution-type', 'bin'], shell=False)
