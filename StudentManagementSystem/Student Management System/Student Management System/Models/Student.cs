using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;
using Microsoft.EntityFrameworkCore;

namespace Student_Management_System.Models
{
    [Index(nameof(studentId), IsUnique = true)]
    internal class Student : Person
    {
        [Required(ErrorMessage ="Please Enter Student ID")]
        public string studentId { get; set; }

        [Required(AllowEmptyStrings = false, ErrorMessage = "Please Enter Course")]
        public string course { get; set; }

        [Range(1, 8, ErrorMessage = "Semester must be between 1 and 8")]
        public int semester { get; set; }

        [Range(0, 100, ErrorMessage = "Please Enter Marks of Students")]
        public int marks { get; set; }

        [Range(0, 100, ErrorMessage = "Please Enter Attendance Percentage of Students")]
        public double attendancePercentage { get; set; }

        public Student(string name, int age, string email, string phone, string studentId, string course, int semester, int marks, double attendacePercentage)
        {
            this.name = name;
            this.age = age;
            this.email = email;
            this.phone = phone;
            this.studentId = studentId;
            this.course = course;
            this.semester = semester;
            this.marks = marks;
            this.attendancePercentage = attendacePercentage;
        }

        public string GetGrade()
        {
            string grade;
            if(marks >= 80)
            {
                grade = "A";
            }
            else if (marks >= 70 && marks <= 79)
            {
                grade = "B";
            }
            else if (marks >= 60 && marks <= 69)
            {
                grade = "C";
            }
            else if(marks >= 50 && marks <=59)
            {
                grade = "D";
            }
            else
            {
                grade = "F";
            }
            return grade;
        }

        public bool isEligible()
        {
            if(marks>=50 && attendancePercentage>=75)
            {
                return true;
            }
            else { return false; }
        }
    }
}
