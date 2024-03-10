def calculate_discount(price, discount_percent):
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    if discount_percent > 20:
        final_price = price - (discount_percent / 100 * price)
        print(f"Your final price is {final_price} after applying your discount of {discount_percent}%")
    elif discount_percent <= 20:
        print(f"Your final price is {price} since no discount was applied")

# Example usage
calculate_discount(0, 0)
