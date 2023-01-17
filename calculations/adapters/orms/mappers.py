from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
from calculations.adapters.orms.orm_accounts import accounts
from calculations.adapters.orms.orm_balance import balances
from calculations.adapters.orms.orm_expenses import expenses
from calculations.adapters.orms.orm_persons import persons
from calculations.adapters.orms.orm_revenues import revenues
from calculations.adapters.orms.orm_users import users
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.person import Person
from calculations.domain.entities.revenues import Revenue
from calculations.domain.entities.user import User

mapper_registry = registry()


def start_mappers():
    print("Init the mappers")
    mapper_registry.map_imperatively(
        Account,
        accounts,
        properties={
            "account_id": accounts.c.id,
            "number_of_account": accounts.c.number_of_account,
            "amount": accounts.c.amount,
            "created_when": accounts.c.created_when,
            "modified_when": accounts.c.modified_when,
        },
    )

    mapper_registry.map_imperatively(
        User,
        users,
        properties={
            "user_id": users.c.id,
            "email": users.c.email,
            "password": users.c.password,
            "avatar": users.c.avatar,
            "persons": relationship(
                Person,
                backref="user",
                order_by=persons.c.id
            ),
            "created_when": users.c.created_when,
            "modified_when": users.c.modified_when
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
                Account,
                backref="person",
                order_by=accounts.c.id
            ),
            "expenses": relationship(
                Expense,
                backref="person",
                order_by=expenses.c.id
            ),
            "revenues": relationship(
                Revenue,
                backref="person",
                order_by=revenues.c.id
            ),
            "created_when": persons.c.created_when,
            "modified_when": persons.c.modified_when,
        },
    )
    

    mapper_registry.map_imperatively(
        Expense,
        expenses,
        properties={
            "expense_id": expenses.c.id,
            "description": expenses.c.description,
            "value": expenses.c.value,
            "due_date": expenses.c.due_date,
            "already_paid": expenses.c.already_paid,
            "category": expenses.c.category,
            "created_when": expenses.c.created_when,
            "modified_when": expenses.c.modified_when,
        },
    )

    mapper_registry.map_imperatively(
        Revenue,
        revenues,
        properties={
            "revenue_id": revenues.c.id,
            "description": revenues.c.description,
            "value": revenues.c.value,
            "date_receivment": revenues.c.date_of_receivment,
            "category": revenues.c.category,
            "created_when": revenues.c.created_when,
            "modified_when": revenues.c.modified_when,
        },
    )

    mapper_registry.map_imperatively(
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
            "status": balances.c.status,
            "expenses": relationship(
                Expense,
                backref="balance",
                order_by=expenses.c.id

            ),
            "revenues": relationship(
                Revenue,
                backref="balance",
                order_by=revenues.c.id
            ),
            "created_when": balances.c.created_when,
            "modified_when": balances.c.modified_when,
        }
    )