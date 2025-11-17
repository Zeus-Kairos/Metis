# Getting and Putting Data using SCPI

* * *

This Visual Basic Program does the following:

  * Reads data from the analyzer

  * Puts the data back into memory

  * To see the data on the analyzer after running the program, from the front panel click:  
Trace - Math/Memory - Memory Trace

To run this program, you need:

  * An established [GPIB interface connection](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

##### [ See Other SCPI Example Programs](SCPI_Example_Programs.md)

Note: To change the read and write location of data, removing the comment from
the beginning of ONE of the lines, and replace the comment in the beginning of
the SDATA and SMEM lines.

* * *

Private Sub ReadWrite_Click()  
Dim i As Integer  
Dim t As Integer  
Dim q As Integer  
Dim dat As String  
Dim cmd As String  
Dim datum() As Double  
  
GPIB.Configure  
GPIB.Write "SYSTem:PRESet;*wai"  
  
'Select the measurement  
GPIB.Write "CALCulate:PARameter:SELect 'CH1_S11_1'"  
  
'Read the number of data points  
GPIB.Write "SENSe1:SWEep:POIN?"  
numpts = GPIB.Read  
  
'Turn continuous sweep off  
GPIB.Write "INITiate:CONTinuous OFF"  
  
'Take a sweep  
GPIB.Write "INITiate:IMMediate;*wai"  
  
'Ask for the Data  
  
'PICK ONE OF THESE LOCATIONS TO READ  
'GPIB.Write "CALCulate:DATA? FDATA" 'Formatted Meas  
'GPIB.Write "CALCulate:DATA? FMEM" 'Formatted Memory  
GPIB.Write "CALCulate:DATA? SDATA" 'Corrected, Complex Meas  
'GPIB.Write "CALCulate:DATA? SMEM" 'Corrected, Complex Memory  
'GPIB.Write "CALCulate:DATA? SCORR1" 'Error-Term Directivity  
  
'Number of values returned per data point  
'q = 1 ' Pick this if reading FDATA or FMEM  
q = 2 ' Otherwise pick this  
  
'Parse the data  
ReDim datum(q, numpts)  
For i = 0 To numpts - 1  
For t = 0 To q - 1  
'Read the Data  
dat = GPIB.Read(20)  
'Parse it into an array  
datum(t, i) = Val(dat)  
Next t  
Next i  
  
'PUT THE DATA BACK IN  
GPIB.Write "format ascii"  
  
'PICK ONE OF THESE LOCATIONS TO PUT THE DATA  
'cmd = "CALCulate:DATA FDATA," 'Formatted Meas  
'cmd = "CALCulate:DATA FMEM," 'Formatted Memory  
'cmd = "CALCulate:DATA SDATA," 'Corrected, Complex Meas  
cmd = "CALCulate:DATA SMEM," 'Corrected, Complex Memory  
'cmd = "CALCulate:DATA SCORR1," 'Error-Term Directivity  
  
For i = 0 To numpts - 1  
For t = 0 To q - 1  
If i = numpts - 1 And t = q - 1 Then  
cmd = cmd & Format(datum(t, i))  
Else  
cmd = cmd & Format(datum(t, i)) & ","  
End If  
Next t  
Next i  
  
GPIB.Write cmd  
End Sub

* * *

This Excel VBA Program with VISA-COM does the following:

  * Reads data from the analyzer

  * Puts the data back into memory

Note: To change the read and write location of data, removing the comment from
the beginning of ONE of the lines, and replace the comment in the beginning of
the FDATA lines.

Sub SampleGetPutData()  
'*** The variables of the resource manager and the instrument I/O are
declared.  
Dim ioMgr As VisaComLib.ResourceManager  
Dim GPIB As VisaComLib.FormattedIO488  
'*** The memory area of the resource manager and the instrument I/O are
acquired.  
Set ioMgr = New VisaComLib.ResourceManager  
Set GPIB = New VisaComLib.FormattedIO488  
'*** Open the instrument.  
Set GPIB.IO = ioMgr.Open("GPIB0::16::INSTR")  
GPIB.IO.timeout = 10000  
  
Dim Numpts As Long  
Dim Datam As Variant  
  
'Select the measurement  
GPIB.WriteString "CALCulate1:MEASure1:PARameter 'S21'", True  
'Read the number of data points  
GPIB.WriteString "SENSe1:SWEep:POINts?", True  
Numpts = GPIB.ReadNumber  
'Turn continuous sweep off  
GPIB.WriteString "INITiate:CONTinuous OFF", True  
'Take a sweep  
GPIB.WriteString "INITiate1:IMMediate;*WAI", True  
'Ask for the Data  
'PICK ONE OF THESE LOCATIONS TO READ  
GPIB.WriteString "CALCulate1:MEASure1:DATA:FDATA?", True ' Formatted Meas  
'GPIB.WriteString "CALCulate1:MEASure1:DATA:FMEM?", True ' Formatted Memory  
'GPIB.WriteString "CALCulate1:MEASure1:DATA:SDATA?", True ' Corrected, Complex
Meas  
'GPIB.WriteString "CALCulate1:MEASure1:DATA:SMEM?", True ' Corrected, Complex
Memory  
'GPIB.WriteString "SENSe1:CORRection:CSET:ETERm:DATA? 'Directivity(1,1)'",
True ' Error-Term Directivity  
  
'Parse the data  
Datam = GPIB.ReadList(ASCIIType_R8, ",")  
  
'PUT THE DATA BACK IN  
GPIB.WriteString "CALCulate1:MEASure1:DATA:FDATA ", False ' Formatted Meas  
'GPIB.WriteString "CALCulate1:MEASure1:DATA:FMEM ", False ' Formatted Memory  
'GPIB.WriteString "CALCulate1:MEASure1:DATA:SDATA ", False ' Corrected,
Complex Meas  
'GPIB.WriteString "CALCulate1:MEASure1:DATA:SMEM ", False ' Corrected, Complex
Memory  
'GPIB.WriteString "SENSe1:CORRection:CSET:ETERm:DATA 'Directivity(1,1)',",
False ' Error-Term Directivity  
  
GPIB.WriteList Datam, ASCIIType_R8, ",", True  
  
'*** End procedure  
GPIB.IO.Close  
End Sub  

* * *

