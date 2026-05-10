from src.billing_engine import calculate_bill


def test_bill_without_overage():

    subscription = {
        'status': 'ACTIVE',
        'monthly_fee': 500,
        'usage_limit_gb': 100
    }

    result = calculate_bill(subscription, 80)

    assert result['overage_gb'] == 0
    assert result['total_bill'] == 500


def test_bill_with_overage():

    subscription = {
        'status': 'ACTIVE',
        'monthly_fee': 500,
        'usage_limit_gb': 100
    }

    result = calculate_bill(subscription, 150)

    assert result['overage_gb'] == 50
    assert result['total_bill'] == 1000


def test_suspended_subscription_billing():

    subscription = {
        'status': 'SUSPENDED',
        'monthly_fee': 500,
        'usage_limit_gb': 100
    }

    result = calculate_bill(subscription, 300)

    assert result['overage_gb'] == 0
    assert result['total_bill'] == 500


def test_cancelled_subscription_billing():

    subscription = {
        'status': 'CANCELLED',
        'monthly_fee': 500,
        'usage_limit_gb': 100
    }

    result = calculate_bill(subscription, 300)

    assert result['total_bill'] == 0