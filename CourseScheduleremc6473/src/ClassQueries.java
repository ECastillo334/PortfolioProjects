
import java.security.Timestamp;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;


public class ClassQueries {
    
    private static Connection connection;
    private static ArrayList<String> faculty = new ArrayList<String>();
    private static PreparedStatement addClass;
    private static PreparedStatement getSemesterList;
    private static ResultSet resultSet;
    
    public static void addClass(ClassEntry Class){
        connection = DBConnection.getConnection();
        try
        {
            addClass = connection.prepareStatement("insert into app.class (coursecode, seats, semester) values (?, ?, ?)");
            addClass.setString(1, Class.getCourseCode());
            addClass.setInt(2, Class.getSeats());
            addClass.setString(3, Class.getSemester());
            addClass.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
    }
    
    public static ArrayList<String> getAllCourseCodes(String semester){
        connection = DBConnection.getConnection();
        ArrayList<String> allCourseCodes = new ArrayList<String>();
        try
        {
            getSemesterList = connection.prepareStatement("select coursecode, semester from app.class order by coursecode");
            resultSet = getSemesterList.executeQuery();
            
            while(resultSet.next())
            {
                if(resultSet.getString(2).equals(semester)){
                   allCourseCodes.add(resultSet.getString(1)); 
                }
                
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
        return allCourseCodes;
    }
    
    public static int getClassSeats(String semester, String courseCode){
        connection = DBConnection.getConnection();
        int courseSeats = 0;
        try
        {
            getSemesterList = connection.prepareStatement("select coursecode, seats, semester from app.class order by coursecode");
            resultSet = getSemesterList.executeQuery();
            
            while(resultSet.next())
            {
                if(resultSet.getString(1).equals(courseCode) && resultSet.getString(3).equals(semester)){
                    return resultSet.getInt(2);
                }
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
        return courseSeats;
    }
    
    
    public static void dropClass(String semester, String courseCode){
        connection = DBConnection.getConnection();
        try
        {
            getSemesterList = connection.prepareStatement("DELETE FROM app.class where coursecode = ? AND semester = ?");
            
            
            getSemesterList.setString(1, courseCode);
            getSemesterList.setString(2, semester);
            getSemesterList.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
    }
    
}
