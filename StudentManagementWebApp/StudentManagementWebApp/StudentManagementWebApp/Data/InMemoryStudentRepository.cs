using System;
using System.Collections.Generic;
using System.Linq;
using StudentManagementWebApp.Services.Interfaces;
using StudentManagementWebApp.Models;

namespace StudentManagementWebApp.Data
{
    public class InMemoryStudentRepository : IStudentRepository
    {
        private List<Student> students= new List<Student>();
        public IEnumerable<Student> GetAll()
        {
            return students;
        }

        public Student? GetById(string StudentId)
        {
            Student student = students.FirstOrDefault(s => s.StudentId == StudentId);

            if(student == null)
            {
                return null;
            }
            return student;
        }

        public void Add(Student student)
        {
            students.Add(student);
        }

        public bool Update(Student student)
        {
            var ExistingStudent = students.FirstOrDefault(s => s.StudentId == student.StudentId);
            if(ExistingStudent == null)
            {
                return false;
            }
            ExistingStudent.Name = student.Name;
            ExistingStudent.Age = student.Age;
            ExistingStudent.Email = student.Email;
            ExistingStudent.Phone = student.Phone;
            ExistingStudent.Course = student.Course;
            ExistingStudent.Semester = student.Semester;
            ExistingStudent.Marks = student.Marks;
            ExistingStudent.AttendancePercentage = student.AttendancePercentage;

            return true;
        }

        public bool Delete(string StudentId)
        {
            var ExistingStudent = students.FirstOrDefault(s => s.StudentId == StudentId);
            if(ExistingStudent == null)
            {
                return false;
            }
            students.Remove(ExistingStudent);
            return true;
        }

    }
}
