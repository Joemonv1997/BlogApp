import sys
import os
from flask import make_response, request, jsonify

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "common",
    )
)
from app_blueprint import AppBlueprint
from app_response import AppResponse
from string_table import AppMessages
from app_constants import AppConstants

auth_blueprint = AppBlueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["GET,POST"])
def login_request():
    app_response = AppResponse()
    app_response.set_response(
        code_param=AppConstants.CODE_OK,
        data_param={"Success": "User Successfully LoggedInn"},
        message_param=AppMessages.OPERATION_SUCCESS,
        status_param=AppConstants.SUCCESSFULL_STATUS_CODE,
    )
    return make_response(jsonify(app_response), 200)


@auth_blueprint.route("/register", methods=["GET,POST"])
def register_request():
    app_response = AppResponse()
    app_response.set_response(
        code_param=AppConstants.CODE_OK,
        data_param={"Success": "User Successfully Registered"},
        message_param=AppMessages.OPERATION_SUCCESS,
        status_param=AppConstants.SUCCESSFULL_STATUS_CODE,
    )
    return make_response(jsonify(app_response), 200)
