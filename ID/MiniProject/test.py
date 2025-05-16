import cx_Oracle
import sys

# Establish connection
conn = cx_Oracle.connect("<user>", "<password>", "172.17.144.110:1521/ora11g")
cur = conn.cursor()

def show_customers():
    cur.execute("SELECT * FROM customer")
    rows = cur.fetchall()
    print("\nCustomer Records:")
    for row in rows:
        print(row)

def add_customer():
    cust_no = input("Enter Customer Number: ")
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")
    cur.execute("INSERT INTO customer VALUES (:1, :2, :3, :4)", (cust_no, name, phone, city))
    conn.commit()
    print("Customer added successfully!")
    show_customers()

def delete_customer():
    cust_no = input("Enter Customer Number to delete: ")
    cur.execute("DELETE FROM customer WHERE cust_no = :1", (cust_no,))
    conn.commit()
    print("Customer deleted successfully!")
    show_customers()

def update_customer():
    cust_no = input("Enter Customer Number to update: ")
    print("Choose field to update: 1. Name  2. Phone  3. City")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter new name: ")
        cur.execute("UPDATE customer SET name = :1 WHERE cust_no = :2", (name, cust_no))
    elif choice == 2:
        phone = input("Enter new phone: ")
        cur.execute("UPDATE customer SET phoneno = :1 WHERE cust_no = :2", (phone, cust_no))
    elif choice == 3:
        city = input("Enter new city: ")
        cur.execute("UPDATE customer SET city = :1 WHERE cust_no = :2", (city, cust_no))
    else:
        print("Invalid choice.")
        return
    conn.commit()
    print("Customer updated successfully!")
    show_customers()

def show_account_details():
    cust_no = input("Enter Customer Number: ")
    cur.execute("""
        SELECT c.*, a.account_no, a.type, a.balance, b.branch_code, b.branch_name, b.branch_city
        FROM customer c
        JOIN account a ON c.cust_no = a.cust_no
        JOIN branch b ON a.branch_code = b.branch_code
        WHERE c.cust_no = :1
    """, (cust_no,))
    for row in cur.fetchall():
        print(row)

def show_loan_details():
    cust_no = input("Enter Customer Number: ")
    cur.execute("""
        SELECT c.*, l.loan_no, l.amount, b.branch_code, b.branch_name, b.branch_city
        FROM customer c
        JOIN loan l ON c.cust_no = l.cust_no
        JOIN branch b ON l.branch_code = b.branch_code
        WHERE c.cust_no = :1
    """, (cust_no,))
    rows = cur.fetchall()
    if not rows:
        print("Congratulations! No loans found for this customer.")
    else:
        for row in rows:
            print(row)

def deposit_money():
    account_no = input("Enter Account Number: ")
    amount = float(input("Enter amount to deposit: "))
    cur.execute("UPDATE account SET balance = balance + :1 WHERE account_no = :2", (amount, account_no))
    conn.commit()
    print("Amount deposited successfully!")
    show_account_details()

def withdraw_money():
    account_no = input("Enter Account Number: ")
    amount = float(input("Enter amount to withdraw: "))
    cur.execute("SELECT balance FROM account WHERE account_no = :1", (account_no,))
    row = cur.fetchone()
    if row and row[0] >= amount:
        cur.execute("UPDATE account SET balance = balance - :1 WHERE account_no = :2", (amount, account_no))
        conn.commit()
        print("Amount withdrawn successfully!")
        show_account_details()
    else:
        print("Insufficient balance.")

def main_menu():
    while True:
        print("\n***** Banking Management System *****")
        print("1. Show Customer Records")
        print("2. Add Customer Record")
        print("3. Delete Customer Record")
        print("4. Update Customer Information")
        print("5. Show Account Details of a Customer")
        print("6. Show Loan Details of a Customer")
        print("7. Deposit Money to an Account")
        print("8. Withdraw Money from an Account")
        print("9. Exit the Program")
        
        try:
            choice = int(input("Enter your choice (1-9): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            show_customers()
        elif choice == 2:
            add_customer()
        elif choice == 3:
            delete_customer()
        elif choice == 4:
            update_customer()
        elif choice == 5:
            show_account_details()
        elif choice == 6:
            show_loan_details()
        elif choice == 7:
            deposit_money()
        elif choice == 8:
            withdraw_money()
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        main_menu()
    finally:
        cur.close()
        conn.close()
