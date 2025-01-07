

public class StudentEntry {
    
    private String firstName;
    private String lastName;
    private String studentID;

    public StudentEntry(String firstName, String lastName, String ID) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.studentID = ID;
    }
    
    public String getFirstName(){
        return firstName;
    }
    
    public String getLastName(){
        return lastName;
    }
    
    public String getStudentID(){
        return studentID;
    }
    /*
    @Override
    public String toString(){
        return getFirstName() + " " + getLastName();
    }
    */
}
