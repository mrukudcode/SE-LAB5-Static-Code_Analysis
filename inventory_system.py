"""Inventory System Module"""

import json
import logging
from datetime import datetime

# Global inventory dictionary
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory with quantity."""
    if logs is None:
        logs = []
    if not isinstance(item, str):
        logging.warning("Invalid item type: %s. Must be str.", type(item))
        return
    if not isinstance(qty, int):
        logging.warning("Invalid quantity type: %s. Must be int.", type(qty))
        return
    if qty <= 0:
        logging.warning("Quantity must be positive.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the inventory."""
    try:
        if item not in stock_data:
            raise KeyError(f"{item} not found in inventory.")
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Invalid quantity.")
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, ValueError) as e:
        logging.warning("Remove failed: %s", e)


def get_qty(item):
    """Get the quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error("Load failed: %s", e)


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f)
    except IOError as e:
        logging.error("Save failed: %s", e)


def print_data():
    """Print the current inventory report."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the threshold quantity."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution block."""
    logging.basicConfig(level=logging.INFO)
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, now handled
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
