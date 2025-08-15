def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or more, apply it; otherwise, return the original price.

    :param price: float - original price of the item
    :param discount_percent: float - discount percentage
    :return: float - final price after discount or original price
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"The final price is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
