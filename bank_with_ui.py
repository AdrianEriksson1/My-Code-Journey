import datetime

class BankAccount:
    accounts = {}

    def __init__(self, owner="a"):
        self.owner = owner
        self.currencies = {"USD": 0, "SEK": 0, "GBP": 0, "EUR": 0}
        self.history = {}
        self.usd_currency_conversion_rates = {"SEK": 10.91, "GBP": 0.81, "EUR": 0.94, "USD": 1}
        self.ownera = None

    @classmethod
    def create_account(cls, owner, password):
        new_account = cls(owner)
        cls.accounts[owner] = password
        print("Account created successfully!")
        return new_account

    @classmethod
    def login_account(cls, owner):
        if owner in cls.accounts:
            return cls.accounts[owner]
        else:
            print("Account not found!")
            return None

    def sign_in_or_create_account(self):
        while True:
            choice = input("Sign in(x) or Create an account(y): ").lower()
            if choice == "x":
                owner = input("Enter your username: ")
                self.ownera = self.login_account(owner)
                if self.ownera:
                    break
            elif choice == "y":
                owner = input("Create a username: ")
                self.password = input("Create a password: ")
                self.ownera = self.create_account(owner, self.password)
                break
            else:
                print("Invalid choice!")

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
        if account in self.accounts:
            if self.currencies[currency] >= self.amount:
                self.currencies[currency] -= amount
                account.deposit(currency, amount)
                self.history[datetime.datetime.now()] = f"-{self.amount} {currency}"
            else:
                print("Insufficient Funds!")
        else:
            print("No such username")

    def get_history(self):
        fmat_his = {}
        for time, amo in self.history.items():
            form_time = time.strftime("%Y-%m-%d %H:%M")
            fmat_his[form_time] = amo
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



    def actions(self):
        use = input("Choose action:\n Deposit, press d\n Withdraw, press w\n Get balance, press b\n Display account Info, press i\n Transfer to another account, press t\n Get transaction history, press h\n Convert to different currency, press c\n Or log out, press x\n")
        while use != "x":
            
            if use == "d":
                self.amount = float(input("Input amount: "))
                self.currency = input("Input currency: ")
                self.deposit(self.currency, self.amount)
            elif use == "w":
                self.amount = float(input("Input amount: "))
                self.currency = input("Input currency: ")
                self.withdraw(self.currency, self.amount)
            elif use == "b":
                print(self.get_balance())
            elif use == "i":
                self.display_info()
            elif use == "t":
                self.account = input("Input account to transfer to: ")
                self.amount = float(input("Input amount: "))
                self.currency = input("Input currency: ")
                self.transfer(self.accounts[self.account], self.currency, self.amount)
            elif use == "h":
                print(self.get_history())
            elif use == "c":
                self.amount = float(input("Input amount: "))
                self.currency_to_convert = input("Input currency to convert: ")
                self.wanted_currency = input("Input wanted currency to convert to: ")
                self.currency_exchange(self.wanted_currency, self.currency_to_convert, self.amount)
            elif use == "x":
                quit()
            else:
                print("Wrong")
            use = input("Choose action:\n Deposit, press d\n Withdraw, press w\n Get balance, press b\n Display account Info, press i\n Transfer to another account, press t\n Get transaction history, press h\n Convert to different currency, press c\n Or log out, press x\n")

account = BankAccount()
account.sign_in_or_create_account()
if account.ownera:
    account.ownera.actions()
