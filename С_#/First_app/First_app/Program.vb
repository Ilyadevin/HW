Imports System

Module Program
    Dim Mp As Integer
    Sub Main()
        Console.Write("Введите число: ")
        Dim p = Convert.ToInt32(Console.ReadLine())
        If p / p Or p / 1 Then
            Mp = 2 * p - 1
            Console.WriteLine($"Число Мерсенна - {Mp}")
        Else
            Console.WriteLine($"Введенное число не простое")
        End If
    End Sub
End Module
