using System;

class A { }
class B { }
class C { }
class Program
{
    static void Main()
    {
        Console.WriteLine("Параметр а:");
        int A = Convert.ToInt32(Console.ReadLine()); 
        Console.WriteLine("Параметр b:");
        int B = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Параметр c:");
        int C = Convert.ToInt32(Console.ReadLine());
        double result = Math.Sqrt(Math.Pow(A,2) + Math.Pow(B,2) - (2 * A * B*Math.Cos(C)));
        Console.WriteLine(result);
    }
}


