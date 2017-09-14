from flask import Blueprint
#�ڶ��� ��������
main = Blueprint('main', __name__)
#��views�������
from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)