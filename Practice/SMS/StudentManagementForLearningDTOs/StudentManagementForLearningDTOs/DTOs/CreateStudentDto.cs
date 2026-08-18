using System.ComponentModel.DataAnnotations;

namespace StudentManagementForLearningDTOs.DTOs
{
    public class CreateStudentDto
    {
        [Required]
        public string Name { get; set; }
        [Required]
        [EmailAddress]
        public string Email { get; set; }
        [Range(1, 30)]
        public int Age { get; set; }
        [Required]
        [StringLength(10)]
        public string Department { get; set; }
        [Required]
        [Range(1, 8)]
        public int Semester { get; set; }
    }
}
