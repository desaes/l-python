for value in range(1,11):
    print(value)


cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    # This block will be executed if no errors, no breaks happens.
    # This else can be applied to while also
    print("All cars built successfully. No faulty cars!")