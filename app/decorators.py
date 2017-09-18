from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

#decorated 1、构建方法 def function :def decorator(f):@wraps()def funtion2():return f() return function2 return decorator
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

#返回一个function 的function 就可以用作装饰器
def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
