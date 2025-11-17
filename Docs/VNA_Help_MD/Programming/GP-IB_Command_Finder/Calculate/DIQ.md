# Calculate:DIQ:XAXis Commands

* * *

Allows you to set the DIQ channel X-Axis domain and source.

![](../../../assets/images/DIQSelectXaxis.gif) |  [CALC:DIQ:XAXis](DIQ.md#XAXis)  
---|---  
[CALC:DIQ:XAXis:DOMain?](DIQ.md#domain)  
[CALC:DIQ:XAXis:SOURce?](DIQ.md#source)  
  
Click to view the command details.

See Also

  * [Sense:DIQ commands](../Sense/DIQ.md)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Differential IQ Application](../../../Applications/Differential_IQ.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<ch>:DIQ:XAXis <domain>,<source>

Applicable Models: N522xB, N524xB (Write-only) Sets the information to display
on the X-axis of the selected DIQ measurement. This command does not change
the default setting for new traces.  
---  
Parameters |   
<ch> |  The Differential IQ channel number. If unspecified, value is set to 1.  
<domain> |  Character - Domain to display on the X-axis. Choose from: FREQuency \- display the primary frequency range. POWer \- display the power sweep range PHASe \- display the phase sweep range DCValue \- display the DC sweep range POINts \- display the data points in the range  
<source> |  String - Specific source for the selected domain. Choose from the following: |  For this X-Axis Domain: |  Choose one of these X-Axis Sources  
---|---  
Frequency |  Frequency Range (F1, F2, etc.)  
Power |  Source port (Port 1, Port 2, etc.)  
Phase |  Source port (Port 1, Port 2, etc.)  
DC Value |  DC Source (AO1, AO2, etc.)  
Points |  Points (N/A)  
Examples |  CALC:DIQ:XAX FREQ,"F2" calculate:diq:xaxis power,"Port 1"  
Query Syntax |  Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  FREQ,"F1"  
  
* * *

## CALCulate<ch>:DIQ:XAXis:DOMain?

Applicable Models: N522xB, N524xB (Read-only) Returns the X-Axis domain of the
selected measurement.  
---  
Parameters |   
<ch> |  The Differential IQ channel number. If unspecified, value is set to 1.  
Example |  CALC:DIQ:XAX:DOM? 'Possible returned values: FREQuency \- display the primary frequency range. POWer - display the power sweep range PHASe \- display the phase sweep range DCValue - display the DC sweep range POINts - display the data points in the range  
Return Type |  Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  FREQuency  
  
* * *

## CALCulate<ch>:DIQ:XAXis:SOURce?

Applicable Models: N522xB, N524xB (Read-only) Returns the X-Axis source of the
selected measurement.  
---  
Parameters |   
<ch> |  The Differential IQ channel number. If unspecified, value is set to 1.  
Example |  CALC:DIQ:XAX:SOURce? See [CALC:DIQ:XAX](DIQ.md#XAXis) for possible returned values.  
Return Type |  String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "F1"  
  
* * *

