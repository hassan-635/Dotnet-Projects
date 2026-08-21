using System.ComponentModel.DataAnnotations;

namespace BookManagement.DTOs
{
    public class BookDto
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
