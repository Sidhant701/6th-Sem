import java.sql.SQLException;
import java.util.Scanner;

public class BankApp {
    public static void main(String[] args) throws SQLException {
        System.out.println("Welcome to my Banking App\n");
        Scanner sc = new Scanner(System.in);
        while (true) {
            String menu = """
                    \n\nFollowing are the available operations of the App:
                    1.All Customer Records
                    2.Add Customer Records
                    3.Delete Customer Record
                    4.Update Customer Information
                    5.Account Details Of Customer
                    6.Loan Details Of Customer
                    7.Deposit Money To Account
                    8.Withdraw Money From Account
                    9.Exit
                    """;
            System.out.println(menu);
            System.out.print("Enter operation to be performed: ");
            int choice = sc.nextInt();
            switch (choice) {
                case 1: {
                    Customer_SQL customer = new Customer_SQL();
                    customer.showCustomerRecord();
                    break;
                }
                case 2: {
                    Customer_SQL customer = new Customer_SQL();
                    System.out.print("Enter Customer's Name: ");
                    String name = sc.next();
                    sc.nextLine();
                    System.out.print("Enter Customer's Phone Number: ");
                    String phone_no = sc.next();
                    sc.nextLine();
                    System.out.print("Enter Customer's City: ");
                    String city = sc.next();
                    sc.nextLine();
                    Customer cust = new Customer(name, phone_no, city);
                    customer.addCustomerRecord(cust);
                    break;
                }
                case 3: {
                    Customer_SQL customer = new Customer_SQL();
                    customer.deleteCustomerRecord();
                    break;
                }
                case 4: {
                    Customer_SQL customer = new Customer_SQL();
                    String menu_ = """
                            1.Update Name
                            2.Update Phone Number
                            3.Update City
                            """;
                    System.out.println(menu_);
                    System.out.print("Enter operation to be performed: ");
                    int choice_ = sc.nextInt();
                    ;
                    switch (choice_) {
                        case 1: {
                            customer.updateName();
                            break;
                        }
                        case 2: {
                            customer.updatePhoneNumber();
                            break;
                        }
                        case 3: {
                            customer.updateCity();
                            break;
                        }
                    }
                    break;
                }
                case 5: {
                    Account_SQL account = new Account_SQL();
                    account.showAccountDetails();
                    break;
                }
                case 6: {
                    Loan_SQL loan = new Loan_SQL();
                    loan.showLoanDetails();
                    break;
                }
                case 7: {
                    Transaction transaction = new Transaction();
                    transaction.deposit();
                    break;
                }
                case 8: {
                    Transaction transaction = new Transaction();
                    transaction.withdraw();
                    break;
                }
                case 9: {
                    DBConnection.getConnection().close();
                    System.exit(0);
                }
            }
        }
    }
}


