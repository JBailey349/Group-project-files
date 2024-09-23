

    # Input employee ID
        employee_id = int(input("Enter employee's ID: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric ID.")
        return

    # Input number of dependents
        num_dependents = int(input("Enter number of dependents: "))

    # Input hours worked
        hours_worked = float(input("Enter hours worked: "))

    # Retrieve hourly rate from the "database"
    hourly_rate = fetch_hourly_rate(employee_id)

    # Output the entered information and fetched hourly rate
    print(f"\nEmployee Details:\nFirst Name: {first_name}\nLast Name: {last_name}")
    print(f"Employee ID: {employee_id}\nDependents: {num_dependents}")
    print(f"Hours Worked: {hours_worked}\nHourly Rate: ${hourly_rate:.2f}")





employee_id = input("ID to Run: ")

query_index = employee_id
record = [0,0,0]
record = query_response

dependents = record[0]
hoursWorked = record[1]
hourlyRate = record[2]
