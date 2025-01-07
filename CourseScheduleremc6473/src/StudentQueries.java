import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;


public class StudentQueries {
    
    private static Connection connection;
    private static ArrayList<String> faculty = new ArrayList<String>();
    private static PreparedStatement addStudent;
    private static PreparedStatement getStudentList;
    private static ResultSet resultSet;
    
    public static void addStudent(StudentEntry student){
        connection = DBConnection.getConnection();
        try
        {
            addStudent = connection.prepareStatement("insert into app.student (firstname, lastname, studentid) values (?, ?, ?)");
            addStudent.setString(1, student.getFirstName());
            addStudent.setString(2, student.getLastName());
            addStudent.setString(3, student.getStudentID());
            addStudent.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
    }
    
    public static ArrayList<StudentEntry> getAllStudents(){
        connection = DBConnection.getConnection();
        ArrayList<StudentEntry> studentList = new ArrayList<StudentEntry>();
        try
        {
            getStudentList = connection.prepareStatement("select firstname, lastname, studentid from app.student order by lastname");
            resultSet = getStudentList.executeQuery();
            
            while(resultSet.next())
            {
                studentList.add(new StudentEntry(resultSet.getString(1), resultSet.getString(2), resultSet.getString(3)));
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
        return studentList;
    }
    
    
    public static StudentEntry getStudent(String studentID){
        connection = DBConnection.getConnection();
        try
        {
            getStudentList = connection.prepareStatement("select firstname, lastname, studentid from app.student order by lastname");
            resultSet = getStudentList.executeQuery();
            
            while(resultSet.next())
            {
                if(resultSet.getString(3).equals(studentID)){
                    return new StudentEntry(resultSet.getString(1), resultSet.getString(2), resultSet.getString(3));
                }
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
        return null;
        
    }
    
    public static void dropStudent(String studentID){
        connection = DBConnection.getConnection();
        try
        {
            getStudentList = connection.prepareStatement("DELETE FROM app.student where studentID = ?");
            getStudentList.setString(1, studentID);
            getStudentList.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        } 
    }
    
}
