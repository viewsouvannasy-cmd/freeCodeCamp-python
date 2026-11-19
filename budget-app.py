import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        number_space = 30 - len(self.name)
        side_space = "*" * round(number_space / 2)
        add = "*" if number_space % 2 != 0 else ""
        summary = f"{add}{side_space}{self.name}{side_space}\n"

        for item in self.ledger:
            describe_length = min(len(item["description"]), 23)
            amount_length = None
            amount_float = None
            if not isinstance(item["amount"], float):
                amount_float = f"{item["amount"]:.2f}"
                amount_length = min(len(amount_float), 7)
            else:
                amount_float = f"{item["amount"]}"
                amount_length = min(len(amount_float), 7)

            remine_space = " " * (30 - describe_length - amount_length)
            summary += f"{item["description"][0:23]}{remine_space}{amount_float[0:7]}\n"

        total = f"Total: {self.get_balance():.2f}"
        summary += total

        return summary

    def deposit(self, amount, description=""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        transaction = {"amount": -amount, "description": description}
        self.ledger.append(transaction)
        return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            if item["amount"] < 0:
                balance -= abs(item["amount"])
            else:
                balance += item["amount"]

        return balance

    def get_total_spend(self):
        total_spend = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total_spend += abs(item["amount"])
        return float(f"{total_spend:.2f}")

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return not amount > self.get_balance()


def create_spend_chart(categories):
    chart_header = "Percentage spent by category\n"
    total_spend = sum(category.get_total_spend() for category in categories)
    percentage_list = []
    total_name_length = 0
    for category in categories:
        total_category_spend = category.get_total_spend()
        total_name_length = (
            len(category.name)
            if total_name_length < len(category.name)
            else total_name_length
        )
        percentage_spend = total_category_spend / total_spend * 100
        percentage_list.append(
            {
                "category": category.name,
                "percentage_spend": int((percentage_spend // 10) * 10),
            }
        )

    # generate body chart
    chart_body = ""
    num = 100
    while num >= 0:
        num_bar = None
        if num == 100:
            num_bar = num
        elif num == 0:
            num_bar = f"  {num}"
        else:
            num_bar = f" {num}"
        row = f"{num_bar}|"

        for item in percentage_list:
            if item["percentage_spend"] >= num:
                row += f" o "
            else:
                row += f"   "
        row += " \n"
        chart_body += row
        num -= 10

    # generate footer chart
    bar_space = " " * 4
    chart_footer = f"{bar_space}{'---' * len(percentage_list) + '-'}\n"
    for i in range(total_name_length):
        row = f"{bar_space}"
        for item in percentage_list:
            text = item["category"][i : i + 1]
            character = " " if not text else text
            row += f" {character} "

        row += " " if i == total_name_length - 1 else "\n"
        chart_footer += row

    return chart_header + chart_body + chart_footer


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothg")
food.transfer(50, clothing)
clothing.deposit(500, "initial deposit")
clothing.withdraw(25.00, "new shirt")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(10.00, "fuel")


print(create_spend_chart([food, clothing, auto]))
