# Set 5 (Banking Transactions)
# NumPy (Intermediate)
#  A bank stores transaction amounts for 50 accounts across 20 days in a NumPy array.

# Task:
# Separate debit and credit transactions


# Compute daily net balance changes


# Identify accounts with continuous negative balance trends

import numpy as np
transactions = np.random.randint(-1000,1000,(50,20))

#debit card
debit = transactions[transactions<0]
print("Debit transactions: \n",debit)

#credit card
credit = transactions[transactions>0]
print("\nCredit transactions: \n",credit)

#daily net balance changes

account_balance = np.sum(transactions, axis=1)
print("\nNet balance: \n", account_balance)

# Identify accounts with continuous negative balance trends
negative_accounts = np.where(account_balance < 0)[0]
print("\nAccounts with continuous negative balance:\n", negative_accounts)
