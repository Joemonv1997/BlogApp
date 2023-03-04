import sys
import os
from flask import make_response,request,jsonify
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"common"))
from app_blueprint import AppBlueprint
from app_response import AppResponse
from string_table import AppMessages
from app_constants import AppConstants
home_blueprint=AppBlueprint("home",__name__)


@home_blueprint.route("/",methods=["GET"])
def home():
    app_response=AppResponse()
    app_response.set_response(
        code_param=AppConstants.CODE_OK, 
        data_param={"hello":"App Successfully Build"}, 
        message_param=AppMessages.OPERATION_SUCCESS, 
        status_param=AppConstants.SUCCESSFULL_STATUS_CODE)
    return make_response(jsonify(app_response),200)