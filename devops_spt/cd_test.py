"""pytest unit tests for the cd module"""
import os
from . import cd

def test_chdir(mocker):
    """unit test cd.chdir"""
    mocker.patch('os.getcwd')
    mocker.patch('os.chdir')
    mocker.patch('os.path.expanduser')
    # Note below that assert_called_once(), assert_called_once_with(), and
    #    resetall() are valid members on the mock, so we ignore pylint E1101
    with cd.chdir('somedir'):
        # pylint:disable-msg=E1101
        os.getcwd.assert_called_once()
        os.path.expanduser.assert_called_once_with('somedir')
        os.chdir.assert_called_once()
        mocker.resetall()
    # chdir (back to prev) should've been called on context exit
    os.chdir.assert_called_once()  # pylint:disable-msg=E1101

    # Same, but raise an exception during the chdir context
    mocker.resetall()
    try:
        with cd.chdir('diffdir'):
            # pylint:disable-msg=E1101
            os.chdir.assert_called_once()
            mocker.resetall()
            raise RuntimeError('some exception during chdir context')
    except RuntimeError:
        pass
    # chdir (back to prev) should've also been called on exception
    os.chdir.assert_called_once()  # pylint:disable-msg=E1101
