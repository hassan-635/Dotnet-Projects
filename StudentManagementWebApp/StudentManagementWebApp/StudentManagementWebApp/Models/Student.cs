using System.ComponentModel.DataAnnotations;
using System;
using Microsoft.EntityFrameworkCore;

namespace StudentManagementWebApp.Models
{
    [Index(nameof(StudentId), nameof(Email), nameof(Phone), IsUnique = true)]
    public class Student
    {
        [Required(ErrorMessage = "Please Enter Student Id")]
        public string StudentId { get; set; }

        [Required(ErrorMessage = "Please Enter Name")]
        [StringLength(20, MinimumLength = 2, ErrorMessage = "Please Enter name of length 2 to 20")]
        public string Name { get; set; }

        [Required(ErrorMessage ="Please Enter Age")]
        public int Age { get; set; }

        [Required(ErrorMessage = "Please Enter Email")]
        [EmailAddress]
        public string Email { get; set; }

        [Required(ErrorMessage = "Please Enter Valid Phone Number")]
        [Phone]
        public string Phone { get; set; }

        [Required(ErrorMessage = "Please Enter Course")]
        [StringLength(10, MinimumLength = 2)]
        public string Course { get; set; }

        [Required(ErrorMessage = "Please Enter Semester")]
        [Range(1, 8, ErrorMessage = "Pleasse Enter Semester 1 to 8")]
        public int Semester { get; set; }

        [Required(ErrorMessage = "Please Enter Marks")]
        [Range(0, 100, ErrorMessage = "Please Enter Marks between 0 to 100")]
        public int Marks { get; set; }

        [Required(ErrorMessage = "Please Enter Student Attendance Percentage")]
        [Range(0, 100, ErrorMessage = "Please Enter Student percentage betwqeen 0 to 100")]
        public double AttendancePercentage { get; set; }
    }
}
