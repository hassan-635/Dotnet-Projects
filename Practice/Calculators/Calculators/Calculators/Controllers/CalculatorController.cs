using Calculators.Models.ViewModels;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics.Eventing.Reader;

namespace Calculators.Controllers
{
    public class CalculatorController : Controller
    {
        public IActionResult Basic()
        {
            BasicCalculatorViewModel model = new BasicCalculatorViewModel();
            return View(model);
        }

        public IActionResult BMI()
        {
            BMICalculatorViewModel model = new BMICalculatorViewModel();
            return View(model);
        }

        public IActionResult Loan()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Calculate(BasicCalculatorViewModel model)
        {
            if(!ModelState.IsValid)
            {
                return View("Basic", model);
            }

            if (model.Operation == "+")
                model.Result = model.Number1 + model.Number2;
            else if (model.Operation == "-")
                model.Result = model.Number1 - model.Number2;
            else if(model.Operation == "*")
                model.Result = model.Number1 * model.Number2;
            else if(model.Operation == "/")
                model.Result =model.Number1 / model.Number2;

            return View("Basic", model);
        }

        [HttpPost]
        public IActionResult CalculateBMI(BMICalculatorViewModel model)
        {
            decimal heightInMeter = model.Height / 100;

            if (heightInMeter == 0)
            {
                model.Result = "Invalid height";
                return View("BMI", model);
            }

            decimal BMI = model.Weight / (heightInMeter * heightInMeter);

            if (BMI < 18.5M)
                model.Result = "Underweight";
            else if (BMI > 18.5M && BMI < 24.9M)
                model.Result = "Normal";
            else if (BMI >= 25 && BMI <= 29.9M)
                model.Result = "Overweight";
            else if (BMI >= 30)
                model.Result = "Obese";

            return View("BMI", model);
        }

        [HttpPost]
        public IActionResult CalculateLoan(LoanCalculatorViewModel model)
        {
            double baseRate = (double)(1m + model.InterestRate);
            double powDouble = Math.Pow(baseRate, (double)model.TotalMonthlyPayments);
            decimal pow = (decimal)powDouble;

            decimal numerator = model.LoanAmount * pow;
            decimal denominator = pow - 1m;
            if (denominator == 0m)
            {
                model.EMI = 0m;
            }
            else
            {
            model.EMI = numerator / denominator;
            }

            return View("Loan", model);
        }
    }
}
