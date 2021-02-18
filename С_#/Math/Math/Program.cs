using System;

class A { }
class B { }
class C { }
class Program
{
    
    static void Main()
    {
        int Mp = 0;
        Console.WriteLine("Параметр а:");
        int A = Convert.ToInt32(Console.ReadLine()); 
        Console.WriteLine("Параметр b:");
        int B = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Параметр c:");
        int C = Convert.ToInt32(Console.ReadLine());
        double result = Math.Sqrt(Math.Pow(A,2) + Math.Pow(B,2) - (2 * A * B*Math.Cos(C)));
        Console.WriteLine($"Результат выполнения первой задачи - {result}");
        if (A > 1 || A % A == 0 || A % 1 == A)
            Mp = (2 * A) - 1;
            Console.WriteLine($"Число Мерсенна ==> { Mp}");
    }
}


