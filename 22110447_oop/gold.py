class Transaction:
    def __init__(self, transaction_id, date, unit_price, quantity):
        self.transaction_id = transaction_id
        self.date = date
        self.unit_price = unit_price
        self.quantity = quantity

    def calculate_total(self):
        return self.unit_price * self.quantity

    def get_info(self):
        pass

    def get_quantity(self):
        return self.quantity

    def get_unit_price(self):
        return self.unit_price


class GoldTransaction(Transaction):
    def __init__(self, transaction_id, date, unit_price, quantity, gold_type):
        super().__init__(transaction_id, date, unit_price, quantity)
        self.gold_type = gold_type

    def calculate_total(self):
        return super().calculate_total()

    def get_info(self):
        return f"{self.transaction_id} - {self.date} - {self.gold_type} - {self.quantity} - {self.unit_price} - Thành tiền: {self.calculate_total()}"

    def get_quantity(self):
        return super().get_quantity()

    def get_unit_price(self):
        return super().get_unit_price()


class CurrencyTransaction(Transaction):
    def __init__(
        self,
        transaction_id,
        date,
        unit_price,
        quantity,
        currency_type,
        transaction_type,
    ):
        super().__init__(transaction_id, date, unit_price, quantity)
        self.currency_type = currency_type
        self.transaction_type = transaction_type

    def calculate_total(self):
        if self.transaction_type == 1:
            return super().calculate_total()
        elif self.transaction_type == 2:
            return super().calculate_total() * 1.05

    def get_info(self):
        if self.transaction_type == 1:
            return f"GD mua: {self.transaction_id} - {self.date} - {self.currency_type} - {self.quantity} - {self.unit_price} - Thành tiền: {self.calculate_total()}"
        else:
            return f"GD bán: {self.transaction_id} - {self.date} - {self.currency_type} - {self.quantity} - {self.unit_price} - Thành tiền: {self.calculate_total()}"

    def get_unit_price(self):
        return super().get_unit_price()

    def get_quantity(self):
        return super().get_quantity()


class TransactionManager:
    def __init__(self):
        pass

    def input_quantity(self):
        quantity = input("Nhập số lượng: ")
        while True:
            try:
                quantity = int(quantity)
                break
            except:
                quantity = input("Nhập số lượng phải là số nguyên: ")
                continue
        return quantity

    def input_unit_price(self):
        unit_price = input("Nhập đơn giá: ")
        while True:
            try:
                unit_price = int(unit_price)
                break
            except:
                unit_price = input("Nhập đơn giá phải là số nguyên: ")
                continue
        return unit_price

    def input_transaction_type(self, text):
        transaction_type = input(text)
        while True:
            try:
                transaction_type = int(transaction_type)
                if transaction_type in [1, 2]:
                    break
                else:
                    transaction_type = input("Không hợp lệ !\nNhập lại: ")
                    continue
            except:
                transaction_type = input("Nhập loại giao dịch phải là số: ")
                continue
        return transaction_type

    def input_gold_type(self):
        gold_type = input("Chọn loại: 18K / 24k / 9999: ")
        while gold_type not in ["18K", "24k", "9999"]:
            gold_type = input("Chọn loại: 18K / 24k / 9999: ")
        return gold_type

    def input_currency_type(self):
        currency_type = input("Chọn loại: USD / EUR / AUD: ")
        while currency_type not in ["USD", "EUR", "AUD"]:
            currency_type = input("Chọn loại: USD / EUR / AUD: ")
        return currency_type

    def make_transaction(self):
        while True:
            transaction_id = input("Nhập mã GD: ")

            date = input("Nhập ngày GD: ")
            quantity = self.input_quantity()
            transaction_type = self.input_transaction_type(
                "Nhập loại giao dịch: 1: Vàng, 2: Tiền tệ: "
            )
            if transaction_type == 1:
                gold_type = self.input_gold_type()
                unit_price = self.input_unit_price()
                gold_transaction = GoldTransaction(
                    transaction_id, date, unit_price, quantity, gold_type
                )
                print(gold_transaction.get_info())
                print(f"Tổng số lượng: {gold_transaction.get_quantity()}")
                print(f"Tổng số tiền: {gold_transaction.calculate_total()}")

            elif transaction_type == 2:
                currency_type = self.input_currency_type()
                unit_price = self.input_unit_price()
                currency_transaction_type = self.input_transaction_type(
                    "Bạn mua hay bán: 1: Mua, 2: Bán: "
                )
                currency_transaction = CurrencyTransaction(
                    transaction_id,
                    date,
                    unit_price,
                    quantity,
                    currency_type,
                    currency_transaction_type,
                )
                print(currency_transaction.get_info())
                print(f"Tổng số lượng: {currency_transaction.get_quantity()}")
                print(f"Tổng số tiền: {currency_transaction.calculate_total()}")

            ch = input("Bạn có muốn tiếp tục giao dịch: 1: Có, 0: Không: ")
            if ch == "0":
                break


if __name__ == "__main__":
    transaction_manager = TransactionManager()
    transaction_manager.make_transaction()
