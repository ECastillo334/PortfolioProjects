


import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.util.ArrayList;



public class ScheduleQueries {
    
    private static Connection connection;
    private static PreparedStatement addSchedule;
    private static PreparedStatement getScheduleList;
    private static ResultSet resultSet;
    private static ArrayList<String> faculty = new ArrayList<String>();
    
    
    
    public static void addScheduleEntry(ScheduleEntry entry){
        connection = DBConnection.getConnection();
        try
        {
            addSchedule = connection.prepareStatement("insert into app.schedule (semester, coursecode, studentid, status, timestamp) values (?, ?, ?, ?, ?)");
            addSchedule.setString(1, entry.getSemester());
            addSchedule.setString(2, entry.getCourseCode());
            addSchedule.setString(3, entry.getStudentID());
            addSchedule.setString(4, entry.getStatus());
            addSchedule.setTimestamp(5, (Timestamp) entry.getTimestamp());
            addSchedule.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
    }
    
    
    public static ArrayList<ScheduleEntry> getScheduleByStudent(String semester, String studentID){
        connection = DBConnection.getConnection();
        ArrayList<ScheduleEntry> entries = new ArrayList<ScheduleEntry>();
        try
        {
            getScheduleList = connection.prepareStatement("select semester, coursecode, studentid, status, timestamp  from app.schedule");
            resultSet = getScheduleList.executeQuery();
            
            while(resultSet.next()){
                //System.out.println("result: " + resultSet.getString(3));
                //System.out.println("input: " + studentID);
                if(studentID.equals(resultSet.getString(3)) && semester.equals(resultSet.getString(1))){
                    //System.out.println("Triggered");
                    entries.add(new ScheduleEntry(resultSet.getString(4), resultSet.getTimestamp(5), resultSet.getString(1), resultSet.getString(2), resultSet.getString(3)));
                }
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        return entries;
        
    }
    
    public static int getScheduledStudentCount(String semester, String courseCode){
        connection = DBConnection.getConnection();
        int studentCount = 0;
        try
        {
            getScheduleList = connection.prepareStatement("select count(studentID) from app.schedule where semester = ? and courseCode = ? and status = 'S' ");
            getScheduleList.setString(1, semester);
            getScheduleList.setString(2, courseCode);
            resultSet = getScheduleList.executeQuery();
            while(resultSet.next())
            {
                //DEBUG:
                //System.out.println(resultSet.getInt(1));
                studentCount = resultSet.getInt(1);
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
        return studentCount;
    }
    
    
    public static ArrayList<ScheduleEntry> getWaitlistedStudentsByClass(String semester, String courseCode){
        connection = DBConnection.getConnection();
        ArrayList<ScheduleEntry> Waitlisted = new ArrayList<ScheduleEntry>();
        try
        {
            getScheduleList = connection.prepareStatement("select status, timestamp, semester, coursecode, studentid from app.schedule where semester = ? and courseCode = ? order by timestamp");
            getScheduleList.setString(1, semester);
            getScheduleList.setString(2, courseCode);
            resultSet = getScheduleList.executeQuery();
            while(resultSet.next())
            {
                if(resultSet.getString(1).equals("W")){
                    Waitlisted.add(new ScheduleEntry(resultSet.getString(1), resultSet.getTimestamp(2), resultSet.getString(3), resultSet.getString(4), resultSet.getString(5)));
                }
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        return Waitlisted;
    }
    
    public static void dropStudentScheduleByCourse(String semester, String studentID, String courseCode){
        connection = DBConnection.getConnection();
        try
        {
            getScheduleList = connection.prepareStatement("DELETE FROM app.schedule where semester = ? AND studentID = ? AND courseCode = ?");
            getScheduleList.setString(1, semester);
            getScheduleList.setString(2, studentID);
            getScheduleList.setString(3, courseCode);
            getScheduleList.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
    }
    
    
    public static void dropScheduleByCourse(String semester, String courseCode){
        //Goes through the schedule database and deletes all entries that include courseCode.
        //Used when a delete class was used.
        connection = DBConnection.getConnection();
        try
        {
            getScheduleList = connection.prepareStatement("DELETE from app.schedule where semester = ? and courseCode = ?");
            getScheduleList.setString(1, semester);
            getScheduleList.setString(2, courseCode);
            getScheduleList.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
    }
    
    public static void updateScheduleEntry(ScheduleEntry entry){
        //Used to update student status from W to S.
        // Once a student is deleted or removed from a class.
        
        //entry.setStatus("S");
        connection = DBConnection.getConnection();
        try
        {
            getScheduleList = connection.prepareStatement("UPDATE app.schedule SET status = 'S' WHERE  studentid = ? and semester = ? and coursecode = ?");
            getScheduleList.setString(1, entry.getStudentID());
            getScheduleList.setString(2, entry.getSemester());
            getScheduleList.setString(3, entry.getCourseCode());
            getScheduleList.executeUpdate();
            
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
    }
    
}
