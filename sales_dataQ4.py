from collections import defaultdict

# Sample sales data
sales_data = [
    {
        "customer": "Alice",
        "date": "2023-09-15",
        "items": [
            {"item": "Widget A", "quantity": 2, "price": 10.99},
            {"item": "Widget B", "quantity": 1, "price": 12.99},
        ],
    },
    # Add more sales data here...
]

def calculate_total_sales(start_date, end_date):
    total_sales = 0.0
    for sale in sales_data:
        sale_date = sale["date"]
        if start_date <= sale_date <= end_date:
            for item in sale["items"]:
                total_sales += item["quantity"] * item["price"]
    return total_sales

def top_selling_item():
    item_counts = defaultdict(int)
    for sale in sales_data:
        for item in sale["items"]:
            item_name = item["item"]
            item_counts[item_name] += item["quantity"]
    
    top_items = [item for item, count in item_counts.items() if count == max(item_counts.values())]
    return top_items

def most_frequent_customer():
    customer_counts = defaultdict(int)
    for sale in sales_data:
        customer_name = sale["customer"]
        customer_counts[customer_name] += 1
    
    most_frequent = max(customer_counts, key=customer_counts.get)
    return most_frequent

def customer_who_spent_the_most():
    customer_spending = defaultdict(float)
    for sale in sales_data:
        customer_name = sale["customer"]
        sale_total = sum(item["quantity"] * item["price"] for item in sale["items"])
        customer_spending[customer_name] += sale_total
    
    top_customer = max(customer_spending, key=customer_spending.get)
    return top_customer

def total_revenue_by_item():
    item_revenue = defaultdict(float)
    for sale in sales_data:
        for item in sale["items"]:
            item_name = item["item"]
            item_total = item["quantity"] * item["price"]
            item_revenue[item_name] += item_total
    
    return dict(item_revenue)

def date_with_highest_sales_revenue():
    date_revenue = defaultdict(float)
    for sale in sales_data:
        sale_date = sale["date"]
        sale_total = sum(item["quantity"] * item["price"] for item in sale["items"])
        date_revenue[sale_date] += sale_total
    
    highest_revenue_date = max(date_revenue, key=date_revenue.get)
    return highest_revenue_date

def main():
    while True:
        print("\nMenu:")
        print("1. Total Sales Revenue for Date Range")
        print("2. Top-Selling Item")
        print("3. Most Frequent Customer")
        print("4. Customer Who Spent the Most")
        print("5. Total Revenue by Item")
        print("6. Date with Highest Sales Revenue")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            total_sales = calculate_total_sales(start_date, end_date)
            print(f"Total sales revenue for the specified date range: ${total_sales:.2f}")
        elif choice == "2":
            top_items = top_selling_item()
            print("Top-selling item(s):", ", ".join(top_items))
        elif choice == "3":
            frequent_customer = most_frequent_customer()
            print(f"Most frequent customer: {frequent_customer}")
        elif choice == "4":
            top_spending_customer = customer_who_spent_the_most()
            print(f"Customer who spent the most: {top_spending_customer}")
        elif choice == "5":
            item_revenue = total_revenue_by_item()
            for item, revenue in item_revenue.items():
                print(f"{item}: ${revenue:.2f}")
        elif choice == "6":
            highest_revenue_date = date_with_highest_sales_revenue()
            print(f"Date with the highest sales revenue: {highest_revenue_date}")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")

if __name__ == "__main__":
    main()
