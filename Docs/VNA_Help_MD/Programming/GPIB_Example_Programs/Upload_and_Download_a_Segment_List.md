# Upload and Download a Segment List

* * *

This VBScript program creates two segments, then uploads the segment data to
the VNA.

The second part [downloads the segment list from the
VNA](Upload_and_Download_a_Segment_List.htm#Download).

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unguided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

[See all Segment SCPI commands.](../GP-IB_Command_Finder/Sense/Segment.md)

### Create and Upload a Segment List

Option Explicit Dim app Set app = CreateObject("AgilentPNA835x.Application") '
Preset the VNA app.Preset Dim scpi Set scpi = app.ScpiStringParser ' In case
of a measurement receiver VNA like N5264B ' which has no source ports,
"SOURce:CATalog?" will ' return an empty list (just a pair of quotation marks)
Dim srcPortNames srcPortNames = Split( scpi.Execute("SOURce:CATalog?"), ",")
Dim numberOfSrcPorts If Left( srcPortNames(0), 2 ) = Chr(34) & Chr(34) Then
numberOfSrcPorts = 0 Else numberOfSrcPorts = UBound(srcPortNames) + 1 End If '
Building up a string consisting of the sweep segment data ' we want to set up.
This example will create two segments. Dim segData ' Set state of first
segment to be ON (1 = ON, 0 = OFF), ' 101 points, start freq of 10 MHz, stop
freq of 1 GHz segData = "1,101,10E6,1E9" ' If you want to include one or more
of: IFbandwidth, Dwell Time ' or Port Power, remove the comments from these
next two lines 'TurnOnOptions 1 'Call the subroutine 'segData =
AddOptionalSettings(segData, numberOfSrcPorts) ' Set state of second segment
to be ON, 201 points, ' start freq of 1 GHz, stop freq of 3 GHz segData =
segData & ",1,201,1E9,3E9" ' Uncomment this line below only if you uncommented
the ' AddOptionalSettings line above for the first segment. 'segData =
AddOptionalSettings(segData, numberOfSrcPorts) Const numSegs = 2 ' Upload our
segment list to the channel scpi.Execute "SENSe1:SEGMent:LIST SSTOP," &
numSegs & "," & segData ' Set segment sweep type on Channel 1 scpi.Execute
"SENSe1:SWEep:TYPE SEGment" ' Having the VNA display the segment sweep table
for the channel scpi.Execute "DISPlay:WINDow1:TABLe SEGMent" Sub
TurnOnOptions(ByVal chan) scpi.Execute "SENSe"&chan&":SEGMent:BWIDth:CONTrol
ON" scpi.Execute "SENSe"&chan&":SEGMent:SWEep:TIME:CONTrol ON" scpi.Execute
"SENSe"&chan&":SEGMent:POWer:CONTrol ON" ' Turning off coupling allows power
to vary per each port scpi.Execute "SOURce"&chan&":POWer:COUPle OFF" End Sub
Function AddOptionalSettings(ByVal inStr, ByVal numSrcPorts) ' Specifying 1
kHz IF bandwidth and Dwell Time of 0 inStr = inStr & ",1E3,0" ' -10 dBm power
for each of the source ports Dim i For i = 0 To numSrcPorts - 1 inStr = inStr
& ",-10" Next AddOptionalSettings = inStr End Function  
---  
  
### Download a Segment List

This example assumes that the active trace is in Window 1

Option Explicit Dim app Set app = CreateObject("AgilentPNA835x.Application")
Dim scpi Set scpi = app.ScpiStringParser ' Set the display-active channel's
sweep type to segment sweep ' (if the VNA's currently active measurement
window doesn't ' contain any traces, this querying for active channel will '
result in a SCPI error which scpi.Parse will trap and throw) Dim chan chan =
CLng( scpi.Parse("SYSTem:ACTive:CHANnel?") ) scpi.Execute
"SENSe"&chan&":SWEep:TYPE SEGment" ' Having the VNA display the segment sweep
table for the channel scpi.Execute "DISPlay:WINDow1:TABLe SEGMent" ' Get the
total number of segments Dim numSegs numSegs = CLng(
scpi.Execute("SENSe"&chan&":SEGMent:COUNt?") ) ' Read the segment listing Dim
segDataStr segDataStr = scpi.Execute("SENSe"&chan&":SEGMent:LIST?") Dim
segData segData = Split(segDataStr, ",") ' Get upper bound of the array of
data values ' (lower bound of array resulting from VB 'Split' function is 0)
Dim segArrayUB segArrayUB = UBound(segData) Dim numDataElementsPerSeg
numDataElementsPerSeg = (segArrayUB + 1) / numSegs WScript.Echo "Number of
segments = " & numSegs WScript.Echo "Number of data values per segment = " &
numDataElementsPerSeg Dim segInfStr segInfStr = "Segment 1: state = " &
CBool(segData(0)) segInfStr = segInfStr & ", num points = " & CLng(segData(1))
segInfStr = segInfStr & ", start freq = " & CDbl(segData(2)) segInfStr =
segInfStr & ", stop freq = " & CDbl(segData(3)) segInfStr = segInfStr & ",
IFBW = " & CDbl(segData(4)) segInfStr = segInfStr & ", dwell time = " &
CDbl(segData(5)) ' In case of a measurement receiver VNA like N5264B ' which
has no source ports, "SOURce:CATalog?" will ' return an empty list Dim
srcPortNames srcPortNames = Split( scpi.Execute("SOURce"&chan&":CATalog?"),
",") Dim srcPortNamesUB srcPortNamesUB = UBound(srcPortNames) ' First source
port name will be preceded by a quotation mark ' and the last name will be
followed by one of those, so stripping ' those off now. srcPortNames(0) =
Right( srcPortNames(0), Len(srcPortNames(0)) - 1 )
srcPortNames(srcPortNamesUB) = Left( srcPortNames(srcPortNamesUB),
InStrRev(srcPortNames(srcPortNamesUB), Chr(34)) - 1 ) Dim firstPortIndex
firstPortIndex = 6 Dim lastPortIndex lastPortIndex = numDataElementsPerSeg - 1
Dim j For j = firstPortIndex To lastPortIndex segInfStr = segInfStr & ", " &
srcPortNames(j - firstPortIndex) & " power = " & CDbl(segData(j)) Next
WScript.Echo segInfStr  
---  
  
