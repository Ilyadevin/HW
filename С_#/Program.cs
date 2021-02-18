using System;

namespace First_app_1
{
    class Program
    {
        private static void Main()
        {
            Console.Write("Введите число: ");
            int number = Convert.ToInt32(Console.ReadLine());
            int i = 2;
            for (int q = 0; q < 10; q++)
                if (number % i == 0)
                {
                    int Mp = 2 * number - 1;
                    Console.WriteLine($"Число Мерсенна - {Mp}");
                    number += 1;
                }
                else
                {
                    Console.WriteLine($"Число {number} не простое");
                    number += 1;
                }
        }
    }
}
