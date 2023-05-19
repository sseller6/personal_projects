using System;
using System.Collections.Generic;
namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool passed = true;

            while (passed)
            {
            List<int> numbers = new List<int>();
            Console.Write("What number would you like to add to the list? ");
            string userAsk = Console.ReadLine();
            int userNumber = int.Parse(userAsk);

            numbers.Add(userNumber);

            for (int i = 0; i < numbers.Count; i++)
            {
                Console.WriteLine(numbers[i]);
            }

            if (userNumber == 0)
            {
                passed = false;
            }
            
            int sum = 0;
            foreach (int number in numbers)
            {
                sum += number;
            }
            //Compute the Sum
            Console.WriteLine($"The sum is: {sum}");
            }


            // List<int> numbers = new List<int>();

            // //Adding Items To A List
            // List<string> words = new List<string>();
            // words.Add("phone");
            // words.Add("keyboard");
            // words.Add("mouse");

            // //Get List Size
            // Console.WriteLine(words.Count);

            // //How to Iterate Through a List
            // foreach (string word in words)
            // {
            // Console.WriteLine(word);
            // }

            // //Accessing items by their Index
            // for (int i = 0; i < words.Count; i++)
            // {
            //     Console.WriteLine(words[i]);
            // }
            
        }
    }
}