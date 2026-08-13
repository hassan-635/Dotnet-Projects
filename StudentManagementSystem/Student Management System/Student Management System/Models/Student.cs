using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;
using Microsoft.EntityFrameworkCore;

namespace Student_Management_System.Models
{
    [Index(nameof(StudentId), IsUnique = true)]
    internal class Student : Person
    {
        [Required(ErrorMessage ="Please Enter Student ID")]
        public string StudentId { get; set; }

        [Required(AllowEmptyStrings = false, ErrorMessage = "Please Enter Course")]
        public string Course { get; set; }

        [Range(1, 8, ErrorMessage = "Semester must be between 1 and 8")]
        public int Semester { get; set; }

        [Range(0, 100, ErrorMessage = "Please Enter Marks of Students")]
        public int marks { get; set; }

        [Range(0, 100, ErrorMessage = "Please Enter Attendance Percentage of Students")]
        public double attendancePercentage { get; set; }
    }
}
