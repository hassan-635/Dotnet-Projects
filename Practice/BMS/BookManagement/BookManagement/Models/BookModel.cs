using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

namespace BookManagement.Models
{
    [Index(nameof(Id), IsUnique = true)]
    public class BookModel
    {
        [Required]
        public int Id { get; set; }
        [Required]
        [StringLength(50)]
        public string Title { get; set; }
        [Required]
        [StringLength(30)]
        public string Author { get; set; }
        [Required]
        public decimal Price { get; set; }
    }
}
