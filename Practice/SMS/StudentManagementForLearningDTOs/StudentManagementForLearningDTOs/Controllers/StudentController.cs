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

        [HttpGet]
        public IActionResult AddStudent()
        {
            return View();
        }

        [HttpPost]
        public IActionResult AddStudent(CreateStudentDto dto)
        {
            StudentModel student = new StudentModel();

            student.Id = students.Count + 1;
            student.Name = dto.Name;
            student.Age = dto.Age;
            student.Email = dto.Email;
            student.Department = dto.Department;
            student.Semester = dto.Semester;

            students.Add(student);

            return RedirectToAction("Index");
        }

        public IActionResult ViewAllStudents()
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

        public IActionResult ViewStudentDetails()
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