## Example in Excel VBA with VISA-COM

Sub SampleSegmentSetup()  
'*** The variables of the resource manager and the instrument I/O are
declared.  
Dim ioMgr As VisaComLib.ResourceManager  
Dim GPIB As VisaComLib.FormattedIO488  
'  
' *** The memory area of the resource manager and the instrument I/O are
acquired.  
Set ioMgr = New VisaComLib.ResourceManager  
Set GPIB = New VisaComLib.FormattedIO488  
'*** Open the instrument.  
Set GPIB.IO = ioMgr.Open("GPIB0::16::INSTR")  
GPIB.IO.timeout = 10000  
  
Dim Buf As String * 100  
Dim srcPortNames As Variant  
Dim numberOfSrcPorts As Integer  
Dim segData As Variant  
Const numSegs = 2  
Const Chan = 1  
Const addIFBW_PWR = 0  
' In case of a measurement receiver VNA like N5264A  
' which has no source ports, "SOURce:CATalog?" will  
' return an empty list (just a pair of quotation marks)  
GPIB.WriteString "SOURce:CATalog?", True  
Buf = GPIB.ReadString  
srcPortNames = Split(Buf, ",")  
If Left(srcPortNames(0), 2) = Chr(34) & Chr(34) Then  
numberOfSrcPorts = 0  
Else  
numberOfSrcPorts = UBound(srcPortNames) + 1  
End If  
' Building up a string consisting of the sweep segment data  
' we want to set up. This example will create two segments.  
' Set state of first segment to be ON (1 = ON, 0 = OFF),  
' 101 points, start freq of 10 MHz, stop freq of 1 GHz  
segData = "1,101,10E6,1E9"  
' If you want to include one or more of: IFbandwidth, Dwell Time  
' or Port Power, set Const addIFBW_PWR = 1  
  
If addIFBW_PWR = 1 Then  
GPIB.WriteString "SENSe" & Chan & ":SEGMent:BWIDth:CONTrol ON"  
GPIB.WriteString "SENSe" & Chan & ":SEGMent:SWEep:TIME:CONTrol ON"  
GPIB.WriteString "SENSe" & Chan & ":SEGMent:POWer:CONTrol ON"  
' Turning off coupling allows power to vary per each port  
GPIB.WriteString "SOURce" & Chan & ":POWer:COUPle OFF"  
segData = AddOptionalSettings(segData, numberOfSrcPorts)  
End If  
  
' Set state of second segment to be ON, 201 points,  
' start freq of 1 GHz, stop freq of 3 GHz  
  
segData = segData & ",1,201,1E9,3E9"  
  
' Uncomment this line below only if you uncommented the  
' AddOptionalSettings line above for the first segment.  
'segData = AddOptionalSettings(segData, numberOfSrcPorts)  
' Upload our segment list to the channel  
GPIB.WriteString "SENSe1:SEGMent:LIST SSTOP," & numSegs & "," & segData  
' Set segment sweep type on Channel 1  
GPIB.WriteString "SENSe1:SWEep:TYPE SEGment"  
' Having the PNA display the segment sweep table for the channel  
GPIB.WriteString "DISPlay:WINDow1:TABLe SEGMent"  
  
'*** End procedure  
GPIB.IO.Close  
End Sub  
Function AddOptionalSettings(ByVal pStr As String, ByVal numSrcPorts As
Integer) As String  
Dim i  
  
' Specifying 1 kHz IF bandwidth and Dwell Time of 0  
pStr = pStr & ", 1E3, 0"  
' -10 dBm power for each of the source ports  
For i = 0 To numSrcPorts - 1  
pStr = pStr & ",-10"  
Next  
AddOptionalSettings = pStr  
End Function

* * *

