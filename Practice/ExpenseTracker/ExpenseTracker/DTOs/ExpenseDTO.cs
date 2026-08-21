using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

namespace ExpenseTracker.DTOs
{
    [Index(nameof(Id), IsUnique = true)]
    public class ExpenseDTO
    {
        [Required]
        public int Id { get; set; }
        [Required]
        [StringLength(30)]
        public string Title { get; set; }
        [Required]
        public int Amount { get; set; }
        [Required]
        public string Category { get; set; }
        [Required]
        public DateOnly Date { get; set; }
    }
}
