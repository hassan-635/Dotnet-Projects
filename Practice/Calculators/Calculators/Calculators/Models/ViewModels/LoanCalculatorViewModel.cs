namespace Calculators.Models.ViewModels
{
    public class LoanCalculatorViewModel
    {

        public decimal LoanAmount { get; set; }
        public decimal InterestRate { get; set; }
        public int TotalMonthlyPayments { get; set; }
        public decimal EMI { get; set; }
    }
}
