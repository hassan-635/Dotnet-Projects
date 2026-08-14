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
    }
}
