using Microsoft.AspNetCore.Mvc;
using StudentManagementForLearningDTOs.Models;
using StudentManagementForLearningDTOs.DTOs;
using System.Collections.Immutable;

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

        [HttpGet]
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

        [HttpGet]
        public IActionResult ViewStudentDetails()
        {
            return View();
        }

        [HttpPost]
        public IActionResult ViewStudentDetails(int id)
        {
            var sm = students.FirstOrDefault(student => student.Id == id);

            if(sm == null)
            {
                return NotFound();
            }

            return View(sm);
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
