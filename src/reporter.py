import pandas as pd
import json


def generate_billing_output(results, output_file='billing_output.csv'):
    """
    Generate billing_output.csv
    """

    df = pd.DataFrame(results)

    df.to_csv(output_file, index=False)


def generate_summary(results, output_file='billing_summary.json'):
    """
    Generate billing_summary.json
    """

    total_subscriptions = len(results)

    active_subscriptions = sum(
        1 for r in results if r['final_status'] == 'ACTIVE'
    )

    suspended_subscriptions = sum(
        1 for r in results if r['final_status'] == 'SUSPENDED'
    )

    cancelled_subscriptions = sum(
        1 for r in results if r['final_status'] == 'CANCELLED'
    )

    total_revenue = sum(r['total_bill'] for r in results)

    average_bill = (
        total_revenue / total_subscriptions
        if total_subscriptions > 0 else 0
    )

    summary = {
        'total_subscriptions': total_subscriptions,
        'active_subscriptions': active_subscriptions,
        'suspended_subscriptions': suspended_subscriptions,
        'cancelled_subscriptions': cancelled_subscriptions,
        'total_revenue': total_revenue,
        'average_bill': average_bill
    }

    with open(output_file, 'w') as file:
        json.dump(summary, file, indent=4)