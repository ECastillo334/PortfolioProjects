
import java.sql.Timestamp;





public class ScheduleEntry {
    private String status;
    private Timestamp timestamp;
    private String semester;
    private String courseCode;
    private String studentID;
    
    public ScheduleEntry(String status, Timestamp timestamp, String semester, String courseCode, String studentID) {
        this.status = status;
        this.timestamp = timestamp;
        this.semester = semester;
        this.courseCode = courseCode;
        this.studentID = studentID;
    }

    public String getStatus() {
        return status;
    }

    public Timestamp getTimestamp() {
        return timestamp;
    }

    public String getSemester() {
        return semester;
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getStudentID() {
        return studentID;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public void setTimestamp(Timestamp timestamp) {
        this.timestamp = timestamp;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public void setCourseCode(String courseCode) {
        this.courseCode = courseCode;
    }

    public void setStudentID(String studentID) {
        this.studentID = studentID;
    }
    
    
    
}
