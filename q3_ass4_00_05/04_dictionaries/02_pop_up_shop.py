def main():
  
    fruit_prices = {
        "apple": 1.5,
        "durian": 5.0,
        "jackfruit": 80.,
        "kiwi": 1,
        "rambutan": 1.5,
        "mango": 5
    }

    total_cost = 0  

    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: ")) 
        total_cost += quantity * price

    print(f"\nYour total is ${total_cost:.2f}") 

if __name__ == '__main__':
    main()