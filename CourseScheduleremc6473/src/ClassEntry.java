
//import java.sql;


public class ClassEntry {
    
    private int seats;
    private String courseCode;
    private String semester;

    public ClassEntry(int seats, String code, String semester) {
        this.seats = seats;
        this.courseCode = code;
        this.semester = semester;
        
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getSemester() {
        return semester;
    }
    
    public int getSeats(){
        return seats;
    }
    
}
