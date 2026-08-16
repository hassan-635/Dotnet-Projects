using Microsoft.AspNetCore.Mvc;
using StudentManagementWebApp.Models;
using StudentManagementWebApp.Models.ViewModels;
using StudentManagementWebApp.Services.Interfaces;

namespace StudentManagementWebApp.Controllers
{
    public class StudentController : Controller
    {
        private readonly IStudentService _studentService;

        public StudentController(IStudentService studentService)
        {
            _studentService = studentService;
        }
        public IActionResult Index()
        {
            var students = _studentService.GetAllStudents();
            return View(students);
        }

        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(StudentFormViewModel model)
        {
            if(!ModelState.IsValid)
            {
                return View(model);
            }

            var student = new Student
            {
                StudentId = model.StudentId,
                Name = model.Name,
                Age = model.Age,
                Email = model.Email,
                Phone = model.Phone,
                Course = model.Course,
                Semester = model.Semester,
                Marks = model.Marks,
                AttendancePercentage = model.AttendancePercentage
            };

            var result = _studentService.CreateStudent(student);

            if(!result)
            {
                ModelState.AddModelError(
                    "StudentId",
                    "Student already exists");

                return View(model);
            }
            return RedirectToAction(nameof(Index));
        }

    }
}
