"""pytest unit tests for the gradle_version module"""
from subprocess import CompletedProcess
from devops_spt import GradleVersion

def test_GradleVersion_existing(mocker):
    """unit test GradleVersion.existing"""
    def run_side_effect():
        effect = CompletedProcess('', 0)
        #effect.stdout = mocker.MagicMock(return_value='line1\nGradle 0.9.8\n')
        effect.stdout = 'line1\nGradle 0.9.8\n'
        return effect
    # patch subprocess.run with desired side effect for testing
    runmock = mocker.patch('subprocess.run')
    runmock.side_effect = run_side_effect()
    # Now test the remaining portions of the existing() method
#
# The following is not yet working
#
#    version = GradleVersion.existing()
#    subprocess.run.assert_called_with(shell=False, text=True, \
#                                      stdout=subprocess.PIPE)
#    subprocess.run.assert_called_with( \
#        argv=['gradlew.bat' if system() == 'Windows' else 'gradlew', '-v'])
#    assert version == '0.9.8'
