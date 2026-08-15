using StudentManagementWebApp.Models;

namespace StudentManagementWebApp.Services.Interfaces
{
    public interface IStudentRepository
    {

        public IEnumerable<Student> GetAll();
        public Student? GetById(string StudentId);
        public void Add(Student student);
        public bool Update(Student student);
        public bool Delete(string StudentId);
    }
}
