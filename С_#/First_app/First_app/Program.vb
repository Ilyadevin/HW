Imports System

Module Program
    Dim Mp As Integer
    Sub Main()
        Console.Write("������� �����: ")
        Dim p = Convert.ToInt32(Console.ReadLine())
        If p / p Or p / 1 Then
            Mp = 2 * p - 1
            Console.WriteLine($"����� �������� - {Mp}")
        Else
            Console.WriteLine($"��������� ����� �� �������")
        End If
    End Sub
End Module
