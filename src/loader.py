import pandas as pd
import logging
import os


# Create logs directory automatically
os.makedirs('logs', exist_ok=True)


# Configure logging
logging.basicConfig(
    filename='logs/billing.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def load_subscriptions(file_path):
    """
    Load subscriptions CSV file safely.
    """

    try:
        df = pd.read_csv(file_path)

        # Fill missing numeric values safely
        df['monthly_fee'] = df['monthly_fee'].fillna(0)

        df['usage_limit_gb'] = df['usage_limit_gb'].fillna(0)

        return df

    except Exception as e:

        logging.error(
            f"Error loading subscriptions file: {e}"
        )

        return pd.DataFrame()


def load_usage(file_path):
    """
    Load usage CSV file safely.
    """

    try:
        df = pd.read_csv(file_path)

        # Fill missing usage values safely
        df['data_used_gb'] = df['data_used_gb'].fillna(0)

        return df

    except Exception as e:

        logging.error(
            f"Error loading usage file: {e}"
        )

        return pd.DataFrame()