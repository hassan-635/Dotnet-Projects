using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

namespace StudentManagementForLearningDTOs.DTOs
{
    [Index(nameof(id), IsUnique = true)]
    public class StudentDto
    {
        [Required]
        public int id { get; set; }
        [Required]
        public string Name { get; set; }
        public string Department { get; set; }
        [Required]
        [Range(1, 8)]
        public int Semester { get; set; }
    }
}
