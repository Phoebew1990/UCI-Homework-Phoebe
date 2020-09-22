Sub Repeat():
Dim Year As Worksheet
Application.ScreenUpdating = False
For Each Year In Worksheets
Year.Select
Call Stock
Next
Application.ScreenUpdating = True
End Sub


Sub Stock():
'set header
Range("J1").Value = "Ticker"
Range("K1").Value = "Yearly Change"
Range("L1").Value = "Percent Change"
Range("M1").Value = "Total Stock Volumn"
Range("P2").Value = "Greatest % Increase"
Range("P3").Value = "Greatest % Decrease"
Range("P4").Value = "Greatest Total Volume"
Range("Q1").Value = "Ticker"
Range("R1").Value = "Value"



Dim Tickername As String
Dim lastrow As Long
Dim TickerRow As Long
Dim YearlyChange As Double
Dim OpenPrice As Double
Dim ClosePrice As Double
Dim PercentChange As Double
Dim Volumn As Double
Dim ColumnRow As Long
Dim GreatestIncrease As Double
Dim GreatestDecrease As Double
Dim GreatestVolumn As Double


'populate ticker column
TickerRow = 1
Volumn = 0
lastrow = Cells(Rows.Count, "A").End(xlUp).Row
OpenPrice = Cells(2, 3).Value



For i = 2 To lastrow
If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
Tickername = Cells(i, 1).Value
TickerRow = TickerRow + 1

Range("J" & TickerRow).Value = Tickername



'Yearly Change

ClosePrice = Cells(i, 6).Value

YearlyChange = ClosePrice - OpenPrice

Range("K" & TickerRow).Value = YearlyChange

  If (YearlyChange > 0) Then
  Range("K" & TickerRow).Interior.ColorIndex = 4
  ElseIf YearlyChange <= 0 Then
  Range("K" & TickerRow).Interior.ColorIndex = 3
  End If

'Percent Change
    If OpenPrice <> 0 Then
    PercentChange = (YearlyChange / OpenPrice)
   Range("L" & TickerRow).Value = PercentChange
   End If
   OpenPrice = Cells(i + 1, 3).Value
' Total volumn

Volumn = Volumn + Cells(i, 7).Value

Range("M" & TickerRow).Value = Volumn
Volumn = 0
Else
Volumn = Volumn + Cells(i, 7).Value

   
End If

'Set color Cells

Next i

'Challenges
GreatestIncrease = Cells(2, 12)
GreatestDecrease = Cells(2, 12)
GreatestVolumn = Cells(2, 13).Value
For j = 2 To lastrow


If Cells(j, 12).Value > GreatestIncrease Then
GreatestIncrease = Cells(j, 12).Value
Range("Q2").Value = Cells(j, 10).Value
Range("R2").Value = GreatestIncrease
End If



If Cells(j, 12).Value < GreatestDecrease Then
GreatestDecrease = Cells(j, 12).Value
Range("Q3").Value = Cells(j, 10).Value
Range("R3").Value = GreatestDecrease
End If


If Cells(j, 13).Value > GreatestVolumn Then
GreatestVolumn = Cells(j, 13).Value
Range("Q4").Value = Cells(j, 10).Value
Range("R4").Value = GreatestVolumn
End If



Next j





End Sub



