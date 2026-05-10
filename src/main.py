from src.loader import load_subscriptions, load_usage
from src.usage_aggregator import aggregate_usage
from src.billing_engine import calculate_bill
from src.status_engine import evaluate_status
from src.reporter import generate_billing_output, generate_summary

subscriptions = load_subscriptions('data/subscriptions.csv')
usage = load_usage('data/usage.csv')

usage_totals = aggregate_usage(usage)

results = []

for _, subscription in subscriptions.iterrows():

    subscription_id = subscription['subscription_id']

    total_usage = usage_totals.get(subscription_id, 0)

    billing = calculate_bill(subscription, total_usage)

    final_status = evaluate_status(subscription, total_usage)

    result = {
        'subscription_id': subscription_id,
        'customer_id': subscription['customer_id'],
        'plan': subscription['plan'],
        'total_usage_gb': billing['total_usage_gb'],
        'overage_gb': billing['overage_gb'],
        'total_bill': billing['total_bill'],
        'final_status': final_status
    }

    results.append(result)

# Generate output files
generate_billing_output(results)

generate_summary(results)

print("Billing processing completed successfully.")
print("Generated billing_output.csv")
print("Generated billing_summary.json")