public class Customer {
    private int customerNo;
    private String name;
    private String phoneNo;
    private String city;

    public Customer(String name, String phoneNo, String city) {
        this.name = name;
        this.phoneNo = phoneNo;
        this.city = city;
    }

    public void setCustomerNo(int customerNo) {
        this.customerNo = customerNo;
    }

    public int getCustomerNo() {
        return this.customerNo;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setPhoneNo(String phoneNo) {
        this.phoneNo = phoneNo;
    }

    public String getPhoneNo() {
        return this.phoneNo;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getCity() {
        return this.city;
    }
}