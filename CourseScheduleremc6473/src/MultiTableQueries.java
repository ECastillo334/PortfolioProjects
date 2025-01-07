
import java.util.ArrayList;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.sql.ResultSet;



public class MultiTableQueries {
    
    private static Connection connection;
    private static PreparedStatement allClasses;
    private static ResultSet resultSet;
    
    public static ArrayList<ClassDescription> getAllClassDescriptions(String semester){
        ArrayList<ClassDescription> descriptionList = new ArrayList<ClassDescription>();
        connection = DBConnection.getConnection();
        /*
        if (connection == null){
            System.out.println("FAILED");
        }
        */
        try {
            allClasses = connection.prepareStatement("select app.class.courseCode, description, seats from app.class, app.course where semester = ? and app.class.courseCode = app.course.courseID order by app.class.courseCode");
            allClasses.setString(1, semester);
            resultSet = allClasses.executeQuery();
            while(resultSet.next()){
                descriptionList.add(new ClassDescription(resultSet.getString(1), resultSet.getString(2), resultSet.getInt(3)));
            }
        } catch (SQLException ex) {
            Logger.getLogger(MultiTableQueries.class.getName()).log(Level.SEVERE, null, ex);
            //System.out.println("FAILED catch exception");
        }

        
        //System.out.println("description list: " + descriptionList);
        return descriptionList;
    }
    
    
    public static ArrayList<StudentEntry> getScheduledStudentsByClass(String semester, String courseCode){
        connection = DBConnection.getConnection();
        ArrayList<StudentEntry> scheduledStudents = new ArrayList<StudentEntry>();
        try {
            allClasses = connection.prepareStatement("select semester, coursecode, studentid, status, timestamp  from app.schedule where semester = ? and coursecode = ? order by timestamp");
            allClasses.setString(1, semester);
            allClasses.setString(2, courseCode);
            resultSet = allClasses.executeQuery();
            while(resultSet.next()){
                if(resultSet.getString(4).equals("S")){
                    scheduledStudents.add(StudentQueries.getStudent(resultSet.getString(3)));
                }
            }
        } 
        catch (SQLException ex) {
            Logger.getLogger(MultiTableQueries.class.getName()).log(Level.SEVERE, null, ex);
        }
        return scheduledStudents;
    }
    
    public static ArrayList<StudentEntry> getWaitlistedStudentsByClass(String semester, String courseCode){
        connection = DBConnection.getConnection();
        ArrayList<StudentEntry> scheduledStudents = new ArrayList<StudentEntry>();
        try {
            allClasses = connection.prepareStatement("select semester, coursecode, studentid, status, timestamp  from app.schedule where semester = ? and coursecode = ? order by timestamp");
            allClasses.setString(1, semester);
            allClasses.setString(2, courseCode);
            resultSet = allClasses.executeQuery();
            while(resultSet.next()){
                if(resultSet.getString(4).equals("W")){
                    scheduledStudents.add(StudentQueries.getStudent(resultSet.getString(3)));
                }
            }
        } 
        catch (SQLException ex) {
            Logger.getLogger(MultiTableQueries.class.getName()).log(Level.SEVERE, null, ex);
        }
        return scheduledStudents;
    }
    
}
