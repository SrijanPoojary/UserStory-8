import os

from src.reporter import generate_billing_output, generate_summary


sample_results = [
    {
        'subscription_id': 'S001',
        'customer_id': 'C001',
        'plan': 'Premium',
        'total_usage_gb': 100,
        'overage_gb': 0,
        'total_bill': 500,
        'final_status': 'ACTIVE'
    }
]


def test_generate_billing_output(tmp_path):

    output_file = tmp_path / "billing_output.csv"

    generate_billing_output(sample_results, output_file)

    assert os.path.exists(output_file)


def test_generate_summary(tmp_path):

    output_file = tmp_path / "billing_summary.json"

    generate_summary(sample_results, output_file)

    assert os.path.exists(output_file)