# generate_roadmap.py
import json
import os

print("Generating ASP.NET Core & AI/ML Backend Roadmap...")

# Let's define the days data
days_data = [
    # --- WEEK 1 ---
    {
        "day_num": 1,
        "title": "C# Syntax Differences from C++ & Memory Model",
        "objectives": [
            "Understand C# compilation flow (.NET CLI -> CIL -> JIT compilation).",
            "Contrast C# reference-based memory model and Garbage Collection against C++ RAII and pointers.",
            "Understand namespace usages, Assembly metadata, and C# basic data types."
        ],
        "theory": [
            "Compilation: Unlike C++ which compiles directly to native assembly, C# compiles to Common Intermediate Language (CIL), packed inside a .dll or .exe. At runtime, the Just-In-Time (JIT) compiler compiles it to native machine instructions.",
            "Memory Management: C# handles heap memory automatically via a generational Garbage Collector (GC). C++ uses RAII, delete/free, or smart pointers. In C#, objects are reference types by default (created with new, managed on heap) while structs are value types (stack-allocated).",
            "Syntax Overrides: Main method belongs to a class (though modern C# supports top-level statements). No separate header files (.h) or forward declarations needed; everything is written inside .cs files."
        ],
        "coding_exercise": {
            "title": "C++ Pointers vs C# References Console App",
            "instructions": "Create a C# program simulating dynamic allocation and object reference swapping. Observe that objects are passed by reference value by default.",
            "stub": """using System;

class Person {
    public string Name { get; set; }
}

class Program {
    static void Main() {
        Person p1 = new Person { Name = "Alice" };
        Person p2 = new Person { Name = "Bob" };
        
        Console.WriteLine($"Before Swap: p1={p1.Name}, p2={p2.Name}");
        Swap(ref p1, ref p2); // ref keyword functions like C++ pointers or reference params
        Console.WriteLine($"After Swap: p1={p1.Name}, p2={p2.Name}");
    }
    
    static void Swap(ref Person a, ref Person b) {
        Person temp = a;
        a = b;
        b = temp;
    }
}"""
        },
        "mini_challenge": "Write a method that takes a value type (struct Point) and a reference type (class Box) and demonstrates which one changes outside the function without using the 'ref' keyword.",
        "common_mistakes": [
            "Attempting to manually release object references (C# does not have a delete operator; set references to null or use 'using' statements for native resources).",
            "Confusing class (reference type) and struct (value type) behaviors."
        ],
        "interview_questions": [
            {
                "q": "What is the difference between value types and reference types in C#?",
                "a": "Value types (structs, primitives) are stored on the stack and hold data directly. Reference types (classes, strings) are stored on the heap, and their memory reference address is stored on the stack."
            },
            {
                "q": "Explain how the Garbage Collector (GC) works in .NET.",
                "a": "The .NET GC manages allocation/release of heap memory. It uses three generations (Gen 0, Gen 1, Gen 2) to optimize collections, promoting long-lived objects to higher generations to reduce sweep frequency."
            }
        ],
        "homework": "Create a console application that defines a struct Point (x, y) and a class Rectangle (width, height, top_left Point). Modify their properties inside a modification function and output state to verify structural mutations.",
        "revision_checklist": [
            "I understand the difference between CIL and C++ machine code compilation.",
            "I know when to use class vs struct.",
            "I understand the 'ref' keyword in parameters."
        ]
    },
    {
        "day_num": 2,
        "title": "C# Collections & Generics (List, Dictionary, Queue, Stack)",
        "objectives": [
            "Compare standard C# collection types with C++ STL vector and maps.",
            "Implement generic constraints in C# interfaces.",
            "Understand when to choose List vs Dictionary vs Queue/Stack."
        ],
        "theory": [
            "C# generic collections are located in System.Collections.Generic.",
            "List<T> acts as a dynamic array similar to C++ std::vector<T>.",
            "Dictionary<TKey, TValue> acts as a hash map, similar to std::unordered_map<TKey, TValue> in C++.",
            "Generics: Type safety without performance costs (no boxing/unboxing). In C#, you can add dynamic constraints to generics using the 'where' keyword (e.g. where T : class, new())."
        ],
        "coding_exercise": {
            "title": "Build a Generic Cache Store",
            "instructions": "Implement a simple generic CacheStore class that uses a Dictionary to cache elements. Apply type constraints.",
            "stub": """using System;
using System.Collections.Generic;

class CacheStore<TKey, TValue> where TValue : class {
    private readonly Dictionary<TKey, TValue> _store = new();
    
    public void Add(TKey key, TValue val) {
        _store[key] = val;
    }
    
    public TValue Get(TKey key) {
        return _store.TryGetValue(key, out var val) ? val : null;
    }
}"""
        },
        "mini_challenge": "Create a program using Queue<string> to simulate processing AI job requests in order, and Stack<string> to track undo operations of a text editor.",
        "common_mistakes": [
            "Using non-generic collections like ArrayList, which causes boxing/unboxing overhead and loses type-safety.",
            "Over-allocating memory by not capacity-initializing lists or dictionaries when dimensions are known."
        ],
        "interview_questions": [
            {
                "q": "What is Boxing and Unboxing in C#?",
                "a": "Boxing is converting a value type to a reference type (object). Unboxing is casting it back. Both processes degrade performance as they allocate objects on the heap."
            },
            {
                "q": "What is the difference between List<T> and Dictionary<K, V> in terms of search complexity?",
                "a": "List<T> has a linear O(N) search complexity (unless sorted and binary searched), while Dictionary<K,V> has near O(1) average lookup time due to hash-based indexing."
            }
        ],
        "homework": "Write a console app to index words from a paragraph and count their occurrences using a Dictionary<string, int>.",
        "revision_checklist": [
            "I can define a class with generic parameters.",
            "I know the performance impact of Boxing.",
            "I understand dictionary key collision mechanics."
        ]
    },
    {
        "day_num": 3,
        "title": "Exception Handling & File I/O",
        "objectives": [
            "Write robust Exception handling blocks with try-catch-finally.",
            "Implement C# 'using' statement and the IDisposable interface to release native resources.",
            "Read and write data to files using FileStream and StreamWriter."
        ],
        "theory": [
            "Exception Handling: Try-Catch-Finally. The 'finally' block executes regardless of exceptions, which is crucial for closing databases or connections.",
            "Resource Management: Unlike C++ destructors which execute instantly when an object goes out of scope (deterministic cleanup), C# relies on Garbage Collection (non-deterministic). To release files, DB connections, or sockets immediately, classes implement IDisposable. The C# 'using' statement handles disposal automatically.",
            "File Handling: System.IO classes. File, FileStream, StreamReader/Writer."
        ],
        "coding_exercise": {
            "title": "Auto-Disposing File Logger",
            "instructions": "Create a file writer using the disposable pattern with the 'using' syntax to log errors to a local text file.",
            "stub": """using System;
using System.IO;

class Program {
    static void Main() {
        string path = "error_log.txt";
        
        try {
            int result = Divide(10, 0);
        }
        catch (DivideByZeroException ex) {
            // Automatic resource release via 'using' block
            using (StreamWriter writer = new StreamWriter(path, true)) {
                writer.WriteLine($"[{DateTime.Now}] ERROR: {ex.Message}");
            }
            Console.WriteLine("Logged error successfully!");
        }
    }
    
    static int Divide(int a, int b) => a / b;
}"""
        },
        "mini_challenge": "Define a custom exception validation rule UserValidationException and write a program to validate age inputs, logging failures inside a custom log file.",
        "common_mistakes": [
            "Catching generic Exceptions (e.g., 'catch (Exception)') instead of specific subclasses (e.g., ArgumentNullException).",
            "Forgetting to call Close() or Dispose() on files, causing locks."
        ],
        "interview_questions": [
            {
                "q": "What is the IDisposable interface and when should you implement it?",
                "a": "IDisposable is used to release unmanaged resources like file handles, database connections, and network sockets. You implement it to allow deterministic cleanups instead of waiting for the GC."
            },
            {
                "q": "What is the difference between throw and throw ex in a catch block?",
                "a": "'throw' preserves the original stack trace of the exception. 'throw ex' resets the stack trace to the current method, losing debugging context."
            }
        ],
        "homework": "Write a script that reads a CSV file containing student information, parses it, and creates a report. Catch potential file-not-found or parse exceptions cleanly.",
        "revision_checklist": [
            "I know when to use the finally block.",
            "I understand the relationship between using statements and IDisposable.",
            "I can create a custom exception class."
        ]
    },
    {
        "day_num": 4,
        "title": "LINQ Basics (Language Integrated Query)",
        "objectives": [
            "Learn LINQ Query and Method syntax.",
            "Perform filtering, mapping, grouping, and aggregation on data collections.",
            "Understand deferred execution vs immediate execution."
        ],
        "theory": [
            "LINQ allows querying collections directly in C# code. Think of it as SQL for object arrays.",
            "Query Syntax: resembles SQL (`from x in list where x > 5 select x`).",
            "Method Syntax: Uses lambda methods (`list.Where(x => x > 5).Select(x => x)`). This is the preferred style in modern ASP.NET Core.",
            "Deferred Execution: Methods like `Where` and `Select` do not execute immediately. They build expression trees. Execution happens when you iterate over the result (e.g. using `foreach`) or force it with methods like `ToList()` or `ToArray()`."
        ],
        "coding_exercise": {
            "title": "Filtering AI Datasets with LINQ",
            "instructions": "Query a list of ML prediction outputs to filter items having validation scores above 85% and sort them descending.",
            "stub": """using System;
using System.Collections.Generic;
using System.Linq;

class Prediction {
    public string ModelName { get; set; }
    public double Confidence { get; set; }
}

class Program {
    static void Main() {
        List<Prediction> dataset = new() {
            new Prediction { ModelName = "ResNet", Confidence = 0.92 },
            new Prediction { ModelName = "YOLO", Confidence = 0.81 },
            new Prediction { ModelName = "BERT", Confidence = 0.95 }
        };
        
        // LINQ Method Syntax
        var highConfidence = dataset
            .Where(p => p.Confidence > 0.85)
            .OrderByDescending(p => p.Confidence)
            .ToList();
            
        foreach (var p in highConfidence) {
            Console.WriteLine($"{p.ModelName}: {p.Confidence:P}");
        }
    }
}"""
        },
        "mini_challenge": "Given a list of strings representing log entries, use LINQ to group logs by their severity tag (INFO, WARN, ERROR) and print counts.",
        "common_mistakes": [
            "Calling `.ToList()` repeatedly on intermediate query chains, causing multiple memory allocations and executing steps early.",
            "Writing nested loops instead of readable LINQ statements."
        ],
        "interview_questions": [
            {
                "q": "What is the difference between Deferred and Immediate execution in LINQ?",
                "a": "Deferred execution means the query evaluation is delayed until the data is actually iterated. Immediate execution occurs when methods like ToList(), FirstOrDefault(), or Count() are called."
            },
            {
                "q": "What is the difference between IEnumerable and IQueryable?",
                "a": "IEnumerable is used for in-memory collections and filters data using in-memory LINQ queries. IQueryable is used for out-of-memory resources (databases) and translates LINQ syntax to SQL before execution."
            }
        ],
        "homework": "Take a list of integers, filter out even numbers, square them, and get the average value of those squared values using LINQ.",
        "revision_checklist": [
            "I know the syntax differences between LINQ method and query syntax.",
            "I can explain Deferred Execution.",
            "I can construct dynamic filters using lambda expressions in LINQ."
        ]
    },
    {
        "day_num": 5,
        "title": "Async/Await & Multithreading basics",
        "objectives": [
            "Understand why async/await is essential for non-blocking I/O.",
            "Create and run asynchronous tasks with C# Tasks.",
            "Compare async models with C++ threads or raw threads."
        ],
        "theory": [
            "Web APIs handle high concurrency. Blocking a thread during database lookups or external API calls halts scalability.",
            "Async/Await: The thread is released back to the thread pool while waiting for I/O operations (like database calls). Once completed, a thread resumes execution.",
            "Task-based Asynchronous Pattern (TAP): C# uses `Task` and `Task<T>` as wrappers around asynchronous operations. It is not identical to spawning threads. A thread pool manages CPU threads, optimizing performance."
        ],
        "coding_exercise": {
            "title": "Simulate Fetching AI Model Output Asynchronously",
            "instructions": "Implement an async method simulating API delays using Task.Delay and wait for it using await.",
            "stub": """using System;
using System.Threading.Tasks;

class Program {
    static async Task Main() {
        Console.WriteLine("Sending inputs to PyTorch Model...");
        string prediction = await GetPredictionAsync();
        Console.WriteLine($"Model Response: {prediction}");
    }
    
    static async Task<string> GetPredictionAsync() {
        // Simulates network latency
        await Task.Delay(2000); 
        return "{'class': 'Cat', 'accuracy': 0.98}";
    }
}"""
        },
        "mini_challenge": "Create a console application that runs 3 long-running async tasks concurrently and prints results when all are completed using `Task.WhenAll`.",
        "common_mistakes": [
            "Using `.Result` or `.Wait()` to block async tasks in synchronous contexts, causing deadlocks (always use async/await top-to-bottom).",
            "Forgetting to mark async methods returning a value with `Task<T>`."
        ],
        "interview_questions": [
            {
                "q": "What happens when you await a task in C#?",
                "a": "The compiler transforms the method into a state machine. It releases the calling thread, schedules the remainder of the method as a callback, and returns execution control back to the caller."
            },
            {
                "q": "Why should you avoid 'async void' in ASP.NET Core applications?",
                "a": "'async void' should only be used for event handlers. Exceptions thrown in an async void method cannot be caught by try-catch blocks and will crash the application process."
            }
        ],
        "homework": "Write an application that reads 3 text files simultaneously using async techniques, then measures the time taken compared to reading them synchronously.",
        "revision_checklist": [
            "I know the difference between blocking and non-blocking code.",
            "I understand the function of Task.WhenAll.",
            "I can handle exceptions thrown inside asynchronous tasks."
        ]
    },
    {
        "day_num": 6,
        "title": "Delegates, Events & Lambdas",
        "objectives": [
            "Understand delegates as type-safe C++ function pointers.",
            "Use built-in delegates like Action, Func, and Predicate.",
            "Learn event publishing and subscription patterns."
        ],
        "theory": [
            "Delegates: Object-oriented, type-safe references to methods. In C++, you had function pointers. In C#, a delegate is a class wrapping a method pointer.",
            "Built-in Delegates: Func<T, TResult> (takes params, returns value), Action<T> (takes params, returns void), Predicate<T> (takes param, returns bool).",
            "Lambda Expressions: Concise way to write inline methods (e.g. `(a, b) => a + b`).",
            "Events: Uses publisher-subscriber model built directly on top of multicast delegates."
        ],
        "coding_exercise": {
            "title": "Delegate-Based Logging Pipeline",
            "instructions": "Create a pipeline system where users can register different target output formats (console, file) using delegates.",
            "stub": """using System;

delegate void LogMessage(string message);

class Program {
    static void Main() {
        LogMessage logPipeline = WriteToConsole;
        logPipeline += WriteToAlert; // Multicast
        
        logPipeline("System starting prediction pipeline...");
    }
    
    static void WriteToConsole(string msg) => Console.WriteLine($"Console: {msg}");
    static void WriteToAlert(string msg) => Console.WriteLine($"[ALERT]: {msg}");
}"""
        },
        "mini_challenge": "Rewrite the delegate exercise using `Action<string>` instead of defining a custom delegate, and pass one of the logic statements as an inline lambda.",
        "common_mistakes": [
            "Not checking if a delegate reference is null before calling it (use `myDelegate?.Invoke()`).",
            "Causing memory leaks by failing to unsubscribe (`-=`) event handlers from long-lived publishers."
        ],
        "interview_questions": [
            {
                "q": "What is a delegate and what are the Action, Func, and Predicate types?",
                "a": "A delegate is a reference type that defines a method signature. Action represents a method that returns void. Func represents a method that returns a value. Predicate returns a boolean."
            },
            {
                "q": "What is a multicast delegate?",
                "a": "A delegate that points to multiple methods sequentially. When invoked, all attached methods run in the order they were added (`+=` operator)."
            }
        ],
        "homework": "Implement a simulated payment processing engine with an event `OnPaymentCompleted`. Subscribe a invoice generator and SMS notifier to it.",
        "revision_checklist": [
            "I can define and invoke a delegate.",
            "I know how Func and Action differ.",
            "I understand standard lambda expression syntax."
        ]
    },
    {
        "day_num": 7,
        "title": "Week 1 Review & Mini Project",
        "objectives": [
            "Review syntax transformations and core coding concepts.",
            "Complete a weekly console application and verify implementation.",
            "Solve a complex debugging exercise."
        ],
        "theory": [
            "Revision Focus: Verify transition from manual allocations to safe heap references. Ensure knowledge of the IDisposable cleanup flow.",
            "Check that LINQ expressions utilize correct execution methods to avoid out-of-memory conditions.",
            "Confirm that async code does not use blocking constructs like `.Result`."
        ],
        "coding_exercise": {
            "title": "Mini Project: Contact Management Console App",
            "instructions": "Build a console app where users can create, delete, and list contacts using LINQ. Cache contacts in memory and save changes to text files asynchronously. Run validation checks.",
            "stub": """// Implement a contact class with ID, Name, Phone.
// Implement dynamic operations inside your repository.
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

class Contact {
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
}

class Program {
    static async Task Main() {
        // Build program loop allowing CRUD and async file persistence.
        Console.WriteLine("Contact System Active.");
    }
}"""
        },
        "mini_challenge": "Debugging Challenge: Fix a program that causes Task Deadlocks by converting it from block-state task invocation `.Wait()` to async execution flow `await`.",
        "common_mistakes": [
            "Ignoring exceptions raised inside async code.",
            "Writing nested async operations without utilizing Task context properly."
        ],
        "interview_questions": [
            {
                "q": "What is the role of assembly manifest in C#?",
                "a": "An assembly manifest contains information about identity, version, security details, and references to external libraries or files needed by the application."
            },
            {
                "q": "How does C# manage unmanaged resources without direct destructors?",
                "a": "C# manages unmanaged resources through implementation of the IDisposable interface inside classes and invoking the resource cleanup using 'using' statements."
            }
        ],
        "homework": "Optimize the Contact Manager app: Add dynamic generic validation routines to verify emails contain '@' characters, raising standard validation exceptions.",
        "revision_checklist": [
            "I have built the Contact Management Console App.",
            "I solved the task deadlock problem.",
            "I can explain OOP differences between C++ and C#."
        ]
    },

    # --- WEEK 2 ---
    {
        "day_num": 8,
        "title": "SQL Server Basics & Schema Design",
        "objectives": [
            "Understand relational database models and schema design principles.",
            "Learn Primary Keys, Foreign Keys, and Referential Integrity.",
            "Design database schemas adhering to 1NF, 2NF, and 3NF normalization."
        ],
        "theory": [
            "Relational Database: Stores data in tables with relationships mapped through keys. Primary Key (PK) uniquely identifies rows. Foreign Key (FK) maps links to PKs of other tables.",
            "Referential Integrity: Ensures child records cannot point to non-existent parent records (cascading actions like ON DELETE CASCADE control delete propagation).",
            "Normalization: Process of structural organization to prevent redundancy: 1NF (atomic values, no repeating columns), 2NF (meet 1NF, ensure full functional dependency on the PK), 3NF (meet 2NF, ensure transitive dependencies are eliminated)."
        ],
        "coding_exercise": {
            "title": "Create Student Database Schema",
            "instructions": "Write a SQL script creating tables with PK and FK constraints reflecting student course registrations.",
            "stub": """CREATE DATABASE StudentDB;
GO
USE StudentDB;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    EnrollmentDate DATETIME DEFAULT GETDATE()
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY IDENTITY(1,1),
    CourseTitle NVARCHAR(100) NOT NULL,
    Credits INT CHECK (Credits > 0 AND Credits <= 6)
);"""
        },
        "mini_challenge": "Create a mapping table StudentCourses implementing a composite primary key to map many-to-many relationships.",
        "common_mistakes": [
            "Neglecting indexes on foreign keys, which causes major performance issues during queries.",
            "Designing schemas with low normalization (under 3NF), creating duplicate rows and data inconsistencies."
        ],
        "interview_questions": [
            {
                "q": "What is the difference between Primary Key and Unique Key?",
                "a": "A Primary Key uniquely identifies a record and cannot accept NULL values. A Unique Key enforces unique attributes but allows a single NULL value."
            },
            {
                "q": "Explain 1NF, 2NF, and 3NF database normalization.",
                "a": "1NF requires atomic attributes and no duplicate fields. 2NF requires 1NF compliance and no partial dependencies. 3NF requires 2NF compliance and no transitive dependency on non-key columns."
            }
        ],
        "homework": "Design database schemas representing items, inventories, and warehouse suppliers mapping correct relational constraints.",
        "revision_checklist": [
            "I understand database normalization levels.",
            "I can define composite keys in SQL Server.",
            "I know the performance impact of referential integrity rules."
        ]
    },
    {
        "day_num": 9,
        "title": "SQL CRUD & Filtering",
        "objectives": [
            "Perform INSERT, UPDATE, DELETE, and SELECT operations.",
            "Apply sorting and filtering using WHERE, LIKE, IN, and BETWEEN.",
            "Use GROUP BY with aggregation functions and HAVING filters."
        ],
        "theory": [
            "CRUD: Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).",
            "Filtering: WHERE conditions limit row processing. LIKE is used for pattern matching (e.g. `%gmail.com` matches gmail addresses).",
            "Grouping & Aggregation: GROUP BY collapses rows based on key columns. Aggregation functions (COUNT, SUM, AVG, MIN, MAX) resolve aggregate computations. HAVING filters rows AFTER group creation (unlike WHERE which filters before grouping)."
        ],
        "coding_exercise": {
            "title": "Filter Student Course Enrolments",
            "instructions": "Write queries executing INSERT commands and querying counts of enrolled courses with total averages.",
            "stub": """-- Insert initial data
INSERT INTO Courses (CourseTitle, Credits) VALUES ('ML basics', 4), ('ASP.NET Web Dev', 3);

-- Select grouped counts of course enrollments
SELECT CourseTitle, SUM(Credits) as TotalCredits 
FROM Courses 
GROUP BY CourseTitle 
HAVING SUM(Credits) >= 3;"""
        },
        "mini_challenge": "Write a query retrieving students registered in the current calendar month containing 'gmail' domains in their email details.",
        "common_mistakes": [
            "Using DELETE statements without a WHERE clause, wiping out all table records.",
            "Using WHERE keyword to filter aggregation outputs instead of using HAVING."
        ],
        "interview_questions": [
            {
                "q": "What is the difference between WHERE and HAVING clauses?",
                "a": "WHERE filters source records before grouping. HAVING filters grouped rows after aggregation functions are evaluated."
            },
            {
                "q": "Explain the difference between DELETE and TRUNCATE commands.",
                "a": "DELETE is a DML operation that removes specific rows based on conditions and writes logs for each deleted row. TRUNCATE is a DDL operation that clears the entire table by deallocating pages, running much faster and bypassing individual logs."
            }
        ],
        "homework": "Write a script inserting 10 students with varying grades, then select the top 3 students based on average credit performance.",
        "revision_checklist": [
            "I can write parameterized INSERT query logic.",
            "I know when to apply HAVING vs WHERE.",
            "I understand row tracking using IDENTITY."
        ]
    },
    {
        "day_num": 10,
        "title": "SQL Joins & Data Assembly",
        "objectives": [
            "Master merging data across relational tables using Joins.",
            "Analyze INNER, LEFT, RIGHT, FULL, and CROSS joins.",
            "Use self-joins to manage hierarchical table layouts."
        ],
        "theory": [
            "Joins combine records across multiple tables using common columns.",
            "INNER JOIN: Returns matching rows in both tables.",
            "LEFT JOIN: Returns all rows from left table, with matches from right table (adds NULL if no match exists).",
            "RIGHT JOIN: Returns all rows from right table, with matches from left table.",
            "FULL JOIN: Merges LEFT and RIGHT results.",
            "SELF JOIN: Join a table to itself (e.g. matching employees to their managers)."
        ],
        "coding_exercise": {
            "title": "Student Course Registration Join Query",
            "instructions": "Query matching student names with their corresponding course titles through enrollment tables using LEFT and INNER joins.",
            "stub": """-- Assume StudentCourses mapping table exists
SELECT s.FirstName, s.LastName, c.CourseTitle 
FROM Students s
INNER JOIN StudentCourses sc ON s.StudentID = sc.StudentID
INNER JOIN Courses c ON sc.CourseID = c.CourseID;"""
        },
        "mini_challenge": "Query all courses, listing registered students, including courses that have no registered students (hint: use LEFT JOIN).",
        "common_mistakes": [
            "Not defining table aliases, leading to ambiguous columns syntax errors.",
            "Selecting inappropriate columns during large joins, slowing down database systems."
        ],
        "interview_questions": [
            {
                "q": "What happens when you do a LEFT JOIN but the right table lacks matching rows?",
                "a": "All columns retrieved from the right table will contain NULL values for those rows."
            },
            {
                "q": "What is the difference between UNION and UNION ALL?",
                "a": "UNION merges data from two SELECT queries and removes duplicate records. UNION ALL merges results and keeps all duplicates, running faster as it skips the deduplication step."
            }
        ],
        "homework": "Build an organizational table structure (Employees, Managers) where manager references employee ID. Write a self-join query displaying employee and manager names.",
        "revision_checklist": [
            "I know when to use LEFT JOIN instead of INNER JOIN.",
            "I can write table relationships using aliases.",
            "I know the performance cost of JOIN tables."
        ]
    },
    {
        "day_num": 11,
        "title": "Database Constraints & Index Tuning",
        "objectives": [
            "Utilize SQL database constraints (CHECK, DEFAULT, UNIQUE).",
            "Learn how indexes speed up data querying.",
            "Contrast Clustered Indexes vs Non-Clustered Indexes."
        ],
        "theory": [
            "Constraints enforce schema rules. CHECK restricts data ranges. DEFAULT applies pre-configured values when fields are left empty.",
            "Indexes: Performance structures mapped on tables.",
            "Clustered Index: Sorts physical data rows in the database based on key values. Only one Clustered Index per table (usually Primary Key).",
            "Non-Clustered Index: Separate structure matching key data to pointers where values exist. Multiple indexes are allowed, which is useful for searching fields."
        ],
        "coding_exercise": {
            "title": "Creating Custom Clustered and Non-Clustered Indexes",
            "instructions": "Define a table and write scripts creating indexes on heavily searched columns (like email fields).",
            "stub": """-- Create a Non-Clustered Index on Email field
CREATE NONCLUSTERED INDEX IX_Students_Email 
ON Students(Email);

-- Verify execution plans using lookup scripts
SELECT * FROM Students WHERE Email = 'test@example.com';"""
        },
        "mini_challenge": "Add a CHECK constraint on the Students table enforcing age ranges (e.g. verifying students are over 16).",
        "common_mistakes": [
            "Over-indexing tables (each index slows down INSERT, UPDATE, and DELETE operations as indexes must be updated).",
            "Underestimating index size requirements in storage systems."
        ],
        "interview_questions": [
            {
                "q": "What is the main difference between Clustered and Non-Clustered indexes?",
                "a": "A Clustered index physically sorts the data in the table itself. A Non-Clustered index stores key values with pointers pointing to real data storage locations."
            },
            {
                "q": "Why do indexes slow down database write operations?",
                "a": "Because every time a write occurs (INSERT, UPDATE, DELETE), the SQL Server engine must update both the base table data and the associated index tree structures."
            }
        ],
        "homework": "Research and write queries displaying query plan indexes from system catalog views in SQL Server.",
        "revision_checklist": [
            "I know how to create a Non-Clustered index.",
            "I know the performance impact of duplicate indexes.",
            "I can explain table scan vs index seek."
        ]
    },
    {
        "day_num": 12,
        "title": "Stored Procedures & SQL Functions",
        "objectives": [
            "Write modular, reusable Stored Procedures in SQL Server.",
            "Pass input and output parameters to procedures.",
            "Contrast Stored Procedures against Scalar/Table-Valued Functions."
        ],
        "theory": [
            "Stored Procedures (SPs): Pre-compiled sets of SQL statements stored on the server. They reduce network overhead, improve security by hiding base tables, and prevent SQL injection attacks.",
            "Input vs Output parameters: Input passes runtime parameters. Output parameters return execution values.",
            "Functions: Scalar (returns single value) vs Table-Valued (returns a virtual table). Functions cannot perform write operations (INSERT, UPDATE, DELETE) inside their execution boundaries, whereas Stored Procedures can."
        ],
        "coding_exercise": {
            "title": "Create Registration Stored Procedure",
            "instructions": "Write an SP that takes student details, inserts the row, and returns the newly generated StudentID via an output parameter.",
            "stub": """CREATE PROCEDURE sp_RegisterStudent
    @FirstName NVARCHAR(50),
    @LastName NVARCHAR(50),
    @Email NVARCHAR(100),
    @NewID INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    INSERT INTO Students (FirstName, LastName, Email)
    VALUES (@FirstName, @LastName, @Email);
    
    SET @NewID = SCOPE_IDENTITY();
END;"""
        },
        "mini_challenge": "Create a Table-Valued function returning a list of students enrolled in a specified course parameter.",
        "common_mistakes": [
            "Writing business logic entirely in Stored Procedures instead of keeping it in C# backend APIs.",
            "Using SPs with wildcard SELECT operations, causing network bottlenecks."
        ],
        "interview_questions": [
            {
                "q": "Why are Stored Procedures pre-compiled?",
                "a": "When created, their execution plans are generated and cached in memory. Subsequent calls skip parsing and compilation, executing instantly."
            },
            {
                "q": "Can you call a Stored Procedure inside a SQL Function?",
                "a": "No, because SQL Functions are not allowed to perform operations that modify database state or run arbitrary logic, which SPs can execute."
            }
        ],
        "homework": "Write a stored procedure executing course allocation logic, validating that a course exists before performing an insert to avoid foreign key failures.",
        "revision_checklist": [
            "I can write a Stored Procedure with Output parameters.",
            "I understand the difference between Functions and Stored Procedures.",
            "I know how to call stored procedures using parameters."
        ]
    },
    {
        "day_num": 13,
        "title": "SQL Transactions & ACID properties",
        "objectives": [
            "Understand the ACID properties of database transactions.",
            "Implement transactional execution blocks (Commit and Rollback).",
            "Learn concurrency isolation levels and locking."
        ],
        "theory": [
            "ACID: Atomicity (all or nothing), Consistency (preserves schema rules), Isolation (independent execution transactions), Durability (persisted on disk).",
            "Isolation Levels: Controls how databases handle concurrency anomalies (Dirty reads, Non-repeatable reads, Phantom reads) using locks. Common levels: Read Committed, Serializable, Snapshot.",
            "Transaction flow: `BEGIN TRANSACTION`, process data, run `COMMIT` to save or `ROLLBACK` on errors."
        ],
        "coding_exercise": {
            "title": "Safe Course Registration Transaction",
            "instructions": "Write a transaction executing course registrations and decrementing class capacity safely. Rollback transaction state on error.",
            "stub": """BEGIN TRANSACTION;

BEGIN TRY
    -- Insert mapping
    INSERT INTO StudentCourses (StudentID, CourseID) VALUES (1, 1);
    
    -- Simulate validation failure or update constraint
    -- UPDATE Courses SET Capacity = Capacity - 1 WHERE CourseID = 1;
    
    COMMIT TRANSACTION;
    PRINT 'Transaction committed successfully.';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'Error occurred, transaction rolled back.';
    THROW;
END CATCH;"""
        },
        "mini_challenge": "Set transaction isolation level to SNAPSHOT and write a script explaining why snapshot isolation prevents transaction reading blocks.",
        "common_mistakes": [
            "Forgetting to write COMMIT or ROLLBACK, leaving transactions open and locking database tables for other users.",
            "Using nested transactions without tracking transaction counters, causing rollback mismatches."
        ],
        "interview_questions": [
            {
                "q": "What does Atomicity mean in ACID?",
                "a": "Atomicity ensures that all operations in a transaction either complete successfully together or none of them do, restoring database state back to its original condition on failure."
            },
            {
                "q": "What is a Deadlock in SQL Server?",
                "a": "A deadlock occurs when two transactions hold locks on separate resources, and each transaction tries to acquire a lock on the resource held by the other, causing a circular block. SQL Server automatically kills one transaction as the deadlock victim."
            }
        ],
        "homework": "Implement a transactional scenario processing student enrollment fees, verifying cash balances are checked and updated dynamically.",
        "revision_checklist": [
            "I understand ACID rules.",
            "I know when to write a ROLLBACK TRANSACTION block.",
            "I can explain isolation levels."
        ]
    },
    {
        "day_num": 14,
        "title": "Week 2 Review & Relational Schema Project",
        "objectives": [
            "Review Relational Design principles and normalizations.",
            "Build database schemas, table relations, and transaction logic.",
            "Debug deadlocks and database performance blocks."
        ],
        "theory": [
            "Review data integrity patterns. Verify table definitions match normal forms.",
            "Confirm that join queries write references correctly and indexes are built on primary/foreign keys.",
            "Review transaction error catch blocks to ensure connections are closed correctly."
        ],
        "coding_exercise": {
            "title": "Mini Project: E-Commerce Catalog & Orders Schema",
            "instructions": "Design a relational DB schema representing Customers, Products, Orders, and OrderItems. Create stored procedures with transactional rollback routines to place orders and update product inventory levels.",
            "stub": """-- Implement full schema creation scripts
-- Build sp_PlaceOrder executing safety transaction logic.
-- Seed mock data to verify schema behavior."""
        },
        "mini_challenge": "Identify and optimize a query that is executing slow table scans by adding a composite non-clustered index on customer details.",
        "common_mistakes": [
            "Failing to handle resource disposal in SQL catch blocks.",
            "Creating transactional code without error tracing."
        ],
        "interview_questions": [
            {
                "q": "What is database catalog in SQL Server?",
                "a": "A database catalog contains metadata about database structures including schemas, tables, relationships, and permissions."
            },
            {
                "q": "How does index fragmentation affect database queries?",
                "a": "Index fragmentation causes pages to split and data to scatter out of logical order. This forces extra physical disc I/O, slowing down read operations."
            }
        ],
        "homework": "Optimize the E-Commerce catalog: Write a stored procedure retrieving top-selling products using LEFT JOIN aggregation queries.",
        "revision_checklist": [
            "I built the E-Commerce Catalog & Orders Schema.",
            "I optimized queries using custom indexes.",
            "I understand ACID transaction mechanics."
        ]
    },

    # --- WEEK 3 ---
    {
        "day_num": 15,
        "title": "ASP.NET Core Project Structure",
        "objectives": [
            "Understand ASP.NET Core project organization templates.",
            "Learn Program.cs structure and the Middleware pipeline.",
            "Run .NET Web API command tools."
        ],
        "theory": [
            "Project Structure: ASP.NET Core projects contain `Program.cs` (app startup, service registration, configuration), `appsettings.json` (JSON configurations), and Controllers/Models folders.",
            "Program.cs: Replaces old Global.asax/Startup.cs in newer versions of .NET. Houses dependency injections and registers the middleware pipeline.",
            "Middleware Pipeline: Request processing units executed sequentially. Requests enter the pipeline, pass through each middleware, hit the endpoint, and the response travels back through the pipeline."
        ],
        "coding_exercise": {
            "title": "Analyze and Create custom Middleware pipeline",
            "instructions": "Build a basic ASP.NET Core Web API project using `dotnet new webapi` and inspect Program.cs pipeline creation.",
            "stub": """// Program.cs structure
var builder = WebApplication.CreateBuilder(args);

// Add services to the container
builder.Services.AddControllers();

var app = builder.Build();

// Configure the HTTP request pipeline
if (app.Environment.IsDevelopment()) {
    app.UseDeveloperExceptionPage();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();"""
        },
        "mini_challenge": "Run command terminal calls creating a Web API project named InventoryAPI using dotnet CLI.",
        "common_mistakes": [
            "Registering middleware in the incorrect order (e.g. putting Auth middleware before Routing, which breaks security checks).",
            "Adding heavy processing logic inside Program.cs instead of keeping it modular."
        ],
        "interview_questions": [
            {
                "q": "What is the role of Program.cs in ASP.NET Core?",
                "a": "Program.cs handles application configuration, sets up the web host (Kestrel), registers services in the Dependency Injection container, and defines the HTTP request middleware pipeline."
            },
            {
                "q": "What is Kestrel in ASP.NET Core?",
                "a": "Kestrel is a cross-platform, high-performance web server implementation embedded inside ASP.NET Core applications by default."
            }
        ],
        "homework": "Create a clean .NET Web API application, review project references and list assembly configuration files.",
        "revision_checklist": [
            "I can create a project via dotnet CLI.",
            "I understand Program.cs layout.",
            "I know what middleware is."
        ]
    },
    {
        "day_num": 16,
        "title": "Routing & Controller Basics",
        "objectives": [
            "Understand Attribute-based and Conventional routing models.",
            "Create API Controllers inheriting from ControllerBase.",
            "Return HTTP status codes using ActionResult types."
        ],
        "theory": [
            "Controllers: Process HTTP requests and return responses. They inherit from `ControllerBase` (provides access to model validation state and helper methods for HTTP status codes).",
            "Attribute Routing: Preferred for REST Web APIs. Directly maps endpoints using attributes (e.g., `[Route(\"api/[controller]\")]`, `[HttpGet]`, `[HttpPost]`).",
            "Conventional Routing: Maps routes globally in Program.cs (standard in MVC apps, but less common in APIs)."
        ],
        "coding_exercise": {
            "title": "Simple HelloWorld Controller API",
            "instructions": "Implement a simple API controller executing action methods that return standard message status codes.",
            "stub": """using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class HelloController : ControllerBase {
    
    [HttpGet]
    public IActionResult GetWelcome() {
        return Ok(new { message = "Welcome to ASP.NET Core API!" });
    }
    
    [HttpGet("check/{id}")]
    public IActionResult CheckID(int id) {
        if (id <= 0) return BadRequest("Invalid ID parameter.");
        return Ok($"Value validated: {id}");
    }
}"""
        },
        "mini_challenge": "Create an API controller method using [HttpPost] returning a 201 Created Status result when receiving a text body.",
        "common_mistakes": [
            "Inheriting from Controller instead of ControllerBase (Controller contains View helper logic which is unneeded and wastes memory in Web APIs).",
            "Hardcoding response messages inside routes instead of using dynamic parameters."
        ],
        "interview_questions": [
            {
                "q": "What is the difference between Controller and ControllerBase classes?",
                "a": "ControllerBase provides helper functions for REST API actions (Ok, BadRequest, etc.). Controller inherits from ControllerBase and adds support for Razor Views, which is not needed for Web APIs."
            },
            {
                "q": "What is Attribute Routing?",
                "a": "Attribute routing maps URI routes to specific controller actions using C# attributes directly on the class or methods, offering precise endpoint design control."
            }
        ],
        "homework": "Create a controller simulating a simplified Calculator API, exposing routes to perform math calculations via parameter segments.",
        "revision_checklist": [
            "I can build a ControllerBase API controller.",
            "I know how to return ActionResult statuses.",
            "I understand path parameters in routing."
        ]
    },
    {
        "day_num": 17,
        "title": "Middleware Pipeline Customization",
        "objectives": [
            "Understand the Request/Response execution flow in middleware.",
            "Write custom inline middleware in Program.cs.",
            "Create reusable Custom Middleware classes."
        ],
        "theory": [
            "Middleware: Software components that compile request handlers. They intercept, inspect, or modify incoming HTTP requests and outgoing responses.",
            "Each middleware chooses whether to pass the request to the next component in the pipeline (`next()`) or short-circuit the execution (e.g. if authentication fails).",
            "Common uses: Exception handling, Request logging, Authentication checking, CORS configuration."
        ],
        "coding_exercise": {
            "title": "Build Request Execution Time Logger Middleware",
            "instructions": "Implement custom middleware measuring request performance time and printing results in console outputs.",
            "stub": """using Microsoft.AspNetCore.Http;
using System.Diagnostics;
using System.Threading.Tasks;

public class PerformanceMiddleware {
    private readonly RequestDelegate _next;

    public PerformanceMiddleware(RequestDelegate next) {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context) {
        var watch = Stopwatch.StartNew();
        
        // Pass request down the pipeline
        await _next(context); 
        
        watch.Stop();
        System.Console.WriteLine($"Request took {watch.ElapsedMilliseconds} ms to execute.");
    }
}"""
        },
        "mini_challenge": "Create custom inline middleware returning standard validation header tags inside Program.cs (e.g. using `app.Use()`).",
        "common_mistakes": [
            "Forgetting to call `await next(context)`, causing requests to freeze in the pipeline (short-circuiting).",
            "Attempting to write response header tags after pipeline responses have started sending."
        ],
        "interview_questions": [
            {
                "q": "Explain the middleware pipeline short-circuit concept.",
                "a": "If a middleware component decides not to call next(), it halts execution. It returns a response immediately, preventing subsequent middleware and controllers from running."
            },
            {
                "q": "What is the difference between app.Use and app.Run in middleware configuration?",
                "a": "app.Use can call the next middleware component in the pipeline using next(), while app.Run terminates the pipeline and never calls next()."
            }
        ],
        "homework": "Write reusable middleware inspecting request authorization tokens, returning a 401 status if keys are missing.",
        "revision_checklist": [
            "I know how to intercept HTTP requests.",
            "I can implement custom middleware classes.",
            "I understand the RequestDelegate delegate type."
        ]
    },
    {
        "day_num": 18,
        "title": "Configuration & Application Settings",
        "objectives": [
            "Manage settings inside appsettings.json.",
            "Retrieve configuration keys using IConfiguration.",
            "Bind configuration options using Options Patterns."
        ],
        "theory": [
            "Configuration: ASP.NET Core loads configs from JSON files (`appsettings.json`), environment variables, user secrets, and command arguments.",
            "IConfiguration: Service interface used to fetch config values using string keys (e.g. `_config[\"Database:ConnectionString\"]`).",
            "Options Pattern: Binds configuration blocks directly to strongly-typed C# classes, ensuring clean code and validation support."
        ],
        "coding_exercise": {
            "title": "Read Connection String from Configuration",
            "instructions": "Configure key values in appsettings.json and access database connection strings inside dynamic action methods.",
            "stub": """// appsettings.json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=TestDB;Integrated Security=True;"
  }
}

// Controller
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;

[ApiController]
[Route("api/[controller]")]
public class ConfigController : ControllerBase {
    private readonly IConfiguration _config;
    
    public ConfigController(IConfiguration config) {
        _config = config;
    }
    
    [HttpGet("connection")]
    public IActionResult GetDbString() {
        var dbStr = _config.GetConnectionString("DefaultConnection");
        return Ok(new { connection = dbStr });
    }
}"""
        },
        "mini_challenge": "Create a strongly-typed class JwtSettings and map a JSON configuration section to it using IOptions pattern.",
        "common_mistakes": [
            "Hardcoding database connection strings directly in controller classes.",
            "Failing to add fallback configurations for non-development environments."
        ],
        "interview_questions": [
            {
                "q": "How does the Options Pattern work in ASP.NET Core?",
                "a": "It binds configuration sections to C# classes, registering them in the DI container so they can be injected using IOptions<T> references."
            },
            {
                "q": "Where does ASP.NET Core look for configuration values in production environments?",
                "a": "It checks multiple sources sequentially, including appsettings.json, environment-specific appsettings.Production.json, and OS Environment Variables."
            }
        ],
        "homework": "Add settings representing threshold values to config files, read them inside validation logic, and return appropriate errors if inputs exceed values.",
        "revision_checklist": [
            "I know how to read appsettings configurations.",
            "I can define nested configuration sections.",
            "I understand environment configurations."
        ]
    },
    {
        "day_num": 19,
        "title": "Dependency Injection & Service Lifetimes",
        "objectives": [
            "Understand Dependency Injection (DI) as a clean design pattern.",
            "Register services as Transient, Scoped, and Singleton.",
            "Prevent lifetime mismatch bugs (Captive Dependencies)."
        ],
        "theory": [
            "Dependency Injection (DI): A design pattern that decouples classes by injecting dependencies instead of creating them with 'new'. ASP.NET Core has a built-in IoC (Inversion of Control) container.",
            "Service Lifetimes:",
            "1. Transient: Created every time they are requested. Ideal for lightweight, stateless services.",
            "2. Scoped: Created once per HTTP request. Ideal for stateful services or database contexts.",
            "3. Singleton: Created once on first request and shared across all subsequent requests. Ideal for caches.",
            "Captive Dependency: Occurs when a long-lived service (Singleton) incorrectly captures a short-lived service (Scoped). Since the Singleton never dies, the Scoped service is kept alive indefinitely, leading to memory leaks and thread-safety bugs."
        ],
        "coding_exercise": {
            "title": "DI Lifetimes Demonstration API",
            "instructions": "Implement interfaces tracking lifetime IDs and verify how GUIDs change across Transient, Scoped, and Singleton scopes.",
            "stub": """using System;

public interface ILifetimeService { Guid Id { get; } }
public interface ITransientService : ILifetimeService {}
public interface IScopedService : ILifetimeService {}
public interface ISingletonService : ILifetimeService {}

public class LifetimeService : ITransientService, IScopedService, ISingletonService {
    public Guid Id { get; } = Guid.NewGuid();
}"""
        },
        "mini_challenge": "Register the services in Program.cs and create a controller injecting all three services, showing differences in return results across requests.",
        "common_mistakes": [
            "Injecting Scoped services (like DB contexts) into Singleton services, causing thread synchronization failures.",
            "Creating objects manually with 'new' instead of leveraging the IoC container."
        ],
        "interview_questions": [
            {
                "q": "Explain the difference between Transient, Scoped, and Singleton lifetimes.",
                "a": "Transient creates a new instance on every request. Scoped creates a single instance per HTTP request. Singleton creates a single instance shared across all application threads."
            },
            {
                "q": "What is a captive dependency?",
                "a": "A captive dependency occurs when a service with a longer lifetime contains a dependency with a shorter lifetime (e.g., injecting a Scoped service into a Singleton class)."
            }
        ],
        "homework": "Register a custom mock AI model evaluation service using the interface abstraction pattern and call it inside your backend controller via constructors.",
        "revision_checklist": [
            "I understand IoC containers.",
            "I know when to use Scoped services.",
            "I can diagnose captive dependencies."
        ]
    },
    {
        "day_num": 20,
        "title": "Structured Logging with ILogger & Serilog",
        "objectives": [
            "Inject and use default ILogger inside API controllers.",
            "Configure Serilog to output log streams.",
            "Implement structured logging for search optimizations."
        ],
        "theory": [
            "Logging: Vital for production diagnostics. Default logs write text data. Structured logging records events as structured key-value pairs (JSON), making searches fast in log analytics engines (ElasticSearch, Datadog).",
            "Serilog: A third-party library that replaces the built-in logger, outputting structured logs to files, databases, or cloud endpoints (sinks).",
            "Log Levels: Trace, Debug, Information, Warning, Error, Critical."
        ],
        "coding_exercise": {
            "title": "Configuring Logger inside controllers",
            "instructions": "Inject `ILogger<HelloController>` and write log statements recording method execution paths and performance metrics.",
            "stub": """using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

[ApiController]
[Route("api/[controller]")]
public class LogController : ControllerBase {
    private readonly ILogger<LogController> _logger;
    
    public LogController(ILogger<LogController> logger) {
        _logger = logger;
    }
    
    [HttpGet]
    public IActionResult LogTest() {
        _logger.LogInformation("Processing calculation request for {Time}", System.DateTime.UtcNow);
        return Ok("Logged");
    }
}"""
        },
        "mini_challenge": "Configure Serilog in Program.cs to output JSON formatted logs to a local file named 'api_log.json'.",
        "common_mistakes": [
            "Using string interpolation (e.g. `$"User {userId} logged in"`) which breaks structured search indexing (always use property placeholders: `_logger.LogInformation("User {UserId} logged in", userId)`).",
            "Logging sensitive data like user passwords or authorization tokens."
        ],
        "interview_questions": [
            {
                "q": "What is Structured Logging and why is it preferred in production?",
                "a": "Structured logging writes logs as searchable JSON objects rather than plain text strings. This allows log management systems to index and query logs based on key parameters."
            },
            {
                "q": "How do you configure logging filters in appsettings.json?",
                "a": "You set levels inside the 'Logging:LogLevel' node (e.g., Default: Warning, Microsoft.AspNetCore: Information) to control log volume."
            }
        ],
        "homework": "Implement error-logging middleware that intercepts exceptions and logs structured error descriptions, including request IDs.",
        "revision_checklist": [
            "I understand log level hierarchies.",
            "I can write structured log statements.",
            "I know how to install and setup Serilog."
        ]
    },
    {
        "day_num": 21,
        "title": "Week 3 Review & Web API Service Setup",
        "objectives": [
            "Review ASP.NET Core project setup and configurations.",
            "Resolve DI issues and configure logging output structures.",
            "Execute API pipeline validations."
        ],
        "theory": [
            "Review registration patterns. Double-check service lifetime dependencies.",
            "Check that configurations load environment properties properly.",
            "Ensure that logging levels don't leak debug information in production environments."
        ],
        "coding_exercise": {
            "title": "Mini Project: Configurable Logger Web API",
            "instructions": "Create an API with a custom logger middleware that logs request execution times, routes, and client IP addresses. Inject a configurable service to dynamically return custom greeting text depending on appsettings.json setup.",
            "stub": """// Create custom middleware class
// Write Program.cs registering services
// Build controller reading configuration mapping configurations."""
        },
        "mini_challenge": "Identify a dependency error in code where a transient client creates a scoped db context parameter inside a singleton logger, and refactor it.",
        "common_mistakes": [
            "Forgetting exception handler middleware configurations.",
            "Failing to structure environment settings."
        ],
        "interview_questions": [
            {
                "q": "Explain Dependency Injection scopes in multi-threaded environments.",
                "a": "Each HTTP request represents an isolated execution thread thread context. Scoped dependencies are instantiated once per thread context and are disposed when the request concludes."
            },
            {
                "q": "Can you configure custom middleware using extension methods?",
                "a": "Yes. You can write extension functions extending `IApplicationBuilder` to build neat calls like `app.UseCustomLogging();`."
            }
        ],
        "homework": "Extend the logger service: Add configuration options verifying that headers contain required API validation keys before allowing execution.",
        "revision_checklist": [
            "I built the Configurable Logger Web API.",
            "I resolved service lifetime errors.",
            "I understand the middleware invocation model."
        ]
    },

    # --- WEEK 4 ---
    {
        "day_num": 22,
        "title": "REST API Principles & HTTP Verbs",
        "objectives": [
            "Understand REST architecture standards and resources.",
            "Use HTTP verbs (GET, POST, PUT, DELETE) appropriately.",
            "Return HTTP status codes mapped to actions."
        ],
        "theory": [
            "REST (Representational State Transfer): An architectural style using HTTP protocols to manipulate resources. Resources are identified by URIs (e.g. `/api/students`).",
            "HTTP Verbs:",
            "- GET: Read resources (Idempotent, safe).",
            "- POST: Create resource (Non-idempotent).",
            "- PUT: Replace resource completely (Idempotent).",
            "- DELETE: Remove resource (Idempotent).",
            "Status Codes: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)."
        ],
        "coding_exercise": {
            "title": "Design Student REST Resource API",
            "instructions": "Create a controller class executing standard student operations mapped to appropriate HTTP status codes.",
            "stub": """using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class StudentsController : ControllerBase {
    private static readonly List<string> _students = new() { "Alice", "Bob" };

    [HttpGet]
    public IActionResult GetAll() => Ok(_students);

    [HttpPost]
    public IActionResult Create([FromBody] string name) {
        _students.Add(name);
        return CreatedAtAction(nameof(GetAll), new { name = name });
    }
}"""
        },
        "mini_challenge": "Add PUT and DELETE endpoints to the StudentsController. Verify PUT replaces names by array index references.",
        "common_mistakes": [
            "Using POST routes for everything instead of matching routes with correct HTTP verbs.",
            "Returning 200 OK statuses when resource queries result in Null or Not Found values (always return 404)."
        ],
        "interview_questions": [
            {
                "q": "What does idempotency mean in REST APIs?",
                "a": "An HTTP method is idempotent if executing it multiple times yields the same result and state. GET, PUT, and DELETE are idempotent; POST is not."
            },
            {
                "q": "What is the difference between PUT and PATCH?",
                "a": "PUT replaces the target resource entirely with the request payload. PATCH modifies only the specified parts of the resource."
            }
        ],
        "homework": "Build an API structure representing course inventory products. Map CRUD operations to correct REST verbs and status code results.",
        "revision_checklist": [
            "I understand HTTP method differences.",
            "I can design REST URIs.",
            "I know when to return 201 vs 200."
        ]
    },
    {
        "day_num": 23,
        "title": "Model Binding & Validation (DataAnnotations & FluentValidation)",
        "objectives": [
            "Learn how MVC binds payloads via [FromBody], [FromRoute], and [FromQuery].",
            "Enforce constraints using DataAnnotations.",
            "Build fluent validation rules using FluentValidation library."
        ],
        "theory": [
            "Model Binding: ASP.NET Core maps request parameters from various sources: Body (JSON payloads), Route (URL parameters), Query (URL search queries).",
            "Validation: Ensures input data meets business rules before processing. DataAnnotations use attributes (e.g., `[Required]`, `[EmailAddress]`). FluentValidation is a popular library that keeps validation logic separate from models, making it cleaner and easier to test."
        ],
        "coding_exercise": {
            "title": "Validate Registration Requests",
            "instructions": "Create a registration model class utilizing DataAnnotations. Verify model states inside controllers.",
            "stub": """using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc;

public class RegisterDto {
    [Required]
    [EmailAddress]
    public string Email { get; set; }

    [Required]
    [StringLength(20, MinimumLength = 6, ErrorMessage = "Password must be 6-20 characters.")]
    public string Password { get; set; }
}

// Controller logic validates ModelState.IsValid automatically in [ApiController]"""
        },
        "mini_challenge": "Install FluentValidation and build a custom validator for a StudentDto checking that student age ranges meet minimum constraints.",
        "common_mistakes": [
            "Executing database operations with unvalidated parameters, inviting SQL injection or schema issues.",
            "Neglecting validation messages, leading to poor user experiences."
        ],
        "interview_questions": [
            {
                "q": "Where does Model Binding look for parameters by default?",
                "a": "It checks parameters in query strings, route values, and form fields sequentially. Complex object parameters are assumed to come from the request body."
            },
            {
                "q": "How does [ApiController] handle invalid model validation?",
                "a": "It automatically short-circuits the request and returns a 400 Bad Request response containing the validation errors, removing the need to manually check ModelState.IsValid in controllers."
            }
        ],
        "homework": "Write a validation configuration class checking that course registrations contains valid enrollment ranges and dates.",
        "revision_checklist": [
            "I know the difference between FromBody and FromQuery.",
            "I can define model validation attributes.",
            "I understand the role of Dto classes."
        ]
    },
    {
        "day_num": 24,
        "title": "Swagger Documentation & Global Error Handling",
        "objectives": [
            "Set up Swagger/OpenAPI inside your ASP.NET Core project.",
            "Customize Swagger layout using XML doc comments.",
            "Build custom Global Exception Handling middleware."
        ],
        "theory": [
            "Swagger: Evaluates API structures and generates interactive API documentation. This allows frontend developers and integration systems to test endpoints.",
            "Global Exception Handling: Crucial for production. Instead of wrapping every controller action in try-catch blocks, configure global exception handling middleware. It intercepts uncaught exceptions, logs them, and returns a clean, standardized JSON error response (like RFC 7807 Problem Details) to the client without exposing internal stack traces."
        ],
        "coding_exercise": {
            "title": "Global Exception Handler Middleware",
            "instructions": "Implement global exception handling middleware that catches all unhandled exceptions and returns a structured JSON payload.",
            "stub": """using Microsoft.AspNetCore.Http;
using System.Text.Json;
using System.Threading.Tasks;

public class ExceptionHandlerMiddleware {
    private readonly RequestDelegate _next;

    public ExceptionHandlerMiddleware(RequestDelegate next) {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context) {
        try {
            await _next(context);
        }
        catch (System.Exception ex) {
            context.Response.ContentType = "application/json";
            context.Response.StatusCode = 500;
            
            var response = new { error = "An unexpected error occurred.", detail = ex.Message };
            await context.Response.WriteAsync(JsonSerializer.Serialize(response));
        }
    }
}"""
        },
        "mini_challenge": "Enable Swagger XML documentation generation in the .csproj file and use triple-slash (///) comments on a controller to document parameter limits.",
        "common_mistakes": [
            "Leaking raw database or connection error traces inside API responses in production environments.",
            "Failing to exclude Swagger UI paths in production setup configuration."
        ],
        "interview_questions": [
            {
                "q": "What is Swagger and how does it benefit API development?",
                "a": "Swagger automatically inspects endpoints to generate interactive, self-updating API documentation, allowing developers to test HTTP calls directly from the browser."
            },
            {
                "q": "What is the recommended way to handle errors globally in ASP.NET Core?",
                "a": "By using a custom Exception Handler Middleware or registering a Developer Exception Page in local development environments."
            }
        ],
        "homework": "Add custom error statuses to your exception middleware to return a 400 status code on validation exceptions and a 500 status code on standard errors.",
        "revision_checklist": [
            "I know how to set up Swagger UI.",
            "I can construct global exception catch middleware.",
            "I understand standard API error formats."
        ]
    },
    {
        "day_num": 25,
        "title": "Dapper ORM Installation & CRUD Operations",
        "objectives": [
            "Install Dapper NuGet packages.",
            "Connect to SQL databases using SqlConnection.",
            "Write fast CRUD queries mapping raw SQL output to C# objects."
        ],
        "theory": [
            "ORM (Object Relational Mapper): Bridges the gap between OOP objects and relational databases. Entity Framework (EF Core) is a full-featured ORM, whereas Dapper is a 'Micro-ORM'.",
            "Why Dapper? It is lightweight and exceptionally fast (almost as fast as ADO.NET). It extends `IDbConnection` with helper methods like `Query<T>` and `Execute` that map query results directly to C# models using raw SQL.",
            "Security: Avoid SQL Injection by always passing parameters as anonymous objects (e.g. `new { Id = studentId }`). Never use string concatenation."
        ],
        "coding_exercise": {
            "title": "Execute Dapper Queries",
            "instructions": "Write an endpoint querying records from your SQL database and mapping records directly to a student class using Dapper.",
            "stub": """using Dapper;
using Microsoft.Data.SqlClient;
using System.Collections.Generic;
using System.Threading.Tasks;

public class StudentRepository {
    private readonly string _connectionString = "Server=localhost;Database=StudentDB;Trusted_Connection=True;";
    
    public async Task<IEnumerable<Student>> GetStudentsAsync() {
        using var connection = new SqlConnection(_connectionString);
        string sql = "SELECT * FROM Students";
        return await connection.QueryAsync<Student>(sql);
    }
}

public class Student {
    public int StudentID { get; set; }
    public string FirstName { get; set; }
}"""
        },
        "mini_challenge": "Create a Dapper script that executes parameterized inserts (`connection.ExecuteAsync`) adding new students to databases.",
        "common_mistakes": [
            "Writing query parameters using string interpolation, exposing database engines to SQL injection risks.",
            "Leaving database connections open (always wrap connections in 'using' blocks or initialize them inside using scopes)."
        ],
        "interview_questions": [
            {
                "q": "Why is Dapper called a Micro-ORM?",
                "a": "Because unlike full ORMs like EF Core, Dapper does not track object states, manage migrations, or generate SQL queries. It only handles mapping raw SQL outputs to C# objects."
            },
            {
                "q": "How does Dapper prevent SQL Injection?",
                "a": "By using parameterized queries where parameter values are passed as anonymous C# objects, separating query logic from data values."
            }
        ],
        "homework": "Implement a CRUD class executing UPDATE and DELETE operations using Dapper command mappings.",
        "revision_checklist": [
            "I can install NuGet packages via CLI.",
            "I know the difference between QueryAsync and ExecuteAsync.",
            "I can write parameterized queries."
        ]
    },
    {
        "day_num": 26,
        "title": "Dapper Stored Procedures & Repository Pattern",
        "objectives": [
            "Call SQL Stored Procedures using Dapper.",
            "Implement Repository Patterns to decouple database logic.",
            "Manage database connections via Dependency Injection."
        ],
        "theory": [
            "Repository Pattern: A design pattern that acts as an in-memory collection of domain objects. It decouples the database access code (SQL, Dapper, EF) from the application business logic (Controllers).",
            "By defining repositories as interfaces (e.g. `IStudentRepository`), controllers rely on abstractions. This makes testing easy via mock repositories.",
            "Stored Procedures in Dapper: Call procedures by passing the procedure name and specifying `CommandType.StoredProcedure`."
        ],
        "coding_exercise": {
            "title": "Call Stored Procedures with Dapper",
            "instructions": "Implement a generic repository method executing Stored Procedures with input/output variables using Dapper parameters.",
            "stub": """using Dapper;
using Microsoft.Data.SqlClient;
using System.Data;
using System.Threading.Tasks;

public interface IStudentRepository {
    Task<int> RegisterStudentAsync(string first, string last, string email);
}

public class DapperStudentRepository : IStudentRepository {
    private readonly string _connStr = "Server=localhost;Database=StudentDB;Trusted_Connection=True;";
    
    public async Task<int> RegisterStudentAsync(string first, string last, string email) {
        using var conn = new SqlConnection(_connStr);
        var parameters = new DynamicParameters();
        parameters.Add("@FirstName", first);
        parameters.Add("@LastName", last);
        parameters.Add("@Email", email);
        parameters.Add("@NewID", dbType: DbType.Int32, direction: ParameterDirection.Output);
        
        await conn.ExecuteAsync("sp_RegisterStudent", parameters, commandType: CommandType.StoredProcedure);
        return parameters.Get<int>("@NewID");
    }
}"""
        },
        "mini_challenge": "Register the IStudentRepository in Program.cs as a Scoped service and inject it into your StudentsController constructor.",
        "common_mistakes": [
            "Failing to define interfaces, making application controller layers difficult to unit test.",
            "Manually instantiating connection repositories instead of injecting configuration lifetimes."
        ],
        "interview_questions": [
            {
                "q": "What is the primary benefit of the Repository Pattern?",
                "a": "It abstracts database access details from the application controllers, creating a decoupled structure that is easy to test and maintain."
            },
            {
                "q": "How does Dapper handle stored procedure execution?",
                "a": "By passing parameters as DynamicParameters and setting the commandType argument to CommandType.StoredProcedure."
            }
        ],
        "homework": "Implement a repository matching course tables, exposing interface operations to retrieve courses using specialized stored procedures.",
        "revision_checklist": [
            "I can write interface repository abstractions.",
            "I know how to map DynamicParameters in Dapper.",
            "I understand connection lifecycle registration in DI."
        ]
    },
    {
        "day_num": 27,
        "title": "JWT Authentication & Role-Based Authorization",
        "objectives": [
            "Understand authentication and authorization concepts.",
            "Generate JSON Web Tokens (JWT) using security signing keys.",
            "Enforce role-based access policies in controllers."
        ],
        "theory": [
            "Authentication: Verifies who the user is (e.g. Username/Password validation).",
            "Authorization: Verifies what the authenticated user is allowed to do (e.g. Roles/Permissions).",
            "JWT (JSON Web Token): A secure, compact, self-contained way of transmitting claims as a JSON object signed using cryptographic keys. It consists of a Header, Payload (claims like UserId and Roles), and Signature.",
            "Security: The token is stateless. The backend validates the signature using security keys configured in the pipeline."
        ],
        "coding_exercise": {
            "title": "Generate JWT Web Tokens",
            "instructions": "Write helper services returning valid JWT strings containing user claim parameters.",
            "stub": """using Microsoft.IdentityModel.Tokens;
using System;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

public class TokenService {
    public string GenerateToken(string username, string role) {
        var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("SuperSecretKeyMustBe32BytesLong!!"));
        var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);
        
        var claims = new[] {
            new Claim(ClaimTypes.Name, username),
            new Claim(ClaimTypes.Role, role)
        };
        
        var token = new JwtSecurityToken(
            issuer: "MyApi",
            audience: "MyClients",
            claims: claims,
            expires: DateTime.Now.AddHours(2),
            signingCredentials: creds
        );
        
        return new JwtSecurityTokenHandler().WriteToken(token);
    }
}"""
        },
        "mini_challenge": "Configure JWT Bearer authentication in Program.cs and secure a controller method using `[Authorize(Roles = "Admin")]`.",
        "common_mistakes": [
            "Exposing sensitive security keys in source code (always load security keys from environment variables or User Secrets).",
            "Using short cryptographic keys that fail minimum length requirements for HmacSha256 signing."
        ],
        "interview_questions": [
            {
                "q": "What are the three components of a JWT token?",
                "a": "A JWT consists of a Header (metadata and algorithm), a Payload (claims and expiration details), and a Signature (verifies integrity)."
            },
            {
                "q": "What is the difference between [Authorize] and policy-based authorization?",
                "a": "[Authorize] checks basic roles or logins. Policy-based authorization combines multiple claims and validation rules (e.g. requiring a specific email domain and manager status)."
            }
        ],
        "homework": "Implement login controllers that validate mock credentials and return generated tokens inside JSON responses.",
        "revision_checklist": [
            "I know how JWT authorization headers are formatted.",
            "I understand symmetric security keys.",
            "I can secure controllers using claims."
        ]
    },
    {
        "day_num": 28,
        "title": "FastAPI Integration & External API Calls",
        "objectives": [
            "Understand API Integration patterns (Gateway to ML Service).",
            "Use HttpClient and IHttpClientFactory to send HTTP requests.",
            "Integrate external Python FastAPI endpoints."
        ],
        "theory": [
            "AI/ML Integration: AI models are usually built in Python (due to robust library support). In production, an ASP.NET Core gateway API handles authorization, logging, and rate limiting, then forwards payloads to a lightweight Python FastAPI service that executes the model.",
            "HttpClient: Best managed via `IHttpClientFactory` to prevent socket exhaustion bugs (where port connections are left open, locking network access).",
            "Data handling: Convert payloads to JSON using `System.Text.Json`."
        ],
        "coding_exercise": {
            "title": "Call FastAPI prediction service",
            "instructions": "Inject IHttpClientFactory and write async code calling a model prediction endpoint, passing input features and parsing response structures.",
            "stub": """using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class PredictController : ControllerBase {
    private readonly IHttpClientFactory _clientFactory;
    
    public PredictController(IHttpClientFactory clientFactory) {
        _clientFactory = clientFactory;
    }
    
    [HttpPost("classify")]
    public async Task<IActionResult> GetClassification([FromBody] float[] features) {
        var client = _clientFactory.CreateClient();
        
        // Target python FastAPI local endpoint
        var response = await client.PostAsJsonAsync("http://localhost:8000/predict", new { inputs = features });
        
        if (!response.IsSuccessStatusCode) return StatusCode((int)response.StatusCode, "ML Model execution failed.");
        
        var result = await response.Content.ReadFromJsonAsync<object>();
        return Ok(result);
    }
}"""
        },
        "mini_challenge": "Create a dummy FastAPI server in Python (main.py) with a POST endpoint '/predict' that returns mock classification scores.",
        "common_mistakes": [
            "Instantiating HttpClient manually inside using statements (`using var client = new HttpClient()`), which leads to socket exhaustion under high load.",
            "Failing to configure timeouts for external integrations, causing threads to hang indefinitely."
        ],
        "interview_questions": [
            {
                "q": "Why should you use IHttpClientFactory instead of instantiating HttpClient manually?",
                "a": "IHttpClientFactory manages the lifetime of underlying HTTP handlers, caching and reusing connections to prevent socket exhaustion while cleaning up unused handlers."
            },
            {
                "q": "How does integration between C# and Python ML models work in production?",
                "a": "ASP.NET Core acts as the secure, high-performance gateway, handling validation and authorization, and making HTTP/gRPC requests to the Python FastAPI microservice that runs the ML models."
            }
        ],
        "homework": "Implement a prediction model handler passing image path arrays, uploading multipart image files to your ML service, and returning classification scores.",
        "revision_checklist": [
            "I know how to register HttpClient using DI.",
            "I can make POST calls with JsonContent payloads.",
            "I understand microservice gateway concepts."
        ]
    },

    # --- WEEK 5 ---
    {
        "day_num": 29,
        "title": "Application Containerization using Docker",
        "objectives": [
            "Understand containerization concepts and advantages.",
            "Write multi-stage Dockerfiles for ASP.NET Core apps.",
            "Manage container environment variables."
        ],
        "theory": [
            "Containerization: Packages an application and all its dependencies into an isolated image. This guarantees it runs identically in dev, staging, and production.",
            "Multi-stage builds: Optimizes final image size. First stage uses the large SDK image to build and compile the code. Second stage copies compile output into a lightweight runtime image, keeping production images small and secure.",
            "Port binding & environments: Configure ASP.NET Core port exposures using environment variables like `ASPNETCORE_URLS=http://+:5000`."
        ],
        "coding_exercise": {
            "title": "Write Dockerfile for Web API",
            "instructions": "Create a multi-stage Dockerfile configuration file compiling your ASP.NET Core project.",
            "stub": """# Build Stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
WORKDIR /app

# Copy csproj and restore dependencies
COPY *.csproj ./
RUN dotnet restore

# Copy remaining code and publish
COPY . ./
RUN dotnet publish -c Release -o out

# Runtime Stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build-env /app/out .
ENTRYPOINT ["dotnet", "MyApi.dll"]"""
        },
        "mini_challenge": "Build and run your container image locally using CLI commands `docker build` and `docker run` mapping container port 80 to host port 5000.",
        "common_mistakes": [
            "Including source code files and build binaries in final runtime images, increasing image size and security risks.",
            "Hardcoding credentials in Dockerfiles (always load them dynamically via environment variables)."
        ],
        "interview_questions": [
            {
                "q": "Explain multi-stage builds in Docker.",
                "a": "Multi-stage builds use multiple FROM instructions. This allows building the application in an SDK container and copying only the final binaries to a lightweight runtime container, reducing image size."
            },
            {
                "q": "How does ASP.NET Core detect running inside a container?",
                "a": "It uses environment variables set in the container (e.g. DOTNET_RUNNING_IN_CONTAINER=true) to adjust routing configurations."
            }
        ],
        "homework": "Create a docker-compose file that spins up both your ASP.NET Core API and a SQL Server container, linking them together in a secure network.",
        "revision_checklist": [
            "I can write a multi-stage Dockerfile.",
            "I understand docker-compose setups.",
            "I can run docker container management commands."
        ]
    },
    {
        "day_num": 30,
        "title": "Final Review & Roadmap Capstones Launch",
        "objectives": [
            "Synthesize Phase 1-8 backend development skills.",
            "Implement production configurations (CORS, SSL, performance tuning).",
            "Launch the 5 real-world capstone projects."
        ],
        "theory": [
            "Production Readiness: Transition from local setups to secure production environments. Configure CORS policies to allow only trusted frontend origins.",
            "Database Optimizations: Ensure SQL Server connection pooling is active. Review transaction boundaries to prevent locks.",
            "AI/ML Model Deployment: Containerize Python FastAPI alongside ASP.NET Core, mapping endpoints inside internal networks."
        ],
        "coding_exercise": {
            "title": "Production Config Setup",
            "instructions": "Configure strict CORS validation rules and enable HTTPS redirection in your API startup pipeline.",
            "stub": """// Program.cs
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options => {
    options.AddPolicy("ProdPolicy", policy => {
        policy.WithOrigins("https://mytrustedfrontend.com")
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

app.UseHttpsRedirection();
app.UseCors("ProdPolicy");
app.UseAuthorization();
app.MapControllers();
app.Run();"""
        },
        "mini_challenge": "Create a deployment plan checklist detailing all environment overrides for database connection strings and security key keys.",
        "common_mistakes": [
            "Failing to restrict CORS permissions in production, allowing unauthorized cross-origin requests.",
            "Exposing debug logs and detailed error info stack traces to users."
        ],
        "interview_questions": [
            {
                "q": "What is the purpose of CORS in Web API?",
                "a": "Cross-Origin Resource Sharing (CORS) is a security mechanism that allows or restricts resource requests from external web origins, preventing unauthorized domains from calling your APIs."
            },
            {
                "q": "What are the key configuration items to check before deploying an API to production?",
                "a": "Ensure HTTPS is enforced, CORS is restricted, secure database connection strings are loaded from environment variables, detailed error pages are disabled, and structured logging is configured."
            }
        ],
        "homework": "Initialize Git repositories for all 5 Capstone Projects and prepare Docker configs for deployment.",
        "revision_checklist": [
            "I understand production security rules.",
            "I can configure CORS policies.",
            "I have mapped out the 5 Capstone projects."
        ]
    }
]

