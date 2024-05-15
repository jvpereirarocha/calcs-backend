from datetime import datetime
from decimal import Decimal
from flask import Blueprint, jsonify, request
from calculations.domain.aggregates.balance import Balance, StatusBalance

from calculations.domain.entities.expenses import Expense
from infrastructure.database.repository.balances.balances_repo import BalanceRepo
from libs.types.identifiers import BalanceUUID, ExpenseUUID, UserUUID
from application.services.token_required_service import token_required
from calendar import monthrange


expenses_blueprint = Blueprint("expenses", __name__, url_prefix="/expenses")


@expenses_blueprint.route("/create", methods=["POST"])
@token_required
def create_new_expense(user_info):
    # firstly we'll try to persist the expense
    # if it's ok, we'll refactor the code
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

    due_date = datetime.strptime(data["dueDate"], "%d/%m/%Y").date()
    due_date_as_text = "{}/{}/{}".format(due_date.day, due_date.month, due_date.year)

    already_paid = data.get("alreadyPaid", False)

    new_expense = Expense(
        expense_id=ExpenseUUID(),
        description=data["description"],
        value=data["value"],
        due_date=due_date_as_text,
        category=data["category"],
        already_paid=already_paid,
        created_when=datetime.now(),
        modified_when=datetime.now(),
        person_id=person_id,
    )
    # not committed yet
    balance = None
    if person_id:
        balance = balance_repo.get_balance_by_month_year_and_person(
            month=month, year=year, person_id=person_id
        )

    if balance:
        balance.modified_when = datetime.now()
        if balance.expenses:
            balance.expenses.append(new_expense)
        else:
            balance.expenses = [new_expense]
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
            person_id=person_id,
        )

    # adding expense to save
    balance_repo.save_balance(balance=balance)
    balance_repo.commit()

    return jsonify(data), 201


@expenses_blueprint.route("/update/<string:expense_id>", methods=["PUT"])
@token_required
def update_expense(user_info, expense_id):
    data = request.get_json()
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    expense_id = ExpenseUUID(expense_id)
    if not person:
        return jsonify({"error": "Usuário não encontrado"}), 404

    balance = balance_repo.get_balance_by_expense_id_and_person_id(
        expense_id=expense_id, person_id=person.person_id
    )

    due_date = datetime.strptime(data["dueDate"], "%d/%m/%Y").date()
    due_date_as_text = "{}/{}/{}".format(due_date.day, due_date.month, due_date.year)

    if not balance:
        return jsonify({"error": "Saldo não encontrado"}), 404

    expense = balance.get_expense_by_id(expense_id=expense_id)
    if not expense:
        return jsonify({"error": "Despesa não encontrada"}), 404

    expense = expense.update_expense(
        description=data["description"],
        value=float(data["value"]),
        due_date=due_date_as_text,
        already_paid=data["alreadyPaid"],
        category=data["category"],
    )

    # at this moment, not commited yet
    balance_repo.save_balance(balance=balance)
    balance_repo.update_balance(balance=balance)  # updating balance total value
    balance_repo.commit()
    return jsonify({"success": f"Despesa {expense.expense_id} atualizada!"}), 200


@expenses_blueprint.route("/get_expense/<string:expense_id>", methods=["GET"])
@token_required
def fetch_one_expense(user_info, expense_id):
    expense_id = ExpenseUUID(expense_id)
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    if not person:
        return jsonify({"error": "Usuário não encontrado"}), 404

    balance = balance_repo.get_balance_by_expense_id_and_person_id(
        expense_id=expense_id, person_id=person.person_id
    )

    if not balance:
        return jsonify({"error": "Saldo não encontrado"}), 404
    
    expense = balance.get_expense_by_id(expense_id=expense_id)
    if not expense:
        return jsonify({"error": "Despesa não encontrada"}), 404
    
    return jsonify({
        "success": expense.to_dict(amount_as_decimal=True)
    })


@expenses_blueprint.route("/get_all", methods=["GET"])
@token_required
def get_all_expenses_from_user(user_info):
    user_id = UserUUID.parse_to_user_uuid(user_id_as_string=user_info["user_id"])
    balance_repo = BalanceRepo()
    person = balance_repo.get_person_by_user_id(user_id=user_id)
    if not person:
        return jsonify({"error": "Usuário não encontrado"}), 404

    expenses = balance_repo.get_all_expenses_by_person_id(person_id=person.person_id)
    if not expenses:
        return jsonify({"error": "Nenhuma despesa encontrada"}), 404

    expenses = [expense.to_dict() for expense in expenses]

    return jsonify(expenses), 200


@expenses_blueprint.route("/remove/<string:expense_id>", methods=["DELETE"])
@token_required
def remove_expense(_, expense_id: str):
    balance_repo = BalanceRepo()
    expense = balance_repo.get_expense_by_id(expense_id=expense_id)
    if not expense:
        return jsonify({"error": "Despesa Não encontrada"}), 404

    balance_repo.remove_expense(expense=expense)
    balance_repo.commit()

    return jsonify({}), 204
