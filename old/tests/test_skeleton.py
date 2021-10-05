import pytest
import logging
from video_test.skeleton import fib, main
from video_test.vid import test_eggs
from video_test.vid import run_process

__author__ = "Alex Ethier"
__copyright__ = "Alex Ethier"
__license__ = "MIT"

LOGGER = logging.getLogger(__name__)

def test_vid():
    test_eggs()
    assert True

def test_process():
    run_process()
    assert True

def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True

def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests"""

    print("Test Main")

    # capsys is a pytest fixture that allows asserts agains stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["7"])
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out
