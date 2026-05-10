def evaluate_status(subscription, total_usage):
    """
    Evaluate final subscription status.
    """

    current_status = subscription['status']
    usage_limit = float(subscription['usage_limit_gb'])

    # CANCELLED never changes
    if current_status == 'CANCELLED':
        return 'CANCELLED'

    # SUSPENDED -> ACTIVE
    if current_status == 'SUSPENDED' and total_usage <= usage_limit:
        return 'ACTIVE'

    # ACTIVE -> SUSPENDED
    if total_usage > (1.5 * usage_limit):
        return 'SUSPENDED'

    return current_status