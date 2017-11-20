class InvalidInputException(Exception):
    """Exception to record invalid input"""
    pass


class NotFoundException(Exception):
    """Exception to record data not found"""
    pass


class ConnectionErrorException(Exception):
    """Exception to record connection error to API"""
    pass
