using Microsoft.AspNetCore.Mvc;
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

    }
}
