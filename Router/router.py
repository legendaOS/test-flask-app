from flask import Blueprint
from .Controller_v1 import controller

router = Blueprint('router', __name__)

@router.get('/')
def test():
    return controller.test()