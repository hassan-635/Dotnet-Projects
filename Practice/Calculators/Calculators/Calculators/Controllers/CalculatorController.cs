using Microsoft.AspNetCore.Mvc;

namespace Calculators.Controllers
{
    public class CalculatorController : Controller
    {
        public IActionResult Basic()
        {
            return View();
        }

        public IActionResult BMI()
        {
            return View();
        }

        public IActionResult Loan()
        {
            return View();
        }
    }
}
