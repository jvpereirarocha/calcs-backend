from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
from calculations.adapters.orms.orm_accounts import accounts
from calculations.adapters.orms.orm_expenses import expenses
from calculations.adapters.orms.orm_persons import persons
from calculations.adapters.orms.orm_revenues import revenues
from calculations.adapters.orms.orm_users import users
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.person import Person
from calculations.domain.entities.revenues import Revenue
from calculations.domain.entities.user import User

mapper_registry = registry()


def start_mappers():
    print("Init the mappers")
    account_mapper = mapper_registry.map_imperatively(
        Account,
        accounts,
        properties={
            "number_of_account": accounts.c.number_of_account,
            "value": accounts.c.value,
            "created_when": accounts.c.created_when,
            "modified_when": accounts.c.modified_when,
        },
    )

    user_mapper = mapper_registry.map_imperatively(
        User,
        users,
        properties={
            "email": users.c.email,
            "password": users.c.password,
            "avatar": users.c.avatar,
            "created_when": users.c.created_when,
            "modified_when": users.c.modified_when
        },
    )
    person_mapper = mapper_registry.map_imperatively(
        Person,
        persons,
        properties={
            "first_name": persons.c.first_name,
            "last_name": persons.c.last_name,
            "date_of_birth": persons.c.date_of_birth,
            "user": relationship(
                user_mapper,
                back_populates="person"
            ),
            "account": relationship(
                account_mapper,
                back_populates="accounts"
            ),
            "created_when": persons.c.created_when,
            "modified_when": persons.c.modified_when,
        },
    )
    

    expense_mapper = mapper_registry.map_imperatively(
        Expense,
        expenses,
        properties={
            "description": expenses.c.description,
            "value": expenses.c.value,
            "due_date": expenses.c.due_date,
            "already_paid": expenses.c.already_paid,
            "category": expenses.c.category,
            "account": relationship(
                account_mapper,
                back_populates="expenses"
            ),
            "created_when": expenses.c.created_when,
            "modified_when": expenses.c.modified_when,
        },
    )

    revenue_mapper = mapper_registry.map_imperatively(
        Revenue,
        revenues,
        properties={
            "description": revenues.c.description,
            "value": revenues.c.value,
            "date_receivment": revenues.c.date_of_receivment,
            "category": revenues.c.category,
            "account": relationship(
                account_mapper,
                back_populates="revenues"
            ),
            "created_when": revenues.c.created_when,
            "modified_when": revenues.c.modified_when,
        },
    )