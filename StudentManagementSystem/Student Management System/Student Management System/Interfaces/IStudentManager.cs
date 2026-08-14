using Student_Management_System.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Student_Management_System.Interfaces
{
    internal interface IStudentManager
    {
        public void addStudent(Student student);
        public List<Student> showAllStudents();
        public Student? searchStudent(string studentId);
        public bool updateStudent(string studentId, Student student);
        public bool deleteStudent(string studentId);
        public List<Student>? showTopStudents(int count);
        public List<Student>? showEligibleStudents();
        public bool saveStudents();
        public bool loadStudents();
    }
}
