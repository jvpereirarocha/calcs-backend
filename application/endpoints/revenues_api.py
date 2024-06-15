from calendar import monthrange
from datetime import datetime, date
from decimal import Decimal
from flask import Blueprint, jsonify, request
from application.services.token_required_service import token_required
from calculations.domain.aggregates.balance import Balance, StatusBalance
from calculations.domain.entities.revenues import Revenue
from infrastructure.database.repository.balances.balances_repo import BalanceRepo
from libs.types.identifiers import BalanceUUID, RevenueUUID, UserUUID


revenues_blueprint = Blueprint("revenues", __name__, url_prefix="/revenues")


@revenues_blueprint.route("/create", methods=["POST"])
@token_required
def create_new_revenue(user_info):
    data = request.get_json()

    balance_repo = BalanceRepo()

    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    person_id = None
    if person:
        person_id = person.person_id

    current_date = datetime.now()
    month, year = current_date.month, current_date.year
    month_range = monthrange(year, month)
    last_day_of_month = month_range[1]

    date_of_receivment = datetime.strptime(data["dateOfReceivment"], "%d/%m/%Y").date()

    date_as_text = "{}/{}/{}".format(
        date_of_receivment.month, date_of_receivment.day, date_of_receivment.year
    )

    new_revenue = Revenue(
        revenue_id=RevenueUUID(),
        description=data["description"],
        value=Decimal(data["value"]),
        date_of_receivment=date_as_text,
        category=data["category"],
        created_when=datetime.now(),
        modified_when=datetime.now(),
        person_id=person_id,
    )

    balance = None
    if person_id:
        balance = balance_repo.get_balance_by_month_year_and_person(
            month=month, year=year, person_id=person_id
        )

    if balance:
        balance.modified_when = datetime.now()
        if balance.revenues:
            balance.revenues.append(new_revenue)
        else:
            balance.revenues = [new_revenue]

    else:
        balance = Balance(
            balance_id=BalanceUUID(),
            description=f"Balance of {month}/{year}",
            month=month,
            year=year,
            start_date=datetime(year=year, month=month, day=1),
            end_date=datetime(year=year, month=month, day=last_day_of_month),
            total_of_balance=0.0,
            status_balance=StatusBalance.INITIAL.value,
            expenses=[],
            revenues=[new_revenue],
            created_when=datetime.now(),
            modified_when=datetime.now(),
            person_id=person_id,
        )

    balance_repo.save_balance(balance=balance)
    balance_repo.commit()

    return jsonify(data), 201


@revenues_blueprint.route("/update/<string:revenue_id>", methods=["PUT"])
@token_required
def update_revenue(user_info, revenue_id):
    data = request.get_json()
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    date_of_receivment_as_text = data["dateOfReceivment"]
    date_of_receivment = datetime.strptime(
        date_of_receivment_as_text, "%d/%m/%Y"
    ).date()
    date_as_text = "{}/{}/{}".format(
        date_of_receivment.month, date_of_receivment.day, date_of_receivment.year
    )
    revenue_id = RevenueUUID(revenue_id)
    if not person:
        return jsonify({"error": "Usuário não encontrado"}), 404

    balance = balance_repo.get_balance_by_revenue_id_and_person_id(
        revenue_id=revenue_id, person_id=person.person_id
    )

    if not balance:
        return jsonify({"error": "Saldo não encontrado"}), 404

    revenue = balance.get_revenue_by_id(revenue_id=revenue_id)
    if not revenue:
        return jsonify({"error": "Receita não encontrada"}), 404

    revenue = revenue.update_revenue(
        description=data["description"],
        value=Decimal(data["value"]),
        date_of_receivment=date_as_text,
        category=data["category"],
    )

    # at this moment, not commited yet
    balance_repo.save_balance(balance=balance)
    balance_repo.commit()
    return jsonify({"success": f"Receita {revenue.revenue_id} atualizada!"}), 200


@revenues_blueprint.route("/get_all", methods=["GET"])
@token_required
def get_all_revenues_from_user(user_info):
    current_page = args.get("page", None)
    rows_per_page = args.get("rowsPerPage", None)
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    if not person:
        return jsonify({"error": "Usuário não encontrado"}), 404

    if current_page and rows_per_page:
        revenues = balance_repo.get_revenues_by_person_id_limiting_by_rows(
            person_id=person_id,
            current_page=current_page,
            rows_per_page=rows_per_page
        )
    else:
        revenues = balance_repo.get_all_revenues_by_person_id(person_id=person.person_id)

    if not revenues:
        return jsonify({"error": "Nenhuma receita encontrada"}), 404

    revenues = [revenue.to_dict() for revenue in revenues]

    return jsonify(revenues), 200


@revenues_blueprint.route("/remove/<string:revenue_id>", methods=["DELETE"])
@token_required
def remove_revenue(_, revenue_id: str):
    balance_repo = BalanceRepo()
    revenue = balance_repo.get_revenue_by_id(revenue_id=revenue_id)
    if not revenue:
        return jsonify({"error": "Receita Não encontrada"}), 404

    balance_repo.remove_revenue(revenue=revenue)
    balance_repo.commit()

    return jsonify({}), 204
