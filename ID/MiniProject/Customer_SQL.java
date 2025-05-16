import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Customer_SQL {
    private final Connection connection;

    public Customer_SQL() throws SQLException {
        connection = DBConnection.getConnection();
    }

    public void showCustomerRecord() {
        try {
            String query = "SELECT * FROM customer_record";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);
            while (resultSet.next()) {
                System.out.println("\n\nCustomer Number :" + resultSet.getInt(1));
                System.out.println("Name :" + resultSet.getString(2));
                System.out.println("Phone Number :" + resultSet.getString(3));
                System.out.println("City :" + resultSet.getString(4));
            }
            connection.close();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    public void addCustomerRecord(Customer customer) {
        try {
            String query = "INSERT INTO customer_record (cust_no, name, phoneno, city) VALUES(?, ?, ?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            String custQuery = "SELECT MAX(cust_no) FROM CUSTOMER_RECORD";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(custQuery);
            int customer_no = 1000;
            if (resultSet.next()) {
                customer_no = resultSet.getInt(1) + 1;
            }
            customer.setCustomerNo(customer_no);
            preparedStatement.setInt(1, customer_no);
            Scanner sc = new Scanner(System.in);
            preparedStatement.setString(2, customer.getName());
            preparedStatement.setString(3, customer.getPhoneNo());
            preparedStatement.setString(4, customer.getCity());
            int rows_affected = preparedStatement.executeUpdate();
            if (rows_affected > 0) {
                System.out.println("Record Successfully Created!!");
            } else
                System.out.println("Record Creation Unsuccessful, There was an error!!");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        this.showCustomerRecord();
    }

    public void deleteCustomerRecord() {
        try {
            String query = "DELETE FROM customer_record WHERE cust_no = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter Customer Number of the record to be deleted: ");
            preparedStatement.setInt(1, sc.nextInt());
            sc.nextLine();
            int rows_affected = preparedStatement.executeUpdate();
            if (rows_affected > 0) {
                System.out.println("Record Successfully Deleted!!");
            } else
                System.out.println("Record Deletion Unsuccessful, There was an error!!");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        this.showCustomerRecord();
    }

    public void updateName() {
        try {
            String query = "UPDATE customer_record SET name = ? WHERE cust_no = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter the Customer Number: ");
            preparedStatement.setInt(2, sc.nextInt());
            sc.nextLine();
            System.out.print("Enter the name(update): ");
            preparedStatement.setString(1, sc.nextLine());
            int rows_affected = preparedStatement.executeUpdate();
            if (rows_affected > 0) {
                System.out.println("Record Updated Deleted!!");
            } else
                System.out.println("Record not updated, There was an error!!");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        this.showCustomerRecord();
    }

    public void updatePhoneNumber() {
        try {
            String query = "UPDATE customer_record SET phoneno = ? WHERE cust_no = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter Customer Number: ");
            preparedStatement.setInt(2, sc.nextInt());
            sc.nextLine();
            System.out.print("Enter Phone Number(update): ");
            preparedStatement.setString(1, sc.nextLine());
            int rows_affected = preparedStatement.executeUpdate();
            if (rows_affected > 0) {
                System.out.println("Record Updated Deleted!!");
            } else
                System.out.println("Record not updated, There was an error!!");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        this.showCustomerRecord();
    }

    public void updateCity() {
        try {
            String query = "UPDATE customer_record SET city = ? WHERE cust_no = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter Customer Number: ");
            preparedStatement.setInt(2, sc.nextInt());
            sc.nextLine();
            System.out.print("Enter City(update): ");
            preparedStatement.setString(1, sc.nextLine());
            int rows_affected = preparedStatement.executeUpdate();
            if (rows_affected > 0) {
                System.out.println("Record Updated Deleted!!");
            } else
                System.out.println("Record not updated, There was an error!!");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        this.showCustomerRecord();
    }
}