##### [Intro to Examples](COM_Example_Intro.md)

# Getting Trace Data from the Analyzer

* * *

This Visual Basic program:

  * Retrieves Scalar Data from the Analyzer and plots it.

  * Retrieves Paired Data from the Analyzer and plots it.

  * Retrieves Complex Data from the Analyzer and plots it.

To use this code, prepare a form with the following:

  * Two MSCharts named MSChart1 and MSChart2

  * Three buttons named GetScalar, GetPaired, GetComplex

Note: You can get MSChart in Visual Basic by clicking Project / Components /
Microsoft Chart Control

* * *

'Put this in a module  
Public dlocation As NADataStore  
Public numpts As Long  
Public fmt As NADataFormat  
Public app As Application  
Public measData As IArrayTransfer  
Public chan As Channel

Sub Form_Load()  
'Change analyzerName to your analyzer's full computer name  
Set app = CreateObject("AgilentPNA835x.Application", "analyzerName")  

Set measData = app.ActiveMeasurement  
Set chan = app.ActiveChannel  
  
'To pick a location to get the data from remove the comment from one of these  
dlocation = naRawData  
'dlocation = naCorrectedData  
'dlocation = naMeasResult  
'dlocation = naRawMemory  
'dlocation = naMemoryResult  
  
'setup MSChart1 and MSChart2  
'right click on the chart and select:  
' \- line chart  
' \- series in rows  
End Sub  
  

Sub GetComplex_Click()  
ReDim Data(numpts) As NAComplex  
Dim Real(201) AS Single  
Dim Imag(201) AS Single  
numpts = chan.NumberOfPoints

'You cannot change the format of Complex Data  
Call trigger  
'get data  
measData.GetNAComplex dlocation, numpts, Data(0)  
'plot data  
Dim i As Integer  
  
For i = 0 To numpts - 1  
Real(i) = Data(i).Re  
Imag(i) = Data(i).Im  
Next i  
MSChart1 = Real()  
MSChart2.Visible = True  
MSChart2 = Imag()  
Call Sweep  
End Sub  
  

Sub GetPaired_Click()  
ReDim Real(numpts) As Single  
ReDim Imag(numpts) As Single  
numpts = chan.NumberOfPoints

' To pick a format, remove the comment from one of these  
fmt = naLogMagPhase  
'fmt = naLinMagPhase  
Call trigger  
'Get data  
measData.getPairedData dlocation, fmt, numpts, Real(0), Imag(0)  
'Plot Scalar  
MSChart1 = Real()  
MSChart2.Visible = True  
MSChart2 = Imag()  
Call Sweep  
End Sub  
  

Sub GetScalar_Click()  
ReDim Data(numpts) As Single

numpts = chan.NumberOfPoints  
'To pick a format remove the comment from one of these  
fmt = naDataFormat_LogMag  
'fmt = naDataFormat_LinMag  
'fmt = naDataFormat_Phase  
'fmt = naDataFormat_Delay  
'fmt = naDataFormat_Real  
'fmt = naDataFormat_Imaginary  
Call trigger  
'Get data  
measData.GetScalar dlocation, fmt, numpts, Data(0)  
'Plot Data  
MSChart1 = Data()  
MSChart2.Visible = False  
Call Sweep  
End Sub

  
Sub trigger()

'The analyzer sends continuous trigger signals  
app.TriggerSignal = naTriggerInternal  
'The channel will only accept one, then go into hold  
'Sync true will wait for the sweep to complete

sync=True

chan.Single sync  
End Sub

  
Sub Sweep()  
'The channel goes back to accepting all triggers  
chan.Continuous  
End Sub  

