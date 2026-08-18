using System.ComponentModel.DataAnnotations;
namespace Calculators.Models.ViewModels
{
    public class BasicCalculatorViewModel
    {
        [Required(ErrorMessage = "Number 1 is required")]
        public decimal Number1 { get; set; }
        [Required(ErrorMessage = "Number 2 is required")]
        public decimal Number2 { get; set; }
        [Required(ErrorMessage = "Please Select An operator")]
        public string Operation { get; set; }
        public decimal Result { get; set; }
    }
}
