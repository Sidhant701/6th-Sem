import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class test2 {
    public static void main(String[] args) {
        Connection con = null;
        Statement stmt = null;

        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String conurl = "jdbc:sqlserver://172.17.144.108;databaseName=S1941012407";
            con = DriverManager.getConnection(conurl, "S1941012407", "Iter1234#");
            System.out.println("Connection is established");
            stmt = con.createStatement();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int ch = 0;

            do {
                System.out.println("\n\n***** Banking Management System *****");
                System.out.println("1. Show Customer Records");
                System.out.println("2. Add Customer Record");
                System.out.println("3. Delete Customer Record");
                System.out.println("4. Update Customer Record");
                System.out.println("5. Show Account Details of a Customer");
                System.out.println("6. Show Loan Details of a Customer");
                System.out.println("7. Deposit Money to an Account");
                System.out.println("8. Withdraw Money from an Account");
                System.out.println("9. Exit the Program");
                System.out.print("Enter your choice (1-9): ");
                ch = Integer.parseInt(br.readLine());

                switch (ch) {
                    case 1:
                        ResultSet rs = stmt.executeQuery("SELECT * FROM CUSTOMER");
                        int a = 0;
                        while (rs.next()) {
                            System.out.print("\n" + rs.getString("CUST_NO") + "\t");
                            System.out.print(rs.getString("NAME") + "\t");
                            System.out.print(rs.getString("PHONE_NO") + "\t");
                            System.out.print(rs.getString("CITY"));
                            a++;
                        }
                        System.out.println("\nThe number of rows selected is " + a);
                        break;

                    case 2:
                        System.out.print("Enter cust_no: ");
                        String cust_no = br.readLine();
                        System.out.print("Enter the name: ");
                        String name = br.readLine();
                        System.out.print("Enter the phone: ");
                        long phone = Long.parseLong(br.readLine());
                        System.out.print("Enter the city: ");
                        String city = br.readLine();
                        String insertstmt = "INSERT INTO customer VALUES('" + cust_no + "','" + name + "','" + phone + "','" + city + "')";
                        int n = stmt.executeUpdate(insertstmt);
                        System.out.println(n + " Row Inserted");
                        break;

                    case 3:
                        System.out.print("Enter a cust_no for deletion: ");
                        String cust = br.readLine();
                        String deletestmt = "DELETE FROM customer WHERE cust_no='" + cust + "'";
                        n = stmt.executeUpdate(deletestmt);
                        System.out.println(n + " Row deleted");
                        break;

                    case 4:
                        System.out.println("Enter 1: For Name 2: For Phone no 3: For City to update:");
                        int c1 = Integer.parseInt(br.readLine());
                        System.out.print("Enter Cust No: ");
                        cust_no = br.readLine();

                        switch (c1) {
                            case 1:
                                System.out.print("Enter updated name: ");
                                String updatedName = br.readLine();
                                n = stmt.executeUpdate("UPDATE Customer SET Name = '" + updatedName + "' WHERE Cust_no = '" + cust_no + "'");
                                System.out.println(n + " Updated Successfully");
                                break;

                            case 2:
                                System.out.print("Enter updated Phone: ");
                                long updatedPhone = Long.parseLong(br.readLine());
                                n = stmt.executeUpdate("UPDATE Customer SET Phone_No = '" + updatedPhone + "' WHERE Cust_no = '" + cust_no + "'");
                                System.out.println(n + " Updated Successfully");
                                break;

                            case 3:
                                System.out.print("Enter updated City: ");
                                String updatedCity = br.readLine();
                                n = stmt.executeUpdate("UPDATE Customer SET City = '" + updatedCity + "' WHERE Cust_no = '" + cust_no + "'");
                                System.out.println(n + " Updated Successfully");
                                break;

                            default:
                                System.out.println("Invalid update choice.");
                        }
                        break;

                    case 5:
                        System.out.print("Enter Cust No: ");
                        cust_no = br.readLine();
                        String queryAccount = "SELECT A.ACCOUNT_NO, A.TYPE, A.BALANCE, B.BRANCH_CODE, B.BRANCH_NAME, B.BRANCH_CITY " +
                                "FROM ACCOUNT A, BRANCH B, CUSTOMER C, DEPOSITOR D " +
                                "WHERE D.ACCOUNT_NO = A.ACCOUNT_NO AND A.BRANCH_CODE = B.BRANCH_CODE " +
                                "AND C.CUST_NO = D.CUST_NO AND C.CUST_NO = '" + cust_no + "'";
                        rs = stmt.executeQuery(queryAccount);
                        System.out.format("Acc. No.: \tType: \tBalance: \tBranch Code: \tBranch Name: \t\tBranch City:\n");
                        while (rs.next()) {
                            System.out.format("%s \t\t%s \t %.2f\t\t %s\t\t %s\t\t%s\n",
                                    rs.getString("ACCOUNT_NO"),
                                    rs.getString("TYPE"),
                                    rs.getDouble("BALANCE"),
                                    rs.getString("BRANCH_CODE"),
                                    rs.getString("BRANCH_NAME"),
                                    rs.getString("BRANCH_CITY"));
                        }
                        break;

                    case 6:
                        System.out.print("Enter Cust No: ");
                        cust_no = br.readLine();
                        String queryLoan = "SELECT C.*, L.LOAN_NO, L.AMOUNT, B.* FROM LOAN L, CUSTOMER C, BRANCH B " +
                                "WHERE L.BRANCH_CODE = B.BRANCH_CODE AND C.CUST_NO = L.CUST_NO AND C.CUST_NO = '" + cust_no + "'";
                        rs = stmt.executeQuery(queryLoan);
                        while (rs.next()) {
                            System.out.format("%s %s %s %s %s %.2f %s %s %s\n",
                                    rs.getString("CUST_NO"),
                                    rs.getString("NAME"),
                                    rs.getString("PHONE_NO"),
                                    rs.getString("CITY"),
                                    rs.getString("LOAN_NO"),
                                    rs.getDouble("AMOUNT"),
                                    rs.getString("BRANCH_CODE"),
                                    rs.getString("BRANCH_NAME"),
                                    rs.getString("BRANCH_CITY"));
                        }
                        break;

                    case 7:
                        System.out.print("Enter Account No: ");
                        String acc_no = br.readLine();
                        System.out.print("Enter the amount to deposit: ");
                        long amt = Long.parseLong(br.readLine());
                        String queryDeposit = "UPDATE ACCOUNT SET BALANCE = BALANCE + " + amt + " WHERE ACCOUNT_NO = '" + acc_no + "'";
                        n = stmt.executeUpdate(queryDeposit);
                        System.out.println(n + " Balance Updated");
                        break;

                    case 8:
                        System.out.print("Enter Account No: ");
                        acc_no = br.readLine();
                        System.out.print("Enter the amount to withdraw: ");
                        amt = Long.parseLong(br.readLine());
                        String queryBalance = "SELECT BALANCE FROM ACCOUNT WHERE ACCOUNT_NO = '" + acc_no + "'";
                        rs = stmt.executeQuery(queryBalance);
                        if (rs.next()) {
                            long bal = rs.getLong("BALANCE");
                            if (amt <= bal) {
                                String queryWithdraw = "UPDATE ACCOUNT SET BALANCE = BALANCE - " + amt + " WHERE ACCOUNT_NO = '" + acc_no + "'";
                                n = stmt.executeUpdate(queryWithdraw);
                                System.out.println(n + " Balance Updated");
                            } else {
                                System.out.println("Insufficient balance");
                            }
                        }
                        break;

                    case 9:
                        System.out.println("Visit us next time!");
                        stmt.close();
                        con.close();
                        System.exit(0);
                        break;

                    default:
                        System.out.println("Enter from 1 to 9 only.");
                }

            } while (ch != 9);
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
