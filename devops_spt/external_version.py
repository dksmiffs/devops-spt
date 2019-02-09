"""External dependency version module"""
from abc import ABC, abstractmethod

class ExternalVersion(ABC):
    """Define interface for managing external dependency versions"""

    @classmethod
    @abstractmethod
    def existing(cls):
        """Return installed version"""

    @classmethod
    @abstractmethod
    def latest(cls):
        """Return latest version available"""

    @classmethod
    @abstractmethod
    def update(cls, verbose=False):
        """Update installed version to latest if necessary"""
