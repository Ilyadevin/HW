Imports System

Module Program
    Sub Main()
        Console.Write("¬ведите число: ")
        Dim p = Convert.ToInt32(Console.ReadLine())
        If p + 15 < 100 Then
            Console.WriteLine(p - 1)
        ElseIf (p + 15 > 100) Then
            Console.WriteLine("p - больше 100")
            Dim i = 0
            While i < p
                i += 1
                If i = 36 Then
                    Console.WriteLine($"i = {i}")
                    Console.WriteLine($"P^2 = {p * p}")
                End If
            End While
        End If
    End Sub
End Module
