"""pytest unit tests for the gradle_version module"""
from devops_spt import GradleVersion

def test_GradleVersion_existing(mocker):
    """unit test GradleVersion.existing"""
    runmock = mocker.patch('devops_spt.gradle_version.run')
    runmock.return_value.stdout = 'Gradle 0.9.8'
    version = GradleVersion.existing()
    runmock.assert_called_once()
    assert version == '0.9.8'  # nosec

def test_GradleVersion_latest(mocker):
    """unit test GradleVersion.latest"""
    getmock = mocker.patch('devops_spt.gradle_version.get')
    loadsmock = mocker.patch('devops_spt.gradle_version.loads')
    loadsmock.return_value = {'version': '18'}
    version = GradleVersion.latest()
    getmock.assert_called_once()
    loadsmock.assert_called_once()
    assert version == '18'  # nosec
