using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;

namespace Student_Management_System.Models
{
    internal class Person
    {
        [Required(AllowEmptyStrings = false, ErrorMessage = "Please Enter Name")]
        public string name { get; set; }

        public int age { get; set; }    
        public string email { get; set; }
        public string phone { get; set; }
    }
}
