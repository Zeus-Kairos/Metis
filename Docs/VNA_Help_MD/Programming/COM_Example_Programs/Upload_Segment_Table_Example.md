# Upload and Download Segment Table

* * *

These example programs use the
[SetAllSegments_Method](../COM_Reference/Methods/SetAllSegments_Method.md)
and [GetAllSegments
Method](../COM_Reference/Methods/GetAllSegments_Method.htm) to do the
following:

  * Creates a 2-dimensional array (7 x 10) 7 data elements that define each segment x 10 segments

  * Uploads the data to the VNA

  * [Downloads a segment table](Upload_Segment_Table_Example.md#Download) from the VNA

This program does not make sweep type = segment or show the segment table.

The comments indicate the order in which the segment elements are specified:
Index 0 - segment state, Index 4 is IFBW, and so forth.

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as *.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

' Create the application instance, and preset the application  
Set app = CreateObject("AgilentPNA835x.Application")  
app.Preset  
  
Dim chan  
Set chan = app.ActiveChannel  
chan.sweeptype = 4  
  
Dim segs  
Set segs = chan.Segments  
  
Dim win  
Set win = app.NAWindows(1)  
win.ShowTable 2  
  
  
' Multipliers  
kHz = 1000  
MHz = kHz*1000  
GHz = MHz*1000  
' Create segments from 10MHz to 3GHz  
StartFreq = 10 * MHz  
StopFreq = 3 * GHz  
'*  
'* Create 10 segments between StartFreq and StopFreq  
'*  
' Create a 2-D array of segments.  
' 1st dimension is size 7 (6 is max index)  
' to hold all the data per segment.  
' 2nd dimension is size 10 (9 is max index)  
' to hold 10 total segments.  
Dim segdata(6, 9)  
' Width of frequency segment, used below  
SegmentWidth = (StopFreq-StartFreq)/10  
' Fill up all 10 segments (indicies 0 to 9) with data  
For i = 0 To 9  
' element 0=segment state (on or off)  
segdata(0, i) = True  
  
' element 1=Num Points in this segment  
segdata(1, i) = 500  
  
' element 2=Start Freq  
segdata(2, i) = StartFreq + i * SegmentWidth  
  
' element 3=Stop Freq  
segdata(3, i) = segdata(2, i) + SegmentWidth  
  
' element 4=IFBW  
segdata(4, i) = 35000  
  
' element 5=Dwell Time  
segdata(5, i) = 0  
  
' element 1=Power  
segdata(6, i) = 0  
  
Next  
  
' Configure Independent segment settings  
segs.IFBandwidthOption = 1  
segs.SourcePowerOption = 1  
  
' Push the segment data into the VNA's Active Channel  
segs.SetAllSegments segdata  
---  
  
### Download Segment Table

Option Explicit Dim app Set app = CreateObject("AgilentPNA835x.Application")
Dim chan Set chan = app.ActiveChannel chan.sweeptype = 4 Dim segs Set segs =
chan.Segments Dim win Set win = app.NAWindows(1) win.ShowTable 2 Dim segData
segData = segs.GetAllSegments ' Get lower bound and upper bound on the data
values per each segment Dim segDataLB, segDataUB segDataLB = LBound(segData,1)
segDataUB = UBound(segData,1) ' Get lower bound and upper bound corresponding
to how many segments Dim segArrayLB, segArrayUB segArrayLB = LBound(segData,2)
segArrayUB = UBound(segData,2) ' If the VB LBound and UBound functions didn't
generate an error ' before reaching this point, that implies a valid two-
dimensional ' array was returned into 'segData'. WScript.Echo "Number of
segments = " & segArrayUB - segArrayLB + 1 WScript.Echo "Number of data values
per segment = " & segDataUB - segDataLB + 1 Dim index index = segDataLB Dim
segInfStr segInfStr = "Segment 1: state = " & segData(index, segArrayLB) index
= index + 1 segInfStr = segInfStr & ", num points = " & segData(index,
segArrayLB) index = index + 1 segInfStr = segInfStr & ", start freq = " &
segData(index, segArrayLB) index = index + 1 segInfStr = segInfStr & ", stop
freq = " & segData(index, segArrayLB) index = index + 1 segInfStr = segInfStr
& ", IFBW = " & segData(index, segArrayLB) index = index + 1 segInfStr =
segInfStr & ", dwell time = " & segData(index, segArrayLB) ' In case of a
measurement receiver VNA like N5264B ' which has no source ports,
chan.SourcePortNames will ' return an empty variant (no array) Dim
srcPortNames srcPortNames = chan.SourcePortNames Dim srcPortNamesLB,
srcPortNamesUB srcPortNamesUB = -1 On Error Resume Next srcPortNamesLB =
LBound(srcPortNames) srcPortNamesUB = UBound(srcPortNames) On Error GoTo 0 If
(srcPortNamesUB >= 0) And ((srcPortNamesUB - srcPortNamesLB + 1) <> (segDataUB
- index)) Then WScript.Echo "Mismatch in number of source port names!" End If
Dim j For j = index + 1 To segDataUB segInfStr = segInfStr & ", " &
srcPortNames(j - (index + 1) + srcPortNamesLB) & " power = " & segData(j,
segArrayLB) Next WScript.Echo segInfStr  
---  
  
* * *

