from flask import Blueprint, jsonify

from application.services.token_required_service import token_required
from infrastructure.database.repository.balances.balances_repo import BalanceRepo
from libs.types.identifiers import UserUUID


balances_blueprint = Blueprint("balances", __name__, url_prefix="/balances")


@balances_blueprint.route(
    "/get_balance_of_month/<string:month_and_year>", methods=["GET"]
)
@token_required
def get_total_balance_of_month_and_year(user_info, month_and_year):
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    if not person:
        return jsonify({"message": "Usuário não encontrado"}), 404

    month, year = month_and_year.split("_")
    balance = balance_repo.get_balance_by_month_year_and_person(
        month=int(month), year=int(year), person_id=person.person_id
    )
    if not balance:
        return jsonify({"message": "Saldo não encontrado"}), 404

    month_balance = balance.month_balance
    response = {"message": f"R$ {month_balance}"}
    return jsonify(response), 200
