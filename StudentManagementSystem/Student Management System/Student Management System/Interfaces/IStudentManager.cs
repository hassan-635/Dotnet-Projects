using Student_Management_System.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Student_Management_System.Interfaces
{
    internal interface IStudentManager
    {
        public void addStudent();
        public List<Student> showAllStudents();
        public Student? searchStudent(int studentId);
        public bool updateStudent(int studentId);
        public bool deleteStudent(int studentId);
        public List<Student> showTopStudents(int positions);
        public List<Student> showEligibleStudents();
        public bool saveStudents();
        public bool loadStudents();
    }
}
