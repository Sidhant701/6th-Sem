import java.sql.*;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Connection con = null;
        Statement stmt = null;
        Scanner sc = new Scanner(System.in);

        try {
            // Load driver
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // Establish connection
            String conurl = "jdbc:oracle:thin:@172.17.144.110:1521:ora11g";
            con = DriverManager.getConnection(conurl, "<user>", "<password>");
            stmt = con.createStatement();

            int choice;

            do {
                System.out.println("\n***** Banking Management System *****");
                System.out.println("1. Show Customer Records");
                System.out.println("2. Add Customer Record");
                System.out.println("3. Delete Customer Record");
                System.out.println("4. Update Customer Information");
                System.out.println("5. Show Account Details of a Customer");
                System.out.println("6. Show Loan Details of a Customer");
                System.out.println("7. Deposit Money to an Account");
                System.out.println("8. Withdraw Money from an Account");
                System.out.println("9. Exit");
                System.out.print("Enter your choice (1-9): ");
                choice = sc.nextInt();
                sc.nextLine(); // consume newline

                switch (choice) {
                    case 1:
                        ResultSet rs1 = stmt.executeQuery("SELECT * FROM customer");
                        System.out.println("Customer Records:");
                        while (rs1.next()) {
                            System.out.printf("%s %s %s %s\n", rs1.getString(1), rs1.getString(2),
                                    rs1.getString(3), rs1.getString(4));
                        }
                        break;

                    case 2:
                        System.out.print("Enter Customer Number: ");
                        String cno = sc.nextLine();
                        System.out.print("Enter Name: ");
                        String name = sc.nextLine();
                        System.out.print("Enter Phone Number: ");
                        String phone = sc.nextLine();
                        System.out.print("Enter City: ");
                        String city = sc.nextLine();
                        stmt.executeUpdate("INSERT INTO customer VALUES('" + cno + "','" + name + "','" + phone + "','" + city + "')");
                        System.out.println("Customer Added.");
                        break;

                    case 3:
                        System.out.print("Enter Customer Number to delete: ");
                        String delcno = sc.nextLine();
                        stmt.executeUpdate("DELETE FROM customer WHERE cust_no='" + delcno + "'");
                        System.out.println("Customer Deleted.");
                        break;

                    case 4:
                        System.out.print("Enter Customer Number to update: ");
                        String upcno = sc.nextLine();
                        System.out.println("1. Name  2. Phone No  3. City");
                        int upchoice = sc.nextInt();
                        sc.nextLine();
                        if (upchoice == 1) {
                            System.out.print("Enter new Name: ");
                            String newName = sc.nextLine();
                            stmt.executeUpdate("UPDATE customer SET name='" + newName + "' WHERE cust_no='" + upcno + "'");
                        } else if (upchoice == 2) {
                            System.out.print("Enter new Phone: ");
                            String newPhone = sc.nextLine();
                            stmt.executeUpdate("UPDATE customer SET phoneno='" + newPhone + "' WHERE cust_no='" + upcno + "'");
                        } else if (upchoice == 3) {
                            System.out.print("Enter new City: ");
                            String newCity = sc.nextLine();
                            stmt.executeUpdate("UPDATE customer SET city='" + newCity + "' WHERE cust_no='" + upcno + "'");
                        }
                        System.out.println("Customer Updated.");
                        break;

                    case 5:
                        System.out.print("Enter Customer Number: ");
                        String accCno = sc.nextLine();
                        ResultSet rs5 = stmt.executeQuery(
                                "SELECT c.*, a.account_no, a.type, a.balance, b.branch_code, b.branch_name, b.branch_city " +
                                "FROM customer c JOIN account a ON c.cust_no = a.cust_no " +
                                "JOIN branch b ON a.branch_code = b.branch_code " +
                                "WHERE c.cust_no = '" + accCno + "'");
                        while (rs5.next()) {
                            System.out.printf("%s %s %s %s %s %s %.2f %s %s %s\n",
                                    rs5.getString(1), rs5.getString(2), rs5.getString(3), rs5.getString(4),
                                    rs5.getString(5), rs5.getString(6), rs5.getDouble(7),
                                    rs5.getString(8), rs5.getString(9), rs5.getString(10));
                        }
                        break;

                    case 6:
                        System.out.print("Enter Customer Number: ");
                        String loanCno = sc.nextLine();
                        ResultSet rs6 = stmt.executeQuery(
                                "SELECT c.*, l.loan_no, l.amount, b.branch_code, b.branch_name, b.branch_city " +
                                "FROM customer c JOIN loan l ON c.cust_no = l.cust_no " +
                                "JOIN branch b ON l.branch_code = b.branch_code " +
                                "WHERE c.cust_no = '" + loanCno + "'");
                        if (!rs6.next()) {
                            System.out.println("Congratulations! No loans found.");
                        } else {
                            do {
                                System.out.printf("%s %s %s %s %s %.2f %s %s %s\n",
                                        rs6.getString(1), rs6.getString(2), rs6.getString(3), rs6.getString(4),
                                        rs6.getString(5), rs6.getDouble(6), rs6.getString(7), rs6.getString(8),
                                        rs6.getString(9));
                            } while (rs6.next());
                        }
                        break;

                    case 7:
                        System.out.print("Enter Account Number: ");
                        String dacc = sc.nextLine();
                        System.out.print("Enter amount to deposit: ");
                        double damt = sc.nextDouble();
                        stmt.executeUpdate("UPDATE account SET balance = balance + " + damt + " WHERE account_no='" + dacc + "'");
                        System.out.println("Amount Deposited.");
                        break;

                    case 8:
                        System.out.print("Enter Account Number: ");
                        String wacc = sc.nextLine();
                        System.out.print("Enter amount to withdraw: ");
                        double wamt = sc.nextDouble();
                        ResultSet rs8 = stmt.executeQuery("SELECT balance FROM account WHERE account_no='" + wacc + "'");
                        if (rs8.next()) {
                            double bal = rs8.getDouble(1);
                            if (bal >= wamt) {
                                stmt.executeUpdate("UPDATE account SET balance = balance - " + wamt + " WHERE account_no='" + wacc + "'");
                                System.out.println("Amount Withdrawn.");
                            } else {
                                System.out.println("Insufficient balance!");
                            }
                        }
                        break;

                    case 9:
                        System.out.println("Exiting program.");
                        break;

                    default:
                        System.out.println("Invalid choice.");
                }

            } while (choice != 9);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try { if (stmt != null) stmt.close(); } catch (Exception e) {}
            try { if (con != null) con.close(); } catch (Exception e) {}
            sc.close();
        }
    }
}
