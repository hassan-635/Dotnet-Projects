using Microsoft.AspNetCore.Mvc;

namespace ExpenseTracker.Controllers
{
    public class ExpenseController1 : Controller
    {
        public IActionResult Dashboard()
        {
            return View();
        }
    }
}
