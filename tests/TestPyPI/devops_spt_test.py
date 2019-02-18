""" pytest unit tests for the TestPyPI importable package"""
from devops_spt import chdir, GradleVersion, KotlinVersion

def test_chdir(mocker):
    """unit test devops_spt.chdir"""
    mocker.patch('devops_spt.os.getcwd')
    mocker.patch('devops_spt.os.chdir')
    mocker.patch('devops_spt.os.path.expanduser')
    with devops_spt.chdir('somedir'):
        # pylint:disable-msg=E1101
        devops_spt.os.getcwd.assert_called_once()
        devops_spt.os.path.expanduser.assert_called_once_with('somedir')
        devops_spt.os.chdir.assert_called_once()
        mocker.resetall()
    # chdir (back to prev) should've been called on context exit
    devops_spt.os.chdir.assert_called_once()  # pylint:disable-msg=E1101

    # Same, but raise an exception during the chdir context
    mocker.resetall()
    try:
        with devops_spt.chdir('diffdir'):
            # pylint:disable-msg=E1101
            devops_spt.os.chdir.assert_called_once()
            mocker.resetall()
            raise RuntimeError('some exception during chdir context')
    except RuntimeError:
        pass
    # chdir (back to prev) should've also been called on exception
    devops_spt.os.chdir.assert_called_once()  # pylint:disable-msg=E1101

def test_GradleVersion_existing(mocker):
    """unit test devops_spt.GradleVersion.existing"""
    runmock = mocker.patch('devops_spt.gradle_version.run')
    runmock.return_value.stdout = 'Gradle 0.9.8'
    version = GradleVersion.existing()
    runmock.assert_called_once()
    assert version == '0.9.8'  # nosec

def test_GradleVersion_latest(mocker):
    """unit test devops_spt.GradleVersion.latest"""
    getmock = mocker.patch('devops_spt.gradle_version.get')
    loadsmock = mocker.patch('devops_spt.gradle_version.loads')
    loadsmock.return_value = {'version': '18'}
    version = GradleVersion.latest()
    getmock.assert_called_once()
    loadsmock.assert_called_once()
    assert version == '18'  # nosec

def test_GradleVersion_update_not_needed(mocker):
    """unit test devops_spt.GradleVersion.update, no update necessary"""
    gvmock = mocker.patch('devops_spt.gradle_version.GradleVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '6'
    GradleVersion.update(verbose=True)
    gvmock.existing.assert_called_once()

def test_GradleVersion_update_needed(mocker):
    """unit test devops_spt.GradleVersion.update, update necessary"""
    gvmock = mocker.patch('devops_spt.gradle_version.GradleVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '14'
    runmock = mocker.patch('devops_spt.gradle_version.run')
    GradleVersion.update(verbose=False)
    gvmock.existing.assert_called_once()
    runmock.assert_called_once()

def test_KotlinVersion_existing(mocker):
    """unit test devops_spt.KotlinVersion.existing"""
    mocker.patch('builtins.open', \
                 mocker.mock_open(read_data='kotlin("jvm") version "4"'))
    version = KotlinVersion.existing()
    assert version == '4'  # nosec

def test_KotlinVersion_latest(mocker):
    """unit test devops_spt.KotlinVersion.latest"""
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
    """unit test devops_spt.KotlinVersion.update, no update necessary"""
    gvmock = mocker.patch('devops_spt.kotlin_version.KotlinVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '6'
    KotlinVersion.update(verbose=True)
    gvmock.existing.assert_called_once()

def test_KotlinVersion_update_needed(mocker):
    """unit test devops_spt.KotlinVersion.update, update necessary"""
    gvmock = mocker.patch('devops_spt.kotlin_version.KotlinVersion')
    gvmock.existing.return_value = '6'
    gvmock.latest.return_value = '14'
    openmock = mocker.patch('builtins.open', \
                  mocker.mock_open(read_data='kotlin("jvm") version "6"'))
    KotlinVersion.update(verbose=False)
    gvmock.existing.assert_called_once()
    gvmock.latest.assert_called_once()
    assert openmock.call_count == 2  # nosec
