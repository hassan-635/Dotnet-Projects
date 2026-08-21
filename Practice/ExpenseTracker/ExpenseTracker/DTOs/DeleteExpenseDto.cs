using System.ComponentModel.DataAnnotations;

namespace ExpenseTracker.DTOs
{
    public class DeleteExpenseDto
    {
        [Required]
        public int Id { get; set; }
    }
}
