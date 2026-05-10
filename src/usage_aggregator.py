import pandas as pd
import logging


def aggregate_usage(usage_df):
    """
    Aggregate March 2024 usage per subscription.
    """

    usage_totals = {}

    for _, row in usage_df.iterrows():

        subscription_id = row.get('subscription_id')
        usage_date = row.get('usage_date')
        data_used = row.get('data_used_gb', 0)

        try:
            # Convert date safely
            parsed_date = pd.to_datetime(usage_date)

            # Only March 2024
            if parsed_date.year == 2024 and parsed_date.month == 3:

                # Safe numeric conversion
                data_used = float(data_used)

                if subscription_id not in usage_totals:
                    usage_totals[subscription_id] = 0

                usage_totals[subscription_id] += data_used

        except Exception as e:
            logging.error(
                f"Invalid usage record for subscription {subscription_id}: {e}"
            )

    return usage_totals