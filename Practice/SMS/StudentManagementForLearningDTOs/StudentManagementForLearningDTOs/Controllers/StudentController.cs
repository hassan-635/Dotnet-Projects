using Microsoft.AspNetCore.Mvc;

namespace StudentManagementForLearningDTOs.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {
            return View();
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