projects_data = [
    {
        "id": 1,
        "title": "Student Management System",
        "features": [
            "Student profile CRUD with enrollment status indicators.",
            "Course management catalog mapping credit values.",
            "Enrollment workflow registering students to courses via transactions.",
            "Grade entry tracking academic performance metrics."
        ],
        "folder_structure": """StudentManagement/
├── src/
│   ├── Controllers/
│   │   ├── StudentsController.cs
│   │   └── CoursesController.cs
│   ├── Models/
│   │   ├── Student.cs
│   │   └── Course.cs
│   ├── Repositories/
│   │   ├── IStudentRepository.cs
│   │   └── DapperStudentRepository.cs
│   └── Program.cs
└── Dockerfile""",
        "database_design": """-- Tables: Students, Courses, StudentCourses
-- Relationships: Many-to-Many via StudentCourses join table
-- Constraints: UNIQUE Email constraint, CHECK credits range (1-6)""",
        "api_endpoints": [
            "GET /api/students - List all students",
            "POST /api/students - Create new student profile",
            "POST /api/enroll - Register student in course (transactional)",
            "GET /api/courses - List available course catalog"
        ],
        "validation_rules": [
            "Student email must be a valid email format.",
            "First name and last name are required fields.",
            "Course credits must be between 1 and 6."
        ],
        "practice_tasks": [
            "Implement a stored procedure retrieving student GPA averages.",
            "Add generic search filters querying students by name parameters."
        ],
        "extension_challenges": [
            "Add course capacity limits. If the enrollment limit is hit, return a 409 Conflict status and rollback the transaction."
        ]
    },
    {
        "id": 2,
        "title": "Inventory Management System",
        "features": [
            "Inventory product catalog with pricing tracking.",
            "Warehouse location management tracking stock levels.",
            "Stock adjustments updating inventory counts.",
            "Supplier details tracking primary item sources."
        ],
        "folder_structure": """InventoryManagement/
├── src/
│   ├── Controllers/
│   │   ├── ProductsController.cs
│   │   └── InventoryController.cs
│   ├── Models/
│   │   ├── Product.cs
│   │   └── Warehouse.cs
│   ├── Repositories/
│   │   ├── IProductRepository.cs
│   │   └── DapperProductRepository.cs
│   └── Program.cs
└── Dockerfile""",
        "database_design": """-- Tables: Products, Warehouses, InventoryStock, Suppliers
-- Constraints: UNIQUE SKU value, CHECK stock quantity >= 0, CHECK price > 0""",
        "api_endpoints": [
            "GET /api/products - Retrieve inventory catalog",
            "POST /api/products - Add product item to SKU index",
            "POST /api/inventory/adjust - Update physical stock levels (transactional)",
            "GET /api/inventory/low-stock - List items falling below threshold limits"
        ],
        "validation_rules": [
            "SKU must follow a specific pattern (e.g. PROD-XXXX).",
            "Product price must be greater than zero.",
            "Stock adjustments must specify a valid warehouse ID."
        ],
        "practice_tasks": [
            "Write non-clustered indexes on product SKU codes.",
            "Create stored procedures tracking low-stock items."
        ],
        "extension_challenges": [
            "Implement an audit logging table that tracks every stock change, recording the user identity, old count, new count, and change timestamp."
        ]
    },
    {
        "id": 3,
        "title": "WhatsApp Message Sender API with PDF Upload",
        "features": [
            "Message sending queuing triggers simulating WhatsApp integrations.",
            "PDF media upload storing files locally or in cloud structures.",
            "SQL Server logging tracking message status states.",
            "API endpoint processing recipient payloads dynamically."
        ],
        "folder_structure": """WhatsAppSender/
├── src/
│   ├── Controllers/
│   │   └── MessagesController.cs
│   ├── Services/
│   │   ├── IWhatsAppService.cs
│   │   └── MockWhatsAppService.cs
│   ├── Repositories/
│   │   ├── IMessageLogRepository.cs
│   │   └── DapperMessageLogRepository.cs
│   └── Program.cs
└── uploads/""",
        "database_design": """-- Tables: MessageLogs, Recipients
-- Relationships: One-to-Many (Recipient to MessageLogs)
-- Constraints: CHECK status values (Queued, Sent, Failed), DEFAULT status is 'Queued'""",
        "api_endpoints": [
            "POST /api/messages/send - Dispatch message requests",
            "POST /api/messages/upload-pdf - Upload PDF documents and get URL mappings",
            "GET /api/messages/history - Query message logs"
        ],
        "validation_rules": [
            "Recipient phone number must match international formats (+92XXXXXXXXXX).",
            "Uploaded file must be a PDF and under 5MB in size.",
            "Message body text cannot exceed 1000 characters."
        ],
        "practice_tasks": [
            "Configure exception middleware to catch file upload failures cleanly.",
            "Create a Dapper script logging dispatch errors dynamically."
        ],
        "extension_challenges": [
            "Implement background tasks using C# HostedService or Hangfire to automatically process queued messages and retry failed attempts."
        ]
    },
    {
        "id": 4,
        "title": "Authentication System with JWT",
        "features": [
            "User registration hashing password credentials using BCrypt.",
            "Secure login authentication returning signed JWTs.",
            "Role authorization protecting API endpoints.",
            "Token validation checks inside middleware pipelines."
        ],
        "folder_structure": """AuthSystem/
├── src/
│   ├── Controllers/
│   │   └── AuthController.cs
│   ├── Models/
│   │   ├── User.cs
│   │   └── Role.cs
│   ├── Services/
│   │   ├── IPasswordHasher.cs
│   │   └── TokenService.cs
│   └── Program.cs
└── appsettings.json""",
        "database_design": """-- Tables: Users, Roles, UserRoles
-- Relationships: Many-to-Many via UserRoles
-- Constraints: UNIQUE Username and Email constraints""",
        "api_endpoints": [
            "POST /api/auth/register - Create secure user account",
            "POST /api/auth/login - Authenticate credentials and get JWT token",
            "GET /api/users/profile - Secure endpoint (requires authorization token)",
            "GET /api/admin/dashboard - Protected endpoint (requires Admin role)"
        ],
        "validation_rules": [
            "Passwords must contain uppercase letters, numbers, and special characters.",
            "Usernames must be unique and alphanumeric.",
            "JWT security key configs must be loaded from app configurations."
        ],
        "practice_tasks": [
            "Implement custom token policy validation rules.",
            "Create user profiles with dynamic role mapping settings."
        ],
        "extension_challenges": [
            "Implement JWT Refresh Token flow. Save refresh tokens in SQL Server with an expiration timestamp to safely renew access tokens."
        ]
    },
    {
        "id": 5,
        "title": "AI Prediction API (ASP.NET Core + FastAPI)",
        "objectives": [
            "Design ASP.NET Core gateway connecting requests to FastAPI models.",
            "Transmit image binary files to model pipelines.",
            "Retrieve and map ML model accuracy scores."
        ],
        "features": [
            "ASP.NET Core acts as API gateway validating caller details (JWT required).",
            "FastAPI serves model pipelines using PyTorch or Scikit-learn endpoints.",
            "HttpClientFactory manages microservice connections.",
            "Logging middleware records prediction latency and feature metrics."
        ],
        "folder_structure": """AIPredictionSystem/
├── gateway/ (ASP.NET Core)
│   ├── Controllers/
│   │   └── PredictionController.cs
│   ├── Program.cs
│   └── Dockerfile
├── ml_service/ (Python FastAPI)
│   ├── main.py
│   ├── model.pkl
│   └── Dockerfile
└── docker-compose.yml""",
        "database_design": """-- Tables: PredictionLogs
-- Fields: LogID, Timestamp, UserID, FeaturesSent, PredictedClass, AccuracyScore, LatencyMs""",
        "api_endpoints": [
            "POST /api/predict/classify - Gateway endpoint accepting feature values (JWT required)",
            "POST /api/predict/image - Endpoint accepting image file uploads for analysis",
            "GET /api/predict/analytics - Retrieve prediction accuracy counts"
        ],
        "validation_rules": [
            "Feature lists must match required dimensions (e.g. exactly 10 float values).",
            "Supported upload images must be PNG or JPG formats and under 3MB.",
            "Gateway requires valid Authorization header tokens."
        ],
        "practice_tasks": [
            "Build mock classification endpoints in FastAPI returning response structures.",
            "Implement HttpClient error handling in C# gateways for offline FastAPI states."
        ],
        "extension_challenges": [
            "Implement circuit-breaker patterns on HttpClient using Polly. If FastAPI experiences delays, fail-fast and return cached predictions."
        ]
    }
]

