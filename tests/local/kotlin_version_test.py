"""pytest unit tests for the kotlin_version module"""
from devops_spt import KotlinVersion

def test_KotlinVersion_existing(mocker):
    """unit test KotlinVersion.existing"""
    mocker.patch('builtins.open', \
                 mocker.mock_open(read_data='kotlin("jvm") version "4"'))
    version = KotlinVersion.existing()
    assert version == '4'  # nosec

def test_KotlinVersion_latest(mocker):
    """unit test KotlinVersion.latest"""
    getmock = mocker.patch('devops_spt.kotlin_version.get')
    urlmock = mocker.patch('devops_spt.kotlin_version.urlparse')
    basemock = mocker.patch('devops_spt.kotlin_version.basename')
    basemock.return_value ='v8'
    version = KotlinVersion.latest()
    getmock.assert_called_once()
    urlmock.assert_called_once()
    basemock.assert_called_once()
    assert version == '8'  # nosec

def test_KotlinVersion_update_not_needed(mocker):
    """unit test KotlinVersion.update, no update necessary"""
    gvmock = mocker.patch('devops_spt.kotlin_version.KotlinVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '6'
    KotlinVersion.update(verbose=True)
    gvmock.existing.assert_called_once()

def test_KotlinVersion_update_needed(mocker):
    """unit test KotlinVersion.update, update necessary"""
    gvmock = mocker.patch('devops_spt.kotlin_version.KotlinVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '14'
    openmock = mocker.patch('builtins.open', \
                  mocker.mock_open(read_data='kotlin("jvm") version "6"'))
    KotlinVersion.update(verbose=False)
    gvmock.existing.assert_called_once()
    gvmock.latest.assert_called_once()
    assert openmock.call_count == 2
