Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        ' Data source.
        Dim numbers() As Integer = {0, 1, 2, 3, 4, 5, 6}

        ' Query creation.
        Dim evensQuery = From num In numbers
                         Where num Mod 2 = 0
                         Select num

        ' Query execution.
        For Each number In evensQuery
            MsgBox(number & " ")
            Console.Write(number & " ")
        Next
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim refInteger As Object = 2
        MsgBox("TypeOf Object[Integer] Is Integer? " & TypeOf refInteger Is Integer)
        MsgBox("TypeOf Object[Integer] Is Double? " & TypeOf refInteger Is Double)
        Dim refForm As Object = New System.Windows.Forms.Form
        MsgBox("TypeOf Object[Form] Is Form? " & TypeOf refForm Is System.Windows.Forms.Form)
        MsgBox("TypeOf Object[Form] Is Label? " & TypeOf refForm Is System.Windows.Forms.Label)
        MsgBox("TypeOf Object[Form] Is Control? " & TypeOf refForm Is System.Windows.Forms.Control)
        MsgBox("TypeOf Object[Form] Is IComponent? " & TypeOf refForm Is System.ComponentModel.IComponent)
    End Sub
End Class
