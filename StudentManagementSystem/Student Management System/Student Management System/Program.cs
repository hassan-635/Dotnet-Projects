using System;
using Student_Management_System.Interfaces;
using Student_Management_System.Services;
using Student_Management_System.Models;


namespace Student_Management_System
{
    internal class Program
    {
        private static IStudentManager sm = new StudentManager();

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

            bool isvalid = int.TryParse(Console.ReadLine(), out int opt);
            return opt;
        }

        public static void performActions(int option)
        {
            if(option == 1)
            {
                Console.WriteLine("Enter Student Id : ");
                string id = Console.ReadLine();
                Console.WriteLine("Enter Student Namer : ");
                string name = Console.ReadLine();
                Console.WriteLine("Enter Student Age : ");
                bool isvalid = int.TryParse(Console.ReadLine(), out int age);
                Console.WriteLine("Enter Email : ");
                string email = Console.ReadLine();
                Console.WriteLine("Enter Phone number : ");
                string phone = Console.ReadLine();
                Console.WriteLine("Enter Course : ");
                string course = Console.ReadLine();
                Console.WriteLine("Enter Semester : ");
                isvalid = int.TryParse(Console.ReadLine(), out int semester);
                Console.WriteLine("Enter Marks : ");
                isvalid = int.TryParse(Console.ReadLine(), out int marks);
                Console.WriteLine("Enter Attendance Percentage : ");
                isvalid = double.TryParse(Console.ReadLine(), out double attendancePercentage);
                Student student = new Student(id, name, age, email, phone, course, semester, marks, attendancePercentage);
                sm.addStudent(student);
            }
        }
        static void Main(string[] args)
        {
            int option = showOptions();

            performActions(option);
        }
    }
}