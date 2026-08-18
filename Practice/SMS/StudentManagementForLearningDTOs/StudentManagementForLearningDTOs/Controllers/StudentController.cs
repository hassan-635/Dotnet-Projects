using Microsoft.AspNetCore.Mvc;
using StudentManagementForLearningDTOs.Models;
using StudentManagementForLearningDTOs.DTOs;

namespace StudentManagementForLearningDTOs.Controllers
{
    public class StudentController : Controller
    {
        private static List<StudentModel> students = new List<StudentModel>();
        public IActionResult Index()
        {
            List<StudentDto> studentDtos = students.Select(student => new StudentDto
            {
                Id = student.Id,
                Name = student.Name,
                Department = student.Department,
                Semester = student.Semester
            }).ToList();

            return View(studentDtos);
        }

        public IActionResult ViewAllStudents()
        {
            return View();
        }

        public IActionResult ViewStudentDetails()
        {
            return View();
        }

        public IActionResult AddStudent()
        {
            return View();
        }

        public IActionResult EditStudent()
        {
            return View();
        }

        public IActionResult DeleteStudent()
        {
            return View();
        }
    }
}
