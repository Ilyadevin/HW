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
            int Mp = 0;
            if (number == 1)
            {
                Console.WriteLine("Число должно быть больше 1");
            }
            if (number == i)
            {
                Mp = 2 * number - 1;
                Console.WriteLine($"Число Мерсенна - {number} ==> {Mp}");
            }
            if (number > 1)
            {
                for (int q = 2; q < 47; q++)
                    if (number % q == 0)
                    {
                        Console.WriteLine($"Число {number} - сложное");
                    }
                    else
                        Mp = 2 * number - 1;
                        Console.WriteLine($"Число Мерсенна - {number} ==> {Mp}");
                    number += 1;
            }
        }
    }
}
