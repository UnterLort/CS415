# @Kyle Stewart @detector.py version 1
from datetime import datetime
import argparse


def parse_line(line, headers):
    parts = line.strip().split("|")
    if len(parts) != len(headers):
        print(f"Skipping line due to incorrect number of parts: {line}")
        return None
    return dict(zip(headers, parts))


def read_data(file_path, headers, debug):
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]  # Skip the header line
        data = [parse_line(line, headers) for line in lines]  # Parse each line into a dictionary
        filtered_data = [d for d in data if d]  # Remove any None values
        if debug:
            print(f"Read {len(filtered_data)} entries from {file_path}")
        return filtered_data


def print_data(data, num_samples=2):
    print()
    print("Displaying first {} entries:".format(num_samples))
    for entry in data[:num_samples]:
        for key, value in entry.items():
            print(f"{key}: {value}")
        print("-" * 40)


def check_fraud(t1, t2, t3):
    timedelta1 = t2["timestamp"] - t1["timestamp"]
    timedelta2 = t3["timestamp"] - t2["timestamp"]

    return (timedelta1.total_seconds() <= 120
            and timedelta2.total_seconds() <= 86400
            and t1["cc"] != t2["cc"]
            and t1["product_desc"] == t2["product_desc"]
            and float(t2["cost"]) == float(t3["cost"])
            and t1["shipping_address"] == t3["shipping_address"]
            and t2["product_order_number"] == t3["product_order_number"]
            and t1["timestamp"] < t2["timestamp"] < t3["timestamp"])


def process_print_data(A, B, C):
    for data in [A, B, C]:
        for entry in data:
            try:
                entry["timestamp"] = (datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S"))
            except ValueError:
                continue

    print("User Data:")
    print_data(A)

    print("\nMarket Data:")
    print_data(B)

    print("\nVendor Data:")
    print_data(C)

    account_stop = []

    for t1 in A:
        for t2 in B:
            for t3 in C:
                if check_fraud(t1, t2, t3):
                    account_stop.append(t1["market_account"])

    account_stop = list(set(account_stop))  # Remove duplicates

    print("Accounts to shut down:", account_stop)


if __name__ == "__main__":
    par = argparse.ArgumentParser(description="Fraud Triangle Assignment")
    par.add_argument("--debug", action="store_true", help="Enable debug mode for additional output")
    args = par.parse_args()

    user_headers = ["timestamp", "cc", "market_account", "product_desc", "cost", "shipping_address",
                    "cc_billing_address"]
    market_headers = ["timestamp", "cc", "product_desc", "cost", "cc_billing_address", "product_order_number"]
    vendor_headers = ["timestamp", "cost", "shipping_address", "product_order_number"]

    user_data = read_data("user_tx_1.txt", user_headers, args.debug)  # Read user data from file
    market_data = read_data("market_tx_1.txt", market_headers, args.debug)  # Read market data from file
    vendor_data = read_data("vendor_tx_1.txt", vendor_headers, args.debug)  # Read vendor data from file
