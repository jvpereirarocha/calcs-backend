from calendar import monthrange
from datetime import datetime, date
from decimal import Decimal
from flask import Blueprint, jsonify, request
from application.requests.revenues import CreateOrUpdateRevenue

from application.services.token_required_service import token_required
from calculations.domain.aggregates.balance import Balance, StatusBalance
from calculations.domain.entities.revenues import Revenue
from infrastructure.database.repository.balances.balances_repo import BalanceRepo
from libs.types.identifiers import BalanceUUID, RevenueUUID, UserUUID


revenues_blueprint = Blueprint("revenues", __name__, url_prefix="/revenues")


@revenues_blueprint.route("/create", methods=["POST"])
@token_required
def create_new_revenue(user_info):
    import ipdb

    ipdb.set_trace()
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

    date_to_save_as_text = (
        f"{date_of_receivment.month}/{date_of_receivment.day}/{date_of_receivment.year}"
    )

    new_revenue = Revenue(
        revenue_id=RevenueUUID(),
        description=data["description"],
        value=Decimal(data["value"]),
        date_of_receivment=date_to_save_as_text,
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