from ._base import Error


class CoreError(Error):
    """Bot core error"""

class RouterError(CoreError):
    """Router error"""

class UnknownRecorder(RouterError):
    """Unknown recorder for handlers"""
    msg = "Unknown recorder specified"


class RouterDoesNotExist(RouterError):
    """Router was not created in the handler file"""
    msg = "Router not created"