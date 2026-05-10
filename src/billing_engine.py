def calculate_bill(subscription, total_usage):
    """
    Calculate billing details for one subscription.
    """

    status = subscription['status']
    monthly_fee = float(subscription['monthly_fee'])
    usage_limit = float(subscription['usage_limit_gb'])

    overage_gb = 0
    total_bill = 0

    # CANCELLED subscriptions
    if status == 'CANCELLED':
        return {
            'total_usage_gb': total_usage,
            'overage_gb': 0,
            'total_bill': 0
        }

    # SUSPENDED subscriptions
    if status == 'SUSPENDED':
        return {
            'total_usage_gb': total_usage,
            'overage_gb': 0,
            'total_bill': monthly_fee
        }

    # ACTIVE subscriptions
    if total_usage <= usage_limit:

        total_bill = monthly_fee

    else:

        overage_gb = total_usage - usage_limit
        overage_charge = overage_gb * 10
        total_bill = monthly_fee + overage_charge

    return {
        'total_usage_gb': total_usage,
        'overage_gb': overage_gb,
        'total_bill': total_bill
    }