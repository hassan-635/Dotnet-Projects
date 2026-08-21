using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace ExpenseTracker.Models
{
    [Index(nameof(Id), IsUnique = true)]
    public class Expense
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
