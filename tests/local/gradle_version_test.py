"""pytest unit tests for the gradle_version module"""
from devops_spt import GradleVersion

def test_GradleVersion_existing(mocker):
    """unit test GradleVersion.existing"""
    # patch subprocess.run with desired side effect for testing
    runmock = mocker.patch('devops_spt.gradle_version.run')
    runmock.return_value.stdout = 'Gradle 0.9.8'
    version = GradleVersion.existing()
    runmock.assert_called_once()
    assert version == '0.9.8'
