from calculations.domain.aggregates.balance import Balance


def test_balance_with_negative_value(
    mock_balance,
):
    balance: Balance = mock_balance

    assert balance.balance_with_negative_value() is False