# Subscription Billing & Status Evaluation Engine

## Project Overview

This project is a Python-based billing engine developed for processing subscription and usage data for a digital subscription platform.

The application:
- Reads subscription and usage data from CSV files
- Aggregates customer usage for March 2024
- Calculates billing amounts based on business rules
- Evaluates final subscription status
- Generates billing reports in CSV and JSON formats
- Handles invalid data safely using logging
- Includes unit tests with 94% test coverage

---

## Business Rules

### Usage Aggregation
- Only usage records from March 2024 are considered
- Invalid usage dates are skipped and logged
- If no usage exists, usage defaults to 0

### Billing Rules
- If usage <= usage limit:
  - Total bill = monthly fee
- If usage > usage limit:
  - Overage charge = extra GB × 10
  - Total bill = monthly fee + overage charge
- Suspended subscriptions:
  - Only monthly fee is charged
  - No overage charges
- Cancelled subscriptions:
  - Total bill = 0

### Status Evaluation Rules
- If usage exceeds 150% of usage limit:
  - Final status = SUSPENDED
- If previous status was SUSPENDED and usage is within limit:
  - Final status = ACTIVE
- CANCELLED status never changes

---

## Project Structure

```text
UserStory8/
│── data/
│── logs/
│── src/
│── tests/
│── billing_output.csv
│── billing_summary.json
│── README.md
│── requirements.txt
│── pytest.ini
```

---

## How to Run the Application

Run the project using:

```bash
python -m src.main
```

---

## How to Run Unit Tests

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src
```

---

## Assumptions Made

- Missing numeric values are treated as 0
- Only March 2024 usage records are processed
- Invalid dates are skipped safely
- CSV files are assumed to contain required columns

---

## Edge Cases Handled

- Invalid usage dates
- Missing numeric values
- No usage records
- Suspended subscriptions
- Cancelled subscriptions
- Invalid file handling using logging

---

## Test Coverage

- Framework used: pytest
- Total test coverage: 94%

---

## Outputs Generated

### billing_output.csv
Contains:
- subscription_id
- customer_id
- plan
- total_usage_gb
- overage_gb
- total_bill
- final_status

### billing_summary.json
Contains:
- total_subscriptions
- active_subscriptions
- suspended_subscriptions
- cancelled_subscriptions
- total_revenue
- average_bill

---

## Logging

Errors and invalid records are logged in:

```text
logs/billing.log
```
Project completed successfully.