using System;
using System.Collections.Generic;
using System.Linq;
using StudentManagementWebApp.Services.Interfaces;
using StudentManagementWebApp.Models;

namespace StudentManagementWebApp.Data
{
    public class InMemoryStudentRepository : IStudentRepository
    {
        private List<Student> students = new List<Student>
        {
            new Student
            {
                StudentId = "ST001",
                Name = "Ali Khan",
                Age = 20,
                Email = "ali@example.com",
                Phone = "03001234567",
                Course = "Computer Science",
                Semester = 4,
                Marks = 82,
                AttendancePercentage = 88
            },

            new Student
            {
                StudentId = "ST002",
                Name = "Ahmed Raza",
                Age = 21,
                Email = "ahmed@example.com",
                Phone = "03111234567",
                Course = "Software Engineering",
                Semester = 6,
                Marks = 74,
                AttendancePercentage = 79
            },

            new Student
            {
                StudentId = "ST003",
                Name = "Hamza Ali",
                Age = 19,
                Email = "hamza@example.com",
                Phone = "03221234567",
                Course = "Computer Science",
                Semester = 2,
                Marks = 91,
                AttendancePercentage = 94
            }
        };
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
