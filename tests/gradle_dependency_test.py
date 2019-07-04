"""pytest unit tests for the gradle_dependency module"""
from devops_spt import GradleDependency


def test_GradleDependency_existing(mocker):
    """unit test GradleDependency.existing"""
    runmock = mocker.patch('devops_spt.gradle_dependency.run')
    runmock.return_value.stdout = 'Gradle 0.9.8'
    dep = GradleDependency()
    version = dep.existing()
    runmock.assert_called_once()
    assert version == '0.9.8'  # nosec


def test_GradleDependency_latest(mocker):
    """unit test GradleDependency.latest"""
    getmock = mocker.patch('devops_spt.gradle_dependency.get')
    loadsmock = mocker.patch('devops_spt.gradle_dependency.loads')
    loadsmock.return_value = {'version': '18'}
    dep = GradleDependency()
    version = dep.latest()
    getmock.assert_called_once()
    loadsmock.assert_called_once()
    assert version == '18'  # nosec


def test_GradleDependency_update_not_needed(mocker):
    """unit test GradleDependency.update, no update necessary"""
    dep = GradleDependency()
    ex = mocker.patch.object(dep, 'existing', return_value='6')
    la = mocker.patch.object(dep, 'latest', return_value='6')
    dep.update(verbose=False)
    ex.assert_called_once()
    la.assert_called_once()


def test_GradleDependency_update_needed(mocker):
    """unit test GradleDependency.update, update necessary"""
    dep = GradleDependency()
    ex = mocker.patch.object(dep, 'existing', return_value='6')
    la = mocker.patch.object(dep, 'latest', return_value='14')
    runmock = mocker.patch('devops_spt.gradle_dependency.run')
    dep.update(verbose=False)
    ex.assert_called_once()
    la.assert_called_once()
    runmock.assert_called_once()
