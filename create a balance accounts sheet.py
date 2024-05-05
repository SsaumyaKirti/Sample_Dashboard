import pandas as pd
from prettytable import PrettyTable

def get_user_input(prompt):
    "Get user input and validate "
    while True:
        try:
            value = input(prompt)
            return value.strip()  # Remove leading/trailing spaces
        except KeyboardInterrupt:
            print("\nOperation canceled by user.")
            exit(0)
        except Exception:
            print("Invalid input. Please try again.")

def collect_asset_liability_details(num_entries):
    """Collect asset and liability details from the user."""
    asset_data = []
    liability_data = []
    for _ in range(num_entries):
        print('From below table choose the account name') # pprovide user a number of options in a tabular format
# Initialize the table with column names
        balance_sheet = PrettyTable(["Category", "Account"])

        # Add rows for assets
        balance_sheet.add_row(["Assets", "Cash and Cash Equivalents"])
        balance_sheet.add_row(["Assets", "Accounts Receivable"])
        balance_sheet.add_row(["Assets", "Inventory"])
        balance_sheet.add_row(["Assets", "Property, Plant, and Equipment"])
        balance_sheet.add_row(["Assets", "Investments"])
        balance_sheet.add_row(["Assets", "Intangible Assets"])

        # Add rows for liabilities
        balance_sheet.add_row(["Liabilities", "Accounts Payable"])
        balance_sheet.add_row(["Liabilities", "Short-Term Debt"])
        balance_sheet.add_row(["Liabilities", "Long-Term Debt"])
        balance_sheet.add_row(["Liabilities", "Other Liabilities"])

        # Add rows for equity
        balance_sheet.add_row(["Equity", "Common Stock"])
        balance_sheet.add_row(["Equity", "Retained Earnings"])
        balance_sheet.add_row(["Equity", "Additional Paid-In Capital"])

        # Set alignment for columns
        balance_sheet.align = "l"

        # Display 
        print(balance_sheet)
#input details
        account_type = get_user_input("Choose account type (asset/liability): ").lower()
        account_name = get_user_input("Enter account name: ")
        amount = float(get_user_input("Enter amount (in ₹): "))
# input done
        # Validate account type
        if account_type not in ["asset", "liability"]:
            print("Invalid account type. Please choose 'asset' or 'liability'.")
            continue

        # Store data with appropriate sign
        if account_type == "asset":
            asset_data.append([account_name, amount, 0])  # 0 for liability column
        else:
            liability_data.append([account_name, 0, amount])  # 0 for asset column

    return asset_data + liability_data

def main():
    # Prompt the user for asset and liability details
    num_entries = int(get_user_input("Enter the number of entries: "))

    # Collect asset and liability details
    print("\nEnter Asset and Liability Details:")
    data = collect_asset_liability_details(num_entries)

    # Create a DataFrame
    columns = ["Account", "Asset Amount (in ₹)", "Liability Amount (in ₹)"]
    df = pd.DataFrame(data, columns=columns)

    # Calculate total assets and total liabilities
    total_assets = df["Asset Amount (in ₹)"].sum()
    total_liabilities = df["Liability Amount (in ₹)"].sum()

    # Add a total row
    df.loc[len(df)] = ["Total", total_assets, total_liabilities]

    # Prompt the user for the output file path
    output_file_path = get_user_input("Enter the output file path (e.g., 'my_balance_sheet.csv'): ")

    # Save to the specified CSV file
    df.to_csv(output_file_path, index=False)
    print(f"Balance sheet saved to {output_file_path}")

if __name__ == "__main__":
    main()
