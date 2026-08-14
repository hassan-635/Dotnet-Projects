using System;
using Student_Management_System.Interfaces;
using Student_Management_System.Services;
using Student_Management_System.Models;
using Microsoft.Extensions.Options;


namespace Student_Management_System
{
    internal class Program
    {
        private static IStudentManager sm = new StudentManager();

        public static int showOptions()
        {
            sm.loadStudents();
            Console.WriteLine("Enter : ");
            Console.WriteLine("1 to Add Student");
            Console.WriteLine("2 to Show All Students");
            Console.WriteLine("3 to Search Student By id");
            Console.WriteLine("4 to update Student By id");
            Console.WriteLine("5 to delete Student by id");
            Console.WriteLine("6 to show Top Students");
            Console.WriteLine("7 to show Eligible Students");

            int opt = int.Parse(Console.ReadLine() ?? "0");
            return opt;
        }

        public static void performActions(int option)
        {
            if(option == 1)
            {
                Console.WriteLine("Enter Student Id : ");
                string id = Console.ReadLine();
                Console.WriteLine("Enter Student Name : ");
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
                sm.saveStudents();
            }
            else if(option == 2)
            {
                var students = sm.showAllStudents();

                if (students == null || students.Count == 0)
                {
                    Console.WriteLine("No students found.");
                }
                else
                {
                    Console.WriteLine("\n===== ALL STUDENTS =====");
                    foreach (var s in students)
                    {
                        Console.WriteLine($"ID: {s.studentId} | Name: {s.name} | Age: {s.age} | Email: {s.email} | Phone: {s.phone} | Course: {s.course} | Semester: {s.semester} | Marks: {s.marks} | Attendance: {s.attendancePercentage}%");
                    }
                    Console.WriteLine("========================");
                }
            }
            else if(option == 3)
            {
                Console.WriteLine("Enter student id to search : ");
                string id = Console.ReadLine();
                Student  student = sm.searchStudent(id);
                if(student == null)
                {
                    Console.WriteLine("Student Not Found!!!");
                }
                else
                {
                    Console.WriteLine("\n========== STUDENT FOUND ==========");
                    Console.WriteLine($"Student ID: {student.studentId}");
                    Console.WriteLine($"Name: {student.name}");
                    Console.WriteLine($"Age: {student.age}");
                    Console.WriteLine($"Email: {student.email}");
                    Console.WriteLine($"Phone: {student.phone}");
                    Console.WriteLine($"Course: {student.course}");
                    Console.WriteLine($"Semester: {student.semester}");
                    Console.WriteLine($"Marks: {student.marks}");   
                    Console.WriteLine($"Attendance: {student.attendancePercentage}%");
                    Console.WriteLine("===================================");
                }
            }
            else if (option == 4)
            {
                Console.Write("Please enter Student ID to update: ");
                string id = Console.ReadLine();

                Student? existingStudent = sm.searchStudent(id);

                if (existingStudent == null)
                {
                    Console.WriteLine("Student Not Found!!!");
                    return;
                }

                Console.Write("Enter Student Name: ");
                string name = Console.ReadLine();

                int age;

                while (true)
                {
                    Console.Write("Enter Student Age: ");

                    if (int.TryParse(Console.ReadLine(), out age) && age >= 1 && age <= 60)
                    {
                        break;
                    }

                    Console.WriteLine("Invalid Age! Enter a value between 1 and 60.");
                }

                Console.Write("Enter Email: ");
                string email = Console.ReadLine();

                Console.Write("Enter Phone Number: ");
                string phone = Console.ReadLine();

                Console.Write("Enter Course: ");
                string course = Console.ReadLine();

                int semester;

                while (true)
                {
                    Console.Write("Enter Semester: ");

                    if (int.TryParse(Console.ReadLine(), out semester) &&
                        semester >= 1 && semester <= 8)
                    {
                        break;
                    }

                    Console.WriteLine("Invalid Semester! Enter a value between 1 and 8.");
                }

                int marks;

                while (true)
                {
                    Console.Write("Enter Marks: ");

                    if (int.TryParse(Console.ReadLine(), out marks) &&
                        marks >= 0 && marks <= 100)
                    {
                        break;
                    }

                    Console.WriteLine("Invalid Marks! Enter a value between 0 and 100.");
                }

                double attendancePercentage;

                while (true)
                {
                    Console.Write("Enter Attendance Percentage: ");

                    if (double.TryParse(
                            Console.ReadLine(),
                            out attendancePercentage) &&
                        attendancePercentage >= 0 &&
                        attendancePercentage <= 100)
                    {
                        break;
                    }

                    Console.WriteLine("Invalid Attendance! Enter a value between 0 and 100.");
                }

                Student student = new Student(
                    id,
                    name,
                    age,
                    email,
                    phone,
                    course,
                    semester,
                    marks,
                    attendancePercentage
                );

                bool result = sm.updateStudent(id, student);

                if (result)
                {
                    Console.WriteLine("Student Updated Successfully.");
                    sm.saveStudents();
                }
                else
                {
                    Console.WriteLine("Student Update Failed.");
                }
            }
            else if(option == 5)
            {
                Console.Write("Please enter Student ID to update: ");
                string id = Console.ReadLine();

                bool result = sm.deleteStudent(id);

                if (result)
                {
                    Console.WriteLine("Student Deleted!!!");
                    sm.saveStudents();
                }
                else
                {
                    Console.WriteLine("Student Not Found!!!");
                }

            }
            else if (option == 6)
            {
                int count;

                while (true)
                {
                    Console.Write("Please Enter total positions: ");

                    if (int.TryParse(Console.ReadLine(), out count) && count > 0)
                    {
                        break;
                    }

                    Console.WriteLine("Invalid input! Please enter a positive number.");
                }

                List<Student> topStudents = sm.showTopStudents(count);

                if (topStudents.Count == 0)
                {
                    Console.WriteLine("No students found.");
                }
                else
                {
                    Console.WriteLine("\n========== TOP STUDENTS ==========");

                    foreach (Student student in topStudents)
                    {
                        Console.WriteLine(
                            $"ID: {student.studentId} | " +
                            $"Name: {student.name} | " +
                            $"Marks: {student.marks}"
                        );
                    }
                }
            }
            else if (option == 7)
            {
                List<Student>? eligibleStudents = sm.showEligibleStudents();

                if (eligibleStudents == null || eligibleStudents.Count == 0)
                {
                    Console.WriteLine("No eligible students found.");
                }
                else
                {
                    Console.WriteLine("\n========== ELIGIBLE STUDENTS ==========");

                    foreach (Student student in eligibleStudents)
                    {
                        Console.WriteLine(
                            $"ID: {student.studentId} | " +
                            $"Name: {student.name} | " +
                            $"Marks: {student.marks} | " +
                            $"Attendance: {student.attendancePercentage}%"
                        );
                    }
                }
            }

        }
        static void Main(string[] args)
        {
            int option = showOptions();

            performActions(option);
        }
    }
}