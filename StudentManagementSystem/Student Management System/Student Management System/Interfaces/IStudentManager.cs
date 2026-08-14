using System;
using System.Collections.Generic;
using System.Text;

namespace Student_Management_System.Interfaces
{
    internal interface IStudentManager
    {
        public void addStudent();
        public void showAllStudents();
        public void searchStudent(int studentId);
        public void updateStudent(int studentId);
        public void deleteStudent(int studentId);
        public void showTopStudents(int positions);
        public void showEligibleStudents();
        public void saveStudents();
        public void loadStudents();
    }
}
