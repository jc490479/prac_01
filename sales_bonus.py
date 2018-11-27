"""  Program to calculate and display a user's bonus based on sales. If sales are under $1,000, the user gets a 10% bonus. If sales are $1,000 or over, the bonus is 15%. """
def main():
    sales = float(input("input a sales:"))
    while sales >= 0:
        if sales < 1000:
            # sales = float(input("Enter sales: $"))
            bonus = sales * 0.1
            print("the bonus is", bonus)
        else:
            # sales = float(input("Enter sales: $"))
            bonus = sales * 0.15
            print("the bonus is", bonus)
        sales = float(input("input a sales:"))

main()