from datetime import datetime
from flask import Blueprint, jsonify, request
from calculations.domain.aggregates.balance import Balance, StatusBalance

from calculations.domain.entities.expenses import Expense
from infrastructure.database.repository.balances.balances_repo import BalanceRepo
from libs.types.identifiers import BalanceUUID, ExpenseUUID
from calendar import monthrange


expenses_blueprint = Blueprint("expenses", __name__, url_prefix="/expenses")


@expenses_blueprint.route("/create", methods=["POST"])
def create_new_expense():
    # firstly we'll try to persist the expense
    # if it's ok, we'll refactor the code
    data = request.get_json()

    current_date = datetime.now()
    month, year = current_date.month, current_date.year

    month_range = monthrange(year, month)
    last_day_of_month = month_range[1]

    new_expense = Expense(
        expense_id=ExpenseUUID(),
        description=data["description"],
        value=data["value"],
        due_date=data["dueDate"],
        category=data["category"],
        already_paid=data["alreadyPaid"],
        created_when=datetime.now(),
        modified_when=datetime.now(),
    )
    # not committed yet

    balance_repo = BalanceRepo()
    balance = balance_repo.get_balance_by_month_and_year(month=month, year=year)

    if balance:
        balance.modified_when = datetime.now()
        if balance.expenses:
            balance.expenses.append(new_expense)
        else:
            balance.expenses = [new_expense]

        balance_repo.save_balance(balance=balance)
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
            expenses=[new_expense],
            revenues=[],
            created_when=datetime.now(),
            modified_when=datetime.now(),
        )

    # adding expense to save
    balance_repo.save_balance(balance=balance)
    balance_repo.commit()

    return jsonify(data), 201
