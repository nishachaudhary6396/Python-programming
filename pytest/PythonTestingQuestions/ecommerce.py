
def calculate_total(items, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Invalid tax rate")
    
    for price in items:
        if price < 0:
            raise ValueError("price can not be negative")
    total = sum(items)
    return total + (total * tax_rate)
    
