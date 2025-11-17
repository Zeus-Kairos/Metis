# Power Range Example

The following VB Script example exercises the COM commands used to set up the
Power Range feature to access data sheet specified and typical max and min
power levels (in dBm). Max power refers to the maximum leveled source power.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as RxLevel.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

### See Also

[About Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)

[Power Range Object](../COM_Reference/Objects/Power_Range_Object.md)

[See other COM Examples](COM_Example_Intro.md)

## Example #1

Set Application = CreateObject("AgilentPNA835x.Application", "A-N5242A-90065")
Set PowerRange = application.Capabilities.PowerRange powerRange.Reset
powerRange.PortNumber = 1 powerRange.PathElement("Src2Out1LowBand").Value =
"HiPwr" powerRange.RangeStartFrequency = 1e9 powerRange.RangeStopFrequency =
10e9 maxPower = powerRange.RangeGetMaxPower minPower =
powerRange.RangeGetMinPower MsgBox("Max power: " & maxPower & " dBm" & Chr(10)
&_ "Min power: " & minPower & " dBm" ) End Function  
---  
  
## Example #2

Set Application = CreateObject("AgilentPNA835x.Application", "A-N5242A-90065")
Set PowerRange = application.Capabilities.PowerRange powerRange.Reset
powerRange.PortNumber = 3 powerRange.PathElement("Src2Out1LowBand").Value =
"HiPwr" powerRange.DiscreteFrequencies = Array(1e9,2e9,3e9,4e9) maxPower =
powerRange.DiscreteGetMaxPowerArray minPower =
powerRange.DiscreteGetMinPowerArray MsgBox( "Frequency: " &
ArrayToString(powerRange.DiscreteFrequencies) & " Hz" & _ Chr(10) & "Max
power: " & ArrayToString(maxPower) & " dBm" & Chr(10) &_ "Min power: " &
ArrayToString(minPower) & " dBm" ) Function ArrayToString(Arr) ArrayToString =
"[" If IsArray(Arr) Then ArrayToString = ArrayToString & CStr(Arr(0)) For i =
1 to ubound(Arr) ArrayToString = ArrayToString & "," & CStr(Arr(i)) Next End
If ArrayToString = ArrayToString & "]" End Function  
---

