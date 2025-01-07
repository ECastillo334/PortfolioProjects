import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;





public class CourseQueries {
    
    
    private static Connection connection;
    private static ArrayList<String> faculty = new ArrayList<String>();
    private static PreparedStatement addSemester;
    private static PreparedStatement getSemesterList;
    private static ResultSet resultSet;
    
    
    public static void addCourse(CourseEntry course){
        connection = DBConnection.getConnection();
        try
        {
            addSemester = connection.prepareStatement("insert into app.course (courseid, description) values (?, ?)");
            addSemester.setString(1, course.getCourseID());
            addSemester.setString(2, course.getCourseDescription());
            addSemester.executeUpdate();
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
    }
    
    public static ArrayList<String> getAllCourseCodes(){
        connection = DBConnection.getConnection();
        ArrayList<String> courseIDs = new ArrayList<String>();
        try
        {
            getSemesterList = connection.prepareStatement("select courseid from app.course order by courseid");
            resultSet = getSemesterList.executeQuery();
            
            while(resultSet.next())
            {
                courseIDs.add(resultSet.getString(1));
            }
        }
        catch(SQLException sqlException)
        {
            sqlException.printStackTrace();
        }
        
        return courseIDs;
        
    }
}
