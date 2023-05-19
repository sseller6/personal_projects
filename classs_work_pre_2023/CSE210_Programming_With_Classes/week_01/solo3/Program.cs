using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Console.Write("What is the magic number? ");
            // string userNumberChoice = Console.ReadLine();

            Random randomGenerator = new Random();

            int magic_number = randomGenerator.Next(1,10);

            int userGuessNumber = 0;

            while (userGuessNumber != magic_number)
            {
            Console.Write("What is your guess? ");
            string userGuess = Console.ReadLine();
            userGuessNumber = int.Parse(userGuess);

            if (userGuessNumber > magic_number)
            {
                Console.WriteLine("Your guess is higher. ");
            }

            else if (userGuessNumber < magic_number)
            {
                Console.WriteLine("Your guess is lower. ");
            }

            else if (userGuessNumber == magic_number)
            {
                Console.WriteLine("You guessed it! ");
            }

            else
            {
                Console.WriteLine("Your guess was not formatted correctly. ");
            }

            }
            /* Solo Practice */

            // string input ="yes";

            // while (input == "yes")
            // {
            //     Console.Write("Do you want to continue? ");
            //     input = Console.ReadLine();
            // }

            // do
            // {
            //     Console.Write("Do you want to continue? ");
            //     input = Console.ReadLine();
            // } while (input == "yes");

            // // This for loops counts from 0 to 9.
            // for (int i = 0; i < 10; i++)
            // /* The first part initializes the value, the second is the condition to check, 
            // and the third is the increment step taht is run at the end of each loop. */
            // // the ++ operator increments the value in the variable by one.
            // {
            //     Console.WriteLine(i);
            // }

            // for (int i = 2; i <=20; i = i + 2)
            // /* Same as previous for loop except it counts by twos.*/
            // {
            //     Console.WriteLine(i);
            // }

            // foreach (string color in colors)
            // {
            //     Console.WriteLine(color);
            // }

            // Random randomGenerator = new Random();
            // int number = randomGenerator.Next(1,11);

        }
    }
}