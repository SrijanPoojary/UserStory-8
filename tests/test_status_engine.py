from src.status_engine import evaluate_status


def test_active_to_suspended_transition():

    subscription = {
        'status': 'ACTIVE',
        'usage_limit_gb': 100
    }

    result = evaluate_status(subscription, 200)

    assert result == 'SUSPENDED'


def test_suspended_to_active_transition():

    subscription = {
        'status': 'SUSPENDED',
        'usage_limit_gb': 100
    }

    result = evaluate_status(subscription, 80)

    assert result == 'ACTIVE'


def test_cancelled_status_unchanged():

    subscription = {
        'status': 'CANCELLED',
        'usage_limit_gb': 100
    }

    result = evaluate_status(subscription, 500)

    assert result == 'CANCELLED'