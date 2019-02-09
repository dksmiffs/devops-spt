"""pytest unit tests for the cd module"""
from cd import chdir
import os

def test_chdir(mocker):
    """unit test cd.chdir"""
    mocker.patch('os.getcwd')
    mocker.patch('os.chdir')
    mocker.patch('os.path.expanduser')
    # Note below that assert_called_once(), assert_called_once_with(), and
    #    resetall() are valid members on the mock, so we ignore pylint E1101
    with chdir('somedir'):
        # pylint:disable-msg=E1101
        os.getcwd.assert_called_once()
        os.path.expanduser.assert_called_once_with('somedir')
        os.chdir.assert_called_once()
        mocker.resetall()
    # chdir should be called once more upon context exit
    os.chdir.assert_called_once()  # pylint:disable-msg=E1101
