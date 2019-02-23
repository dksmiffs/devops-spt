"""pytest unit tests for the Directory module"""
from devops_spt import Directory

def test_cd(mocker):
    """unit test Directory.cd"""
    getcwd_mock = mocker.patch('devops_spt.directory.getcwd')
    chdir_mock = mocker.patch('devops_spt.directory.chdir')
    expand_mock = mocker.patch('devops_spt.directory.path.expanduser')
    # Note below that assert_called_once(), assert_called_once_with(), and
    #    resetall() are valid members on the mock, so we ignore pylint E1101
    with Directory.cd('somedir'):
        # pylint:disable-msg=E1101
        getcwd_mock.assert_called_once()
        expand_mock.assert_called_once_with('somedir')
        chdir_mock.assert_called_once()
        mocker.resetall()
    # chdir (back to prev) should've been called on context exit
    chdir_mock.assert_called_once()  # pylint:disable-msg=E1101

    # Same, but raise an exception during the chdir context
    mocker.resetall()
    try:
        with Directory.cd('diffdir'):
            # pylint:disable-msg=E1101
            chdir_mock.assert_called_once()
            mocker.resetall()
            raise RuntimeError('some exception during cd context')
    except RuntimeError:
        pass
    # chdir (back to prev) should've also been called on exception
    chdir_mock.assert_called_once()  # pylint:disable-msg=E1101
