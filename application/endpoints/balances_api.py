from datetime import datetime
from flask import Blueprint, jsonify, request

from application.services.token_required_service import token_required
from calculations.domain.aggregates.balance import Balance
from infrastructure.database.repository.balances.balances_repo import BalanceRepo
from libs.types.identifiers import UserUUID


balances_blueprint = Blueprint("balances", __name__, url_prefix="/balances")


@balances_blueprint.route("/get_monthly_balance/", methods=["GET"])
@token_required
def get_total_balance_of_month(user_info):
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    now = datetime.now()
    if not person:
        return jsonify({"message": "Usuário não encontrado"}), 404

    balance = balance_repo.get_balance_by_month_year_and_person(
        month=int(now.month), year=int(now.year), person_id=person.person_id
    )

    response = {
        "success": {
            "expenses": f"R$ 0,00",
            "revenues": f"R$ 0,00",
            "balance": f"R$ 0,00",
        }
    }

    if not balance:
        return jsonify(response), 200

    month_balance = str(balance.month_balance).replace(".", ",")
    month_revenues = str(balance.revenues_amount).replace(".", ",")
    month_expenses = str(balance.expenses_amount).replace(".", ",")
    response = {
        "success": {
            "expenses": f"R$ {month_expenses}",
            "revenues": f"R$ {month_revenues}",
            "balance": f"R$ {month_balance}",
        }
    }
    return jsonify(response), 200


@balances_blueprint.route("/get_yearly_balance/", methods=["GET"])
@token_required
def get_total_balance_of_year(user_info):
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    now = datetime.now()
    if not person:
        return jsonify({"message": "Usuário não encontrado"}), 404

    balances = list(
        balance_repo.get_all_balances_from_year_and_person(
            year=int(now.year), person_id=person.person_id
        )
    )
    response = {
        "success": {
            "expenses": f"R$ 0,00",
            "revenues": f"R$ 0,00",
            "balance": f"R$ 0,00",
        }
    }

    if not balances:
        return jsonify(response), 200

    year_balance = str(
        Balance.sum_all_balances_from_list_of_balances(balances=balances)
    ).replace(".", ",")
    year_revenues = str(
        Balance.sum_all_revenues_from_list_of_balances(balances=balances)
    ).replace(".", ",")
    year_expenses = str(
        Balance.sum_all_expenses_from_list_of_balances(balances=balances)
    ).replace(".", ",")
    response = {
        "success": {
            "expenses": f"R$ {year_expenses}",
            "revenues": f"R$ {year_revenues}",
            "balance": f"R$ {year_balance}",
        }
    }
    return jsonify(response), 200


@balances_blueprint.route("/get_last_transactions", methods=["GET"])
@token_required
def get_last_transactions(user_info):
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    args = request.args
    number_of_transactions = args.get(
        "numberOfTransactions", 5
    )  # per default, 5 transactions
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    now = datetime.now()
    if not person:
        return jsonify({"message": "Usuário não encontrado"}), 404

    balance = balance_repo.get_balance_by_month_year_and_person(
        month=int(now.month), year=int(now.year), person_id=person.person_id
    )

    if not balance:
        return jsonify({"message": "Balanço não encontrado"}), 200

    last_transactions = list(
        balance.get_last_transactions(number_of_transactions=number_of_transactions)
    )
    if last_transactions:
        responses = []
        for transaction in last_transactions:
            current_response = Balance.format_response_to_transaction(
                transaction=transaction
            )
            responses.append(current_response)

        amount_of_transactions = Balance.calculate_total_of_transactions(transactions=last_transactions)
        response = {"success": {"lastTransactions": responses, "amount": "R$: {02:f}, {02:f}".format(amount_of_transactions)}}
    else:
        response = {"success": {"lastTransactions": [], "amount": "R$ 0,00"}}

    return jsonify(response), 200
