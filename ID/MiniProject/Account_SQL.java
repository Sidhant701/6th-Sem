import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class Account_SQL {
    private final Connection connection;
    public Account_SQL() throws SQLException {
        connection = DBConnection.getConnection();
    }

    public void showAccountDetails() {
        try {
            String query = """
                    SELECT
                    c.CUST_NO, c.NAME, c.PHONENO, c.CITY,
                    a.ACCOUNT_NO, a.TYPE, a.BALANCE,
                    b.BRANCH_CODE, b.BRANCH_NAME, b.BRANCH_CITY
                    FROM CUSTOMER_RECORD c
                    JOIN ACCOUNT_DETAILS a ON c.CUST_NO = a.CUST_NO
                    JOIN BRANCH b ON a.BRANCH_CODE = b.BRANCH_CODE
                    WHERE c.CUST_NO = ?;
                    """;
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter The Customer Number for Account Details: ");
            preparedStatement.setInt(1, sc.nextInt());
            sc.nextLine();
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                System.out.println("Customer's Account & Branch information:-\n");
                System.out.println("Customer Number: " + resultSet.getInt(1));
                System.out.println("Name: " + resultSet.getString(2));
                System.out.println("Phone Number: " + resultSet.getString(3));
                System.out.println("City: " + resultSet.getString(4));
                System.out.println("Account Number: " + resultSet.getInt(5));
                System.out.println("Account Type: " + resultSet.getString(6));
                System.out.println("Account Balance: " + resultSet.getDouble(7));
                System.out.println("Branch Code: " + resultSet.getString(8));
                System.out.println("Branch Name: " + resultSet.getString(9));
                System.out.println("Branch City: " + resultSet.getString(10));
            }
            else
                System.out.println("No Such Customer Exist!!");
            sc.close();
        }
        catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}