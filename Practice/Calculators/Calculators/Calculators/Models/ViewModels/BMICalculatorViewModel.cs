using System.ComponentModel.DataAnnotations;

namespace Calculators.Models.ViewModels
{
    public class BMICalculatorViewModel
    {
        [Required]
        public decimal Weight { get; set; }
        [Required]
        public decimal Height { get; set; }
        public string Result { get; set; }
    }
}
