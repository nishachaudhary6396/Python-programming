import re

class TransferError(Exception):
    pass


def transfer(from_account, to_account, amount, balance):
    
    account_pattern = r"^\d{10}$"
    
    if not re.match(account_pattern, from_account):
        raise TransferError("Invalid from account")
    
    if not re.match(account_pattern, to_account):
        raise TransferError("Invalid to account")
    
    if amount <= 0:
        raise TransferError("Invalid amount")
    if amount > balance:
        raise TransferError("Insufficient balance")
    return balance - amount