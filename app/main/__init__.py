# subpackage in the main package
from flask import Blueprint

main = Blueprint('main', __name__)

# always imported at the end of the script
# this is to avoid the circular dependencies
from . import views, errors