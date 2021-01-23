import os
import settings
import pandas as pd

HEADERS = {
    "Acquisition": [
        "id",
        "channel",
        "seller",
        "interest_rate",
        "balance",
        "loan_term",
        "origination_date",
        "first_payment_date",
        "ltv",
        "cltv",
        "borrower_count",
        "dti",
        "borrower_credit_score",
        "first_time_homebuyer",
        "loan_purpose",
        "property_type",
        "unit_count",
        "occupancy_status",
        "property_state",
        "zip",
        "insurance_percentage",
        "product_type",
        "co_borrower_credit_score"
    ],
    "Performance": [
        "id",
        "reporting_period",
        "servicer_name",
        "interest_rate",
        "balance",
        "loan_age",
        "months_to_maturity",
        "maturity_date",
        "msa",
        "delinquency_status",
        "modification_flag",
        "zero_balance_code",
        "zero_balance_date",
        "last_paid_installment_date",
        "foreclosure_date",
        "disposition_date",
        "foreclosure_costs",
        "property_repair_costs",
        "recovery_costs",
        "misc_costs",
        "tax_costs",
        "sale_proceeds",
        "credit_enhancement_proceeds",
        "repurchase_proceeds",
        "other_foreclosure_proceeds",
        "non_interest_bearing_balance",
        "principal_forgiveness_balance"
    ]
}

TYPES = {
    "Acquisition": {
        'id': 'int64',
        'channel': 'object',
        'seller': 'object',
        'interest_rate': 'float64',
        'balance': 'int64',
        'loan_term': 'int64',
        'origination_date': 'object',
        'first_payment_date': 'object',
        'ltv': 'int64',
        'cltv': 'float64',
        'borrower_count': 'float64',
        'dti': 'float64',
        'borrower_credit_score': 'float64',
        'first_time_homebuyer': 'object',
        'loan_purpose': 'object',
        'property_type': 'object',
        'unit_count': 'int64',
        'occupancy_status': 'object',
        'property_state': 'object',
        'zip': 'int64',
        'insurance_percentage': 'float64',
        'product_type': 'object',
        'co_borrower_credit_score': 'float64',
    },
    "Performance": {
        'id': 'int64',
        'reporting_period': 'object',
        'servicer_name': 'object',
        'interest_rate': 'float64',
        'balance': 'float64',
        'loan_age': 'float64',
        'months_to_maturity': 'float64',
        'maturity_date': 'float64',
        'msa': 'object',
        'delinquency_status': 'float64',
        'modification_flag': 'int64',
        'zero_balance_code': 'object',
        'zero_balance_date': 'float64',
        'last_paid_installment_date': 'object',
        'foreclosure_date': 'object',
        'disposition_date': 'object',
        'foreclosure_costs': 'object',
        'property_repair_costs': 'float64',
        'recovery_costs': 'float64',
        'misc_costs': 'float64',
        'tax_costs': 'float64',
        'sale_proceeds': 'float64',
        'credit_enhancement_proceeds': 'float64',
        'repurchase_proceeds': 'float64',
        'other_foreclosure_proceeds': 'float64',
        'non_interest_bearing_balance': 'float64',
        'principal_forgiveness_balance': 'float64',
    },
}

# List of columns to keep
SELECT = {
    "Acquisition": HEADERS["Acquisition"],
    "Performance": [
        "id",
        "foreclosure_date"
    ]
}


def concatenate(prefix="Acquisition"):
    # Get a list of the files in "DATA_DIR"
    files = os.listdir(settings.DATA_DIR)
    # Loop through the files; if the file name starts with "prefix", read it as a DataFrame
    for f in files:
        if not f.startswith(prefix):
            continue
        data = pd.read_csv(os.path.join(settings.DATA_DIR, f), sep="|", header=None, names=HEADERS[prefix],
                           index_col=False, dtype=TYPES[prefix])
        # Keep only the columns on "SELECT"
        data = data[SELECT[prefix]]
        # Write the DataFrame to a .csv file; only use headers for the first write
        if not os.path.isfile(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix))):
            data.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix)), sep="|", header=SELECT[prefix],
                        index=False)
        else:
            data.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix)), mode='a', sep="|", header=False,
                        index=False)


if __name__ == "__main__":
    concatenate("Acquisition")
    concatenate("Performance")
