using StudentManagementWebApp.Models;

namespace StudentManagementWebApp.Services.Interfaces
{
    public interface IStudentService
    {
        public IEnumerable<Student> GetAllStudents();
        public Student? GetStudentById(string StudentId);
        public bool CreateStudent(Student student);
        public bool UpdateStudent(Student student);
        public bool DeleteStudent(string StudentId);
    }
}
