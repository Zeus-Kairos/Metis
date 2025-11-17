# Calculate:Mixer Command

This command is Superseded by the
[CALCulate:MEASure:MIXer:XAXis](Measure.md#CALCulate:MEASure:MIXer:XAXis)
command.

* * *

CALCulate<ch>:MIXer:XAXis <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets or
returns the swept parameter to display on the X-axis for the selected
[FCA](../../../FreqOffset/FCA_Use.md#Xaxis) and GCX measurement. Critical
Note: CALCulate commands act on the selected measurement. You can select one
measurement for each channel using [Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<char> | Parameter to display on the X-axis. Choose from: INPUT \- Input frequency span OUTPUT \- Output frequency span LO_1 \- First LO frequency span LO_2 \- Second LO frequency span  
Examples | CALC:MIX:XAX INPUT  
calc2:mixer:xaxis output See an example that creates, selects, and calibrates
an [SMC](../../GPIB_Example_Programs/Create_and_Cal_an_SMC_Measurement.md)
and [VMC](../../GPIB_Example_Programs/Create_and_Cal_a_VMC_Measurement.md)
measurement using SCPI.  
Query Syntax | CALCulate<ch>:MIXer:XAXis?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OUTPUT  
  
* * *

