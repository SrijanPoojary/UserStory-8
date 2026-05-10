import pandas as pd

from src.usage_aggregator import aggregate_usage


def test_multiple_usage_records():

    usage_data = pd.DataFrame([
        {
            'subscription_id': 'S001',
            'usage_date': '2024-03-01',
            'data_used_gb': 50
        },
        {
            'subscription_id': 'S001',
            'usage_date': '2024-03-10',
            'data_used_gb': 30
        }
    ])

    result = aggregate_usage(usage_data)

    assert result['S001'] == 80


def test_no_usage_records():

    usage_data = pd.DataFrame([])

    result = aggregate_usage(usage_data)

    assert result == {}


def test_invalid_usage_dates():

    usage_data = pd.DataFrame([
        {
            'subscription_id': 'S001',
            'usage_date': 'invalid-date',
            'data_used_gb': 50
        }
    ])

    result = aggregate_usage(usage_data)

    assert result == {}