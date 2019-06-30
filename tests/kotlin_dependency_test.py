"""pytest unit tests for the kotlin_dependency module"""
from devops_spt import KotlinDependency

def test_KotlinDependency_existing(mocker):
    """unit test KotlinDependency.existing"""
    mocker.patch('builtins.open', \
                 mocker.mock_open(read_data='kotlin("jvm") version "4"'))
    dep = KotlinDependency()
    version = dep.existing()
    assert version == '4'  # nosec

def test_KotlinDependency_latest(mocker):
    """unit test KotlinDependency.latest"""
    getmock = mocker.patch('devops_spt.kotlin_dependency.get')
    urlmock = mocker.patch('devops_spt.kotlin_dependency.urlparse')
    basemock = mocker.patch('devops_spt.kotlin_dependency.basename')
    basemock.return_value ='v8'
    dep = KotlinDependency()
    version = dep.latest()
    getmock.assert_called_once()
    urlmock.assert_called_once()
    basemock.assert_called_once()
    assert version == '8'  # nosec

def test_KotlinDependency_update_not_needed(mocker):
    """unit test KotlinDependency.update, no update necessary"""
    dep = KotlinDependency()
    ex = mocker.patch.object(dep, 'existing', return_value='6')
    la = mocker.patch.object(dep, 'latest', return_value='6')
    dep.update(verbose=False)
    ex.assert_called_once()
    la.assert_called_once()

def test_KotlinDependency_update_needed(mocker):
    """unit test KotlinDependency.update, update necessary"""
    dep = KotlinDependency()
    ex = mocker.patch.object(dep, 'existing', return_value='6')
    la = mocker.patch.object(dep, 'latest', return_value='14')
    openmock = mocker.patch('builtins.open', \
                  mocker.mock_open(read_data='kotlin("jvm") version "6"'))
    dep.update(verbose=False)
    ex.assert_called_once()
    la.assert_called_once()
    assert openmock.call_count == 2  # nosec
