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

def test_GradleVersion_update_not_needed(mocker):
    """unit test GradleVersion.update, no update necessary"""
    gvmock = mocker.patch('devops_spt.gradle_version.GradleVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '6'
    GradleVersion.update(verbose=True)
    gvmock.existing.assert_called_once()

def test_GradleVersion_update_needed(mocker):
    """unit test GradleVersion.update, update necessary"""
    gvmock = mocker.patch('devops_spt.gradle_version.GradleVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '14'
    runmock = mocker.patch('devops_spt.gradle_version.run')
    GradleVersion.update(verbose=False)
    gvmock.existing.assert_called_once()
    runmock.assert_called_once()
