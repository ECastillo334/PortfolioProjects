


public class CourseEntry {
    
    private String courseID;
    private String description;

    public CourseEntry(String courseDescription, String ID) {
        courseID = ID;
        description = courseDescription;
    }
    
    public String getCourseDescription(){
        return this.description;
    }
    
    public String getCourseID(){
        return courseID;
    }
}
