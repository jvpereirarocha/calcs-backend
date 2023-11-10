from typing import List
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
from calculations.domain.entities.models import InheritedModel
from infrastructure.database.orms.orm_accounts import accounts
from infrastructure.database.orms.orm_balance import balances
from infrastructure.database.orms.orm_expenses import expenses
from infrastructure.database.orms.orm_persons import persons
from infrastructure.database.orms.orm_revenues import revenues
from infrastructure.database.orms.orm_users import users
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.person import Person
from calculations.domain.entities.revenues import Revenue
from calculations.domain.entities.user import User

mapper_registry = registry()


def start_mappers():
    print("Init the mappers")
    accounts_mapper = mapper_registry.map_imperatively(
        Account,
        accounts,
        properties={
            "account_id": accounts.c.id,
            "number_of_account": accounts.c.number_of_account,
            "amount": accounts.c.amount,
            "person": relationship(
                Person, back_populates="accounts", order_by=persons.c.id
            ),
        },
    )

    mapper_registry.map_imperatively(
        User,
        users,
        properties={
            "user_id": users.c.id,
            "email": users.c.email,
            "password_hash": users.c.password_hash,
            "password_salt": users.c.password_salt,
            "avatar": users.c.avatar,
            "person": relationship(Person, backref="user", order_by=persons.c.id),
        },
    )

    expenses_mapper = mapper_registry.map_imperatively(
        Expense,
        expenses,
        properties={
            "expense_id": expenses.c.id,
            "description": expenses.c.description,
            "value": expenses.c.value,
            "due_date": expenses.c.due_date,
            "already_paid": expenses.c.already_paid,
            "category": expenses.c.category,
            "balance": relationship(
                Balance, back_populates="expenses", order_by=expenses.c.id
            ),
        },
    )

    revenues_mapper = mapper_registry.map_imperatively(
        Revenue,
        revenues,
        properties={
            "revenue_id": revenues.c.id,
            "description": revenues.c.description,
            "value": revenues.c.value,
            "date_receivment": revenues.c.date_of_receivment,
            "category": revenues.c.category,
            "balance": relationship(
                Balance, back_populates="revenues", order_by=revenues.c.id
            ),
        },
    )

    balances_mapper = mapper_registry.map_imperatively(
        Balance,
        balances,
        properties={
            "balance_id": balances.c.id,
            "description": balances.c.description,
            "month": balances.c.month,
            "year": balances.c.year,
            "start_date": balances.c.start_date,
            "end_date": balances.c.end_date,
            "total_of_balance": balances.c.total_of_balance,
            "status_balance": balances.c.status_balance,
            "expenses": relationship(
                expenses_mapper,
                back_populates="balance",
                lazy="selectin",
                order_by=expenses.c.id,
            ),
            "revenues": relationship(
                revenues_mapper,
                back_populates="balance",
                lazy="selectin",
                order_by=revenues.c.id,
            ),
            "person": relationship(
                Person, back_populates="balances", order_by=persons.c.id
            ),
        },
    )

    mapper_registry.map_imperatively(
        Person,
        persons,
        properties={
            "person_id": persons.c.id,
            "first_name": persons.c.first_name,
            "last_name": persons.c.last_name,
            "date_of_birth": persons.c.date_of_birth,
            "accounts": relationship(
                accounts_mapper,
                back_populates="person",
                lazy="selectin",
                order_by=accounts.c.id,
            ),
            "balances": relationship(
                balances_mapper,
                back_populates="person",
                lazy="selectin",
                order_by=balances.c.id,
            ),
        },
    )
