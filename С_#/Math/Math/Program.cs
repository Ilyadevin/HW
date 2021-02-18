using System;


    class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Параметр а - ");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Параметр b - ");
        int b = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Параметр c - ");
        int c = Convert.ToInt32(Console.ReadLine());
        double result = Math.Sqrt((a * a) + (b * b) - (2 * a * b*Math.Cos(c)));
        Console.WriteLine(result);
    } 
}

