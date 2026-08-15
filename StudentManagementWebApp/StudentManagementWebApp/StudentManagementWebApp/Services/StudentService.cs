using StudentManagementWebApp.Models;
using StudentManagementWebApp.Services.Interfaces;

namespace StudentManagementWebApp.Services
{
    public class StudentService : IStudentService
    {
        private readonly IStudentRepository repo;
        public StudentService(IStudentRepository repository)
        {
            repo = repository;
        }
        public IEnumerable<Student> GetAllStudents()
        {
            var students = repo.GetAll();
            return students;
        }
        public Student? GetStudentById(String StudentId)
        {
            var student = repo.GetById(StudentId);
            return student;
        }
        public bool CreateStudent(Student student)
        {
            List<Student> students = repo.GetAll().ToList();
            var existingStudent = students.FirstOrDefault(s => s.StudentId == student.StudentId);
            if(existingStudent != null)
            {
                return false;
            }
            repo.Add(student);
            return true;
        }
        public bool UpdateStudent(Student student)
        {
            return repo.Update(student);
        }
        public bool DeleteStudent(string StudentId)
        {
            return repo.Delete(StudentId);
        }
    }
}