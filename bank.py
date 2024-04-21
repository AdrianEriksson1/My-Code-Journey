import datetime

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.currencies = {"USD": 0, "SEK": 0, "GBP": 0, "EUR": 0}
        self.history = {}
        self.usd_currency_conversion_rates = {"SEK": 10.91, "GBP": 0.81, "EUR": 0.94, "USD": 1}
        self.currencies["USD"] += self.balance



    def deposit(self, currency, amount):
        self.amount = amount
        self.currencies[currency] += self.amount
        self.history[datetime.datetime.now()] = f"+{self.amount} {currency}"
        print("Deposited: ", self.amount, currency, "\nCurrent Balance:", self.currencies)

    def withdraw(self, currency, amount):
        self.amount = amount
        if self.currencies[currency] >= self.amount:
            self.currencies[currency] -= self.amount
            self.history[datetime.datetime.now()] = f"-{self.amount} {currency}"
            print("Withdrew: ", self.amount, currency, "\nCurrent Balance:", self.currencies)
        else:
            print("Insufficient Funds!")

    def get_balance(self):
        return self.currencies

    def display_info(self):
        print(self.owner, ":\n", self.currencies)

    def transfer(self, account, currency, amount):
        self.amount = amount

        if self.currencies[currency] >= self.amount:
            self.currencies[currency] -= amount
            account.deposit(currency, amount)
            self.history[datetime.datetime.now()] = f"-{self.amount} {currency}"
        else:
            print("Insufficient Funds!")

    def get_history(self):
        fmat_his = {time.strftime("%Y-%m-%d %H:%M"): amo for time, amo in self.history.items()}
        return fmat_his

    def currency_exchange(self, wanted_currency, currency_to_conv, amount):
        self.amount = amount
        if self.currencies[currency_to_conv] >= self.amount:
            self.currencies[currency_to_conv] -= self.amount
            self.amount_in_usd = self.amount / self.usd_currency_conversion_rates[currency_to_conv]
            self.amount_in_wantd_currency = self.amount_in_usd * self.usd_currency_conversion_rates[wanted_currency]
            self.currencies[wanted_currency] += self.amount_in_wantd_currency

            self.history[datetime.datetime.now()] = f"{self.amount} {currency_to_conv} --> {self.amount_in_wantd_currency} {wanted_currency}"

            print(f"{self.amount} {currency_to_conv} --> {self.amount_in_wantd_currency} {wanted_currency}")
        else:
            print("Insufficient Funds")

b1 = BankAccount("Elias", 1000)
b2 = BankAccount("Martin", 89374637)
b1.deposit("SEK", 3500)
b2.withdraw("USD", 1000)
b1.display_info()
b2.transfer(b1, "USD", 6000)
b1.currency_exchange("SEK", "USD", 1000)
print(b1.get_history())
print(b2.get_history())
