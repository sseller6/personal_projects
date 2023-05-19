using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* Assignment
            Portion*/

            string letter = "";
            
            Console.Write("What is your grade percentage? ");
            string userGradePercentage = Console.ReadLine();

            int x = int.Parse(userGradePercentage);

            Console.WriteLine($"Your grade percentage is: % {userGradePercentage}.");

            if (x >= 90)
            {
                letter = "A";
                Console.WriteLine($"Your letter grade for this course is an {letter}.");
            }
            else if (x >= 80)
            {
                letter = "B";                
                Console.WriteLine($"Your letter grade for this course is a {letter}.");
            }
            else if (x >= 70)
            {
                letter = "C";
                Console.WriteLine($"Your letter grade for this course is a {letter}.");
            }
            else if (x >= 60)
            {
                letter = "D";
                Console.WriteLine($"Your letter grade for this course is a {letter}.");
            }
            else if (x < 60)
            {
                letter = "F";
                Console.WriteLine($"Your letter grade for this course is a {letter}.");
            }
            else{
                Console.WriteLine($"Please re-enter your grade percentage.");
            }

            if (x >= 70)
            {
                Console.WriteLine("Congrats! You passed the course.");
            }
            else
            {
                Console.WriteLine("Sorry, you did not pass the course.");
            }
            /* Guided
            Portion */

            // Console.Write("Enter Number for X: ");
            // string valueFromUser = Console.ReadLine();

            // Console.Write("Enter Number for Y: ");
            // string secondValueFromUser = Console.ReadLine();
            
            // int x = int.Parse(valueFromUser);
            // int y = int.Parse(secondValueFromUser);

            // if (x > y)
            // {
            //     Console.WriteLine("Greater");
            // }
            // else if (x < y)
            // {
            //     Console.WriteLine("Less");
            // }
            // else
            // {
            //     Console.WriteLine("Not Greater");
            // }


            /* Individual Practice*/


            // if (x > y)
            // {
            //     Console.WriteLine("greater than y");
            // }
            // else if (x > z)
            // {
            //     Console.WriteLine("greater than z");
            // }
            // else 
            // {
            //     Console.WriteLine("less than both");
            // }

            // if (name =="John")
            // {
            //     Console.WriteLine("The name is John");
            // }
            // if (Color != favorite_color)
            // {
            //     Console.WriteLine("That color is not my favorite");
            // }
            // and is && or is || not is !
            
        }
    }
}

// Throw this into the console at the start of each project. "dotnet new console --framework net6.0"