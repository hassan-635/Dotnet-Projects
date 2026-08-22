using System.ComponentModel.DataAnnotations;

namespace MyNotes.Models
{
    public class Note
    {
        [Required]
        public int Id { get; set; }
        [Required]
        [StringLength(18)]
        public string Title { get; set; }
        [Required]
        [StringLength(100)]
        public string Description { get; set; }
    }
}
