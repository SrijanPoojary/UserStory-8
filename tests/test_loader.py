import pandas as pd
from src.loader import load_subscriptions, load_usage


def test_load_subscriptions(tmp_path):

    file = tmp_path / "subscriptions.csv"

    df = pd.DataFrame([
        {
            "subscription_id": "S001",
            "monthly_fee": 500,
            "usage_limit_gb": 100
        }
    ])

    df.to_csv(file, index=False)

    result = load_subscriptions(file)

    assert not result.empty


def test_load_usage(tmp_path):

    file = tmp_path / "usage.csv"

    df = pd.DataFrame([
        {
            "subscription_id": "S001",
            "usage_date": "2024-03-01",
            "data_used_gb": 50
        }
    ])

    df.to_csv(file, index=False)

    result = load_usage(file)

    assert not result.empty