using Student_Management_System.Interfaces;
using Student_Management_System.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Student_Management_System.Services
{
    internal class StudentManager : IStudentManager
    {
        private List<Student> students = new List<Student>();

        public void addStudent(Student student)
        {
                if(students.Any(existingStudent => existingStudent.studentId == student.studentId))
                {
                    Console.WriteLine("Student Already Exist.. Please Enter Unique Student Id...");
                }
                else
                {
                    students.Add(student);
                }
            
                Console.WriteLine("Student Added Successfully....");
        }

        public List<Student> showAllStudents()
        {
            return students;
        }

        public Student? searchStudent(string studentId)
        {
            if (students.Any(existingStudent => existingStudent.studentId == studentId))
            {
                return students.FirstOrDefault(s => s.studentId == studentId);
            }
            else return null;
        }

        public bool updateStudent(string studentId, Student student)
        {
            var existingStudent = students.FirstOrDefault(s => s.studentId == studentId);

            if(studentId == null)
            {
                return false;
            }
            else
            {
                existingStudent.name = student.name;
                existingStudent.age = student.age;
                existingStudent.email = student.email;
                existingStudent.course = student.course;
                existingStudent.semester = student.semester;
                existingStudent.marks = student.marks;
                existingStudent.attendancePercentage = student.attendancePercentage;

                return true;
            }
        }

        public bool deleteStudent(string studentId)
        {
            var existingStudent = students.FirstOrDefault(s => s.studentId == studentId);
            
            if (existingStudent == null)
            {
                return false;
            }

            else
            {
                students.Remove(existingStudent);
                return true;
            }
        }
    }
}
