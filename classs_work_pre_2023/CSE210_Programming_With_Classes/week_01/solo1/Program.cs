using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine("Hello World!");
            // Console.WriteLine("This is in C#!");

            // int number = 5;
            // number = 8;
            // number = number +3;

            // string color = "blue";

            // Console.WriteLine("What is your favorite color? ");
            // string user_color = Console.ReadLine();
            // Console.WriteLine($"Your favorite color is {user_color}, and mine is {color}");

            //Beginning of first assignment.

            Console.WriteLine("What is your first name? ");
            string first_name = Console.ReadLine();
            Console.WriteLine("What is your last name? ");
            string last_name = Console.ReadLine();
            Console.WriteLine($"Your name is {last_name}, {first_name} {last_name}");
        }
    }
}