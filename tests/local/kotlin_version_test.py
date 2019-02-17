"""pytest unit tests for the kotlin_version module"""
from devops_spt import KotlinVersion

def test_KotlinVersion_existing(mocker):
    """unit test KotlinVersion.existing"""
    mocker.patch('builtins.open', \
                 mocker.mock_open(read_data='kotlin("jvm") version "4"'))
    version = KotlinVersion.existing()
    assert version == '4'  # nosec

#def test_KotlinVersion_latest(mocker):
#    """unit test KotlinVersion.latest"""
#    getmock = mocker.patch('devops_spt.kotlin_version.get')
#    loadsmock = mocker.patch('devops_spt.kotlin_version.loads')
#    loadsmock.return_value = {'version': '18'}
#    version = KotlinVersion.latest()
#    getmock.assert_called_once()
#    loadsmock.assert_called_once()
#    assert version == '18'  # nosec
#
#def test_KotlinVersion_update_not_needed(mocker):
#    """unit test KotlinVersion.update, no update necessary"""
#    gvmock = mocker.patch('devops_spt.kotlin_version.KotlinVersion')
#    gvmock.existing.return_value = '6'
#    gvmock.latest.return_value = '6'
#    KotlinVersion.update(verbose=True)
#    gvmock.existing.assert_called_once()
#
#def test_KotlinVersion_update_needed(mocker):
#    """unit test KotlinVersion.update, update necessary"""
#    gvmock = mocker.patch('devops_spt.kotlin_version.KotlinVersion')
#    gvmock.existing.return_value = '6'
#    gvmock.latest.return_value = '14'
#    runmock = mocker.patch('devops_spt.kotlin_version.run')
#    KotlinVersion.update(verbose=False)
#    gvmock.existing.assert_called_once()
#    runmock.assert_called_once()
