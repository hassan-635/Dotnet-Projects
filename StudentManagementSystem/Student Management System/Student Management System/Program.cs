using System;
using Student_Management_System.Interfaces;
using Student_Management_System.Services;

namespace Student_Management_System
{
    internal class Program
    {

        public static int showOptions()
        {
            Console.WriteLine("Enter : ");
            Console.WriteLine("1 to Add Student");
            Console.WriteLine("2 to Show All Students");
            Console.WriteLine("3 to Search Student By id");
            Console.WriteLine("4 to update Student By id");
            Console.WriteLine("5 to delete Student by id");
            Console.WriteLine("6 to show Top Students");
            Console.WriteLine("7 to show Eligible Students");

            int opt = Console.Read();
            return opt;
        }
        static void Main(string[] args)
        {
            IStudentManager sm = new StudentManager();

            int option = showOptions();
        }
    }
}