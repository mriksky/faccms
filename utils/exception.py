from rest_framework import status
from rest_framework.exceptions import APIException as DRFAPIException
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError


class APIException(DRFAPIException):
    """自定义异常增加错误状态码"""
    def __init__(self, detail=None, code=None, status_code=status.HTTP_400_BAD_REQUEST):
        super().__init__(detail, code)
        APIException.status_code = status_code

# class PermissionsException(PermissionDenied):
#     """自定义403权限异常增加错误状态码"""
#     def __init__(self, detail=None, code=None, status_code=status.HTTP_403_FORBIDDEN):
#         super().__init__(detail, code)
#         PermissionsException.status_code = status_code
#
# class ValidationErrorException(ValidationError):
#     """校验参数异常"""
#     def __init__(self, detail=None, code=None, status_code=status.HTTP_400_BAD_REQUEST):
#         super().__init__(detail, code)
#         ValidationErrorException.status_code = status_code