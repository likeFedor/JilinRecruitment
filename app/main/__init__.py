from flask import Blueprint
#第二步 配置蓝本
main = Blueprint('main', __name__)
#把views导入进来
from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