# Generate C# Exercises dynamically
csharp_exercises = []
categories_csharp = [
    ("Basic Syntax & C++ Migration", "easy"),
    ("Classes, Structs & OOP", "medium"),
    ("Collections & Generics", "medium"),
    ("Exceptions & File Handling", "medium"),
    ("LINQ Queries", "hard"),
    ("Async/Await & Tasks", "hard"),
    ("Delegates, Events & Lambdas", "hard")
]

for i in range(1, 101):
    cat, diff = categories_csharp[(i - 1) % len(categories_csharp)]
    title = f"C# Exercise {i}: "
    if i <= 15:
        title += f"Variable Scope and Pointer-to-Ref Conversion"
        desc = "Convert a C++ function taking double pointers into a C# function using the 'ref' and 'out' keywords. Output variable states before and after calls."
        stub = "static void GetValues(out int x, ref int y) { ... }"
    elif i <= 30:
        title += f"OOP Design with Interfaces and Abstract Classes"
        desc = "Create a Shape abstract class with Draw() and an IPrintable interface with Print(). Inherit them in Circle and Rectangle classes."
        stub = "public abstract class Shape { ... }\npublic interface IPrintable { ... }"
    elif i <= 50:
        title += f"Generics Collection Indexer"
        desc = "Create a custom generic list class wrapping a dynamic array, implementing an indexer property to read/write items by index values."
        stub = "public class CustomList<T> {\n    private T[] _items;\n    public T this[int index] { get => _items[index]; set => _items[index] = value; }\n}"
    elif i <= 70:
        title += f"LINQ Data Filter & Transformation"
        desc = "Given a list of transactional logs, query entries matching critical error levels. Group results by source module and sort them descending."
        stub = "var query = logs.Where(l => l.Level == \"Error\").GroupBy(l => l.Module)..."
    elif i <= 85:
        title += f"Async Task Runner with Exception Catching"
        desc = "Write a method that runs a batch of async web page tasks. Catch network timeout exceptions without blocking the main program pipeline."
        stub = "public async Task RunBatchAsync() { ... }"
    else:
        title += f"Delegate Callback Action Pipeline"
        desc = "Implement a custom task runner that accepts an Action delegate, invoking the delegate when processing finishes while logging results."
        stub = "public void ExecuteTask(Action callback) { ... }"

    csharp_exercises.append({
        "id": f"csharp-{i}",
        "category": "csharp",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# SQL Exercises
sql_exercises = []
for i in range(1, 51):
    diff = "easy" if i <= 15 else "medium" if i <= 35 else "hard"
    title = f"SQL Exercise {i}: "
    if i <= 15:
        title += "Table Creation & Constraints"
        desc = "Create a table for catalog items ensuring primary keys, unique SKU values, and price range validations."
        stub = "CREATE TABLE Items ( ... )"
    elif i <= 30:
        title += "Relational JOIN Merging"
        desc = "Write a query returning customer profiles with their order items using LEFT and INNER JOINS across order schemas."
        stub = "SELECT * FROM Customers c INNER JOIN Orders o ON c.ID = o.CustomerID ..."
    elif i <= 40:
        title += "Stored Procedure Parameter Mapping"
        desc = "Create a Stored Procedure checking inventory levels before inserting rows, returning status flags."
        stub = "CREATE PROCEDURE sp_CheckAndAddStock @ItemID INT, @Qty INT, @Status BIT OUTPUT AS ..."
    else:
        title += "ACID Transaction Rollbacks"
        desc = "Implement transactional query blocks updating multiple accounts, rolling back transactions if constraints fail."
        stub = "BEGIN TRANSACTION; BEGIN TRY ... COMMIT; END TRY BEGIN CATCH ROLLBACK; END CATCH;"
        
    sql_exercises.append({
        "id": f"sql-{i}",
        "category": "sql",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# ASP.NET Core API Exercises
aspnet_exercises = []
for i in range(1, 51):
    diff = "easy" if i <= 15 else "medium" if i <= 35 else "hard"
    title = f"API Exercise {i}: "
    if i <= 15:
        title += "Controller Route Configuration"
        desc = "Create an API controller exposing HTTP GET and POST endpoints handling path routing variables."
        stub = "[ApiController]\n[Route(\"api/[controller]\")]\npublic class TestController : ControllerBase { ... }"
    elif i <= 30:
        title += "Custom Middleware Validation"
        desc = "Build a custom middleware checking if requests contain validation keys in headers, returning 401 on failure."
        stub = "public async Task InvokeAsync(HttpContext context) { ... }"
    elif i <= 40:
        title += "DI Dependency Lifetime Checks"
        desc = "Register a scoped database context service and verify instantiation scopes inside controller constructors."
        stub = "builder.Services.AddScoped<IMyContext, MyContext>();"
    else:
        title += "Global Exception Handler Middleware"
        desc = "Configure exception handler middleware returning standard JSON formats on server errors."
        stub = "app.UseMiddleware<GlobalExceptionHandler>();"
        
    aspnet_exercises.append({
        "id": f"aspnet-{i}",
        "category": "aspnet",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# Dapper Exercises
dapper_exercises = []
for i in range(1, 31):
    diff = "easy" if i <= 10 else "medium" if i <= 20 else "hard"
    title = f"Dapper Exercise {i}: "
    if i <= 10:
        title += "Dapper Query Mapping"
        desc = "Query tables using Dapper QueryAsync mapping records directly to custom C# models."
        stub = "var items = await conn.QueryAsync<Item>(\"SELECT * FROM Items\");"
    elif i <= 20:
        title += "Parameterized Commands"
        desc = "Write parameterized INSERT commands passing dynamic inputs safely to prevent SQL injection."
        stub = "await conn.ExecuteAsync(\"INSERT INTO Items VALUES (@Name)\", new { Name = itemName });"
    else:
        title += "Repository Pattern SP Integration"
        desc = "Define repositories calling database stored procedures returning multi-mapping datasets."
        stub = "var result = await conn.QueryMultipleAsync(\"sp_GetOrderDetails\", ...);"
        
    dapper_exercises.append({
        "id": f"dapper-{i}",
        "category": "dapper",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# JWT Exercises
jwt_exercises = []
for i in range(1, 21):
    diff = "medium" if i <= 10 else "hard"
    title = f"JWT Exercise {i}: "
    if i <= 10:
        title += "Token Signature Configuration"
        desc = "Write services signing JWT claims returning valid tokens with configurations."
        stub = "var token = new JwtSecurityToken( ... );"
    else:
        title += "Role Authorization Guards"
        desc = "Secure controller class routes restricting access to validated Admin and Manager roles."
        stub = "[Authorize(Roles = \"Admin\")]"
        
    jwt_exercises.append({
        "id": f"jwt-{i}",
        "category": "jwt",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# API Integration Exercises
integration_exercises = []
for i in range(1, 21):
    diff = "medium" if i <= 10 else "hard"
    title = f"Integration Exercise {i}: "
    if i <= 10:
        title += "HttpClient API Call"
        desc = "Use IHttpClientFactory to query weather or external API endpoints mapping JSON responses."
        stub = "var client = _clientFactory.CreateClient();\nvar res = await client.GetAsync(...);"
    else:
        title += "FastAPI Image prediction dispatch"
        desc = "Configure multipart uploads forwarding image files to model endpoints on Python servers."
        stub = "var content = new MultipartFormDataContent();\ncontent.Add(new StreamContent(...));"
        
    integration_exercises.append({
        "id": f"integration-{i}",
        "category": "integration",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# Deployment Exercises
deployment_exercises = []
for i in range(1, 11):
    diff = "medium" if i <= 5 else "hard"
    title = f"Deployment Exercise {i}: "
    if i <= 5:
        title += "Multi-stage Dockerfile Design"
        desc = "Write a multi-stage Dockerfile for an ASP.NET Core project optimizing image outputs."
        stub = "FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build ..."
    else:
        title += "Docker Compose Environment Links"
        desc = "Build docker-compose configurations grouping web API gateways with SQL database containers."
        stub = "services:\n  api:\n    environment:\n      - ConnectionStrings__Default=..."
        
    deployment_exercises.append({
        "id": f"deployment-{i}",
        "category": "deployment",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# Debugging Exercises
debugging_exercises = []
for i in range(1, 21):
    diff = "medium" if i <= 10 else "hard"
    title = f"Debugging Exercise {i}: "
    if i <= 10:
        title += "NullReference Exception inside Collections"
        desc = "Fix database context calls that throw NullReferenceExceptions when loading empty reference models."
        stub = "// Error: var name = student.Class.Name; // Class is null!\n// Fix: Include reference load or add null checks."
    else:
        title += "Captive Dependency Life-cycle mismatch"
        desc = "Debug service registration errors thrown when scoped DBContexts are injected into singleton cache services."
        stub = "// Error: InvalidOperationException: Cannot consume scoped service from singleton."
        
    debugging_exercises.append({
        "id": f"debugging-{i}",
        "category": "debugging",
        "difficulty": diff,
        "title": title,
        "description": desc,
        "stub": stub
    })

# Combine all exercises
exercises_data = (csharp_exercises + sql_exercises + aspnet_exercises + dapper_exercises +
                  jwt_exercises + integration_exercises + deployment_exercises + debugging_exercises)

# Interview QA
qa_data = []
for i in range(1, 51):
    q_str = ""
    a_str = ""
    if i <= 10:
        q_str = f"Q{i}: What is the main difference between C++ memory management and C# Garbage Collection?"
        a_str = "C++ relies on deterministic memory allocation where developers allocate heap memory and release it manually (using delete or smart pointers). C# uses a Garbage Collector (GC) which runs asynchronously on a separate thread, sweep-analyzing heap allocations and deallocating memory automatically. This reduces leaks but introduces brief GC pauses."
    elif i <= 20:
        q_str = f"Q{i}: How do Indexes improve read performance in SQL Server, and what are their drawbacks?"
        a_str = "Indexes allow SQL Server to find rows quickly without performing full table scans. However, they increase disk storage size requirements and slow down data modification operations (INSERT, UPDATE, DELETE) because every index structure must be rebuilt when data changes."
    elif i <= 30:
        q_str = f"Q{i}: Explain Dependency Injection lifetimes in ASP.NET Core: Transient, Scoped, and Singleton."
        a_str = "Transient services are created every time they are requested. Scoped services are created once per client request (HTTP request lifetime). Singleton services are created once on startup and shared across all request pipelines. Choosing lifetimes correctly is vital to avoid thread safety bugs and captive dependencies."
    elif i <= 40:
        q_str = f"Q{i}: Why is Dapper preferred over Entity Framework Core for high-performance reporting APIs?"
        a_str = "Dapper is a Micro-ORM that directly extends IDbConnection and maps raw SQL results to C# models without the overhead of query translation, change-tracking, or model entity setups. It executes queries at speeds close to ADO.NET while writing clean code mappings."
    else:
        q_str = f"Q{i}: How does a JWT Token work in stateless API Authentication?"
        a_str = "A JSON Web Token (JWT) is signed by the server using secret keys. When client calls request access, they pass the token in authorization headers. The server verifies token integrity and reads claims (UserID, Roles) directly from the payload without checking data tables, enabling high scalability."

    qa_data.append({
        "id": i,
        "q": q_str,
        "a": a_str
    })

print(f"Total compiled days: {len(days_data)}")
print(f"Total compiled projects: {len(projects_data)}")
print(f"Total compiled exercises: {len(exercises_data)}")
print(f"Total compiled QA items: {len(qa_data)}")

# Serializing data into JS variables to embed in HTML template
js_data = f"""
    daysData = {json.dumps(days_data)};
    projectsData = {json.dumps(projects_data)};
    exercisesData = {json.dumps(exercises_data)};
    qaData = {json.dumps(qa_data)};
"""

# Place the JS data into the script section
final_html = html_template.replace(
    "// Placeholder data to be loaded dynamically",
    js_data
)

# Add code to dynamically render all elements
rendering_js = """
    // Render Days
    function renderDays() {
        const container = document.getElementById('days-container');
        container.innerHTML = '';
        
        daysData.forEach(day => {
            const dayHtml = `
                <div class="accordion-header" onclick="toggleAccordion(this)">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span class="badge">Day ${day.day_num}</span>
                        <strong>${day.title}</strong>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1.5rem;" onclick="event.stopPropagation();">
                        <label class="checkbox-container">
                            <input type="checkbox" id="chk-day-${day.day_num}" class="track-checkbox" onchange="toggleTrackItem('chk-day-${day.day_num}')">
                            Mark Read
                        </label>
                        <span>▼</span>
                    </div>
                </div>
                <div class="accordion-content">
                    <div class="day-subsection">
                        <h4>🎯 Learning Objectives</h4>
                        <ul class="nested-list">
                            ${day.objectives.map(o => `<li>${o}</li>`).join('')}
                        </ul>
                    </div>
                    
                    <div class="day-subsection">
                        <h4>📘 Theory Topics</h4>
                        <ul class="nested-list">
                            ${day.theory.map(t => `<li>${t}</li>`).join('')}
                        </ul>
                    </div>

                    <div class="day-subsection">
                        <h4>💻 Coding Exercise: ${day.coding_exercise.title}</h4>
                        <p style="margin-bottom: 0.5rem;">${day.coding_exercise.instructions}</p>
                        <pre><code>${escapeHtml(day.coding_exercise.stub)}</code></pre>
                    </div>

                    <div class="day-subsection">
                        <h4>⭐ Mini Challenge</h4>
                        <p>${day.mini_challenge}</p>
                    </div>

                    <div class="grid-2">
                        <div class="day-subsection" style="border-left-color: var(--hard-color);">
                            <h4 style="color: var(--hard-color);">⚠️ Common Mistakes</h4>
                            <ul class="nested-list">
                                ${day.common_mistakes.map(m => `<li>${m}</li>`).join('')}
                            </ul>
                        </div>
                        <div class="day-subsection" style="border-left-color: var(--easy-color);">
                            <h4 style="color: var(--easy-color);">🎓 Sample Interview Questions</h4>
                            <ul class="nested-list">
                                ${day.interview_questions.map(iq => `<li><strong>Q:</strong> ${iq.q}<br><strong>A:</strong> ${iq.a}</li>`).join('')}
                            </ul>
                        </div>
                    </div>

                    <div class="day-subsection" style="margin-top: 1rem;">
                        <h4>🏠 Homework & Practice</h4>
                        <p>${day.homework}</p>
                    </div>

                    <div class="day-subsection" style="border-left-color: var(--accent-secondary);">
                        <h4 style="color: var(--accent-secondary);">✅ Revision Checklist</h4>
                        <ul class="nested-list" style="list-style-type: none;">
                            ${day.revision_checklist.map((rc, rIdx) => `
                                <li>
                                    <label class="checkbox-container">
                                        <input type="checkbox" id="chk-day-${day.day_num}-rev-${rIdx}" class="track-checkbox" onchange="toggleTrackItem('chk-day-${day.day_num}-rev-${rIdx}')">
                                        ${rc}
                                    </label>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>
            `;
            container.innerHTML += dayHtml;
        });
    }

    // Render Projects
    function renderProjects() {
        const container = document.getElementById('projects-container');
        container.innerHTML = '';
        
        projectsData.forEach(p => {
            const html = `
                <div class="card">
                    <h3 style="color: #818cf8; font-size: 1.5rem; margin-bottom: 1rem;">Project ${p.id}: ${p.title}</h3>
                    
                    <div style="margin-bottom: 1rem;">
                        <strong>🔑 Key Features:</strong>
                        <ul style="margin-left: 1.5rem;">
                            ${p.features.map(f => `<li>${f}</li>`).join('')}
                        </ul>
                    </div>

                    <div style="margin-bottom: 1rem;">
                        <strong>📂 Folder Structure:</strong>
                        <pre><code>${p.folder_structure}</code></pre>
                    </div>

                    <div style="margin-bottom: 1rem;">
                        <strong>🛢️ Database Design:</strong>
                        <p>${p.database_design}</p>
                    </div>

                    <div style="margin-bottom: 1rem;">
                        <strong>🌐 API Endpoints:</strong>
                        <ul style="margin-left: 1.5rem;">
                            ${p.api_endpoints.map(ep => `<li><code>${ep}</code></li>`).join('')}
                        </ul>
                    </div>

                    <div style="margin-bottom: 1rem;">
                        <strong>🛡️ Validation Rules:</strong>
                        <ul style="margin-left: 1.5rem;">
                            ${p.validation_rules.map(vr => `<li>${vr}</li>`).join('')}
                        </ul>
                    </div>

                    <div class="grid-2" style="margin-top: 1rem;">
                        <div style="border-left: 3px solid var(--accent-secondary); padding-left: 1rem;">
                            <h4 style="color: var(--accent-secondary);">✍️ Practice Tasks</h4>
                            <ul style="margin-left: 1rem;">
                                ${p.practice_tasks.map(pt => `<li>${pt}</li>`).join('')}
                            </ul>
                        </div>
                        <div style="border-left: 3px solid var(--medium-color); padding-left: 1rem;">
                            <h4 style="color: var(--medium-color);">🚀 Extension Challenge</h4>
                            <ul style="margin-left: 1rem;">
                                ${p.extension_challenges.map(ec => `<li>${ec}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += html;
        });
    }

    // Render Exercises
    function renderExercises() {
        const container = document.getElementById('exercises-container');
        container.innerHTML = '';
        
        exercisesData.forEach(ex => {
            const html = `
                <div class="card exercise-card" data-category="${ex.category}" data-title="${ex.title.toLowerCase()}" data-desc="${ex.description.toLowerCase()}">
                    <div class="flex-row">
                        <h4 style="color: #f3f4f6;">${ex.title}</h4>
                        <span class="tag ${ex.difficulty}">${ex.difficulty}</span>
                    </div>
                    <p style="color: var(--text-muted); margin-bottom: 1rem;">${ex.description}</p>
                    <pre><code>${escapeHtml(ex.stub)}</code></pre>
                    <div class="flex-row" style="margin-top: 0.5rem; justify-content: flex-end;">
                        <label class="checkbox-container">
                            <input type="checkbox" id="chk-ex-${ex.id}" class="track-checkbox" onchange="toggleTrackItem('chk-ex-${ex.id}')">
                            Mark Complete
                        </label>
                    </div>
                </div>
            `;
            container.innerHTML += html;
        });
    }

    // Filter Exercises Category
    let currentCategory = 'all';
    function filterExerciseCategory(cat) {
        currentCategory = cat;
        // Update active class on buttons
        const buttons = document.querySelectorAll('#practice-bank button');
        buttons.forEach(btn => {
            if (btn.innerText.toLowerCase().includes(cat.toLowerCase()) || (cat === 'all' && btn.innerText === 'All')) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        filterExercises();
    }

    // Search Exercises
    function filterExercises() {
        const query = document.getElementById('exercise-search').value.toLowerCase();
        document.querySelectorAll('.exercise-card').forEach(card => {
            const cat = card.getAttribute('data-category');
            const title = card.getAttribute('data-title');
            const desc = card.getAttribute('data-desc');
            
            const matchesCat = (currentCategory === 'all' || cat === currentCategory);
            const matchesQuery = (title.includes(query) || desc.includes(query));
            
            if (matchesCat && matchesQuery) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Render Q&A
    function renderQA() {
        const container = document.getElementById('qa-container');
        container.innerHTML = '';
        
        qaData.forEach(item => {
            const html = `
                <div class="card qa-card" data-q="${item.q.toLowerCase()}" data-a="${item.a.toLowerCase()}">
                    <h3 style="color: #f59e0b; margin-bottom: 0.5rem;">${item.q}</h3>
                    <p style="color: var(--text-main); font-size: 0.95rem;">${item.a}</p>
                </div>
            `;
            container.innerHTML += html;
        });
    }

    // Filter Q&A Search
    function filterQA() {
        const query = document.getElementById('qa-search').value.toLowerCase();
        document.querySelectorAll('.qa-card').forEach(card => {
            const q = card.getAttribute('data-q');
            const a = card.getAttribute('data-a');
            
            if (q.includes(query) || a.includes(query)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Helpers
    function escapeHtml(text) {
        return text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    // Initial load sequences
    window.onload = function() {
        renderDays();
        renderProjects();
        renderExercises();
        renderQA();
        loadTrackState();
    };
"""

# Let's write the rendering logic in the JS section of HTML
final_html = final_html.replace(
    "// Initial load sequences",
    rendering_js
)

# Output into file
workspace_dir = "F:\\dotnet projects\\Practice\\roadmap"
output_file = os.path.join(workspace_dir, "index.html")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Roadmap HTML successfully written to: " + output_file)
print("Done!")
