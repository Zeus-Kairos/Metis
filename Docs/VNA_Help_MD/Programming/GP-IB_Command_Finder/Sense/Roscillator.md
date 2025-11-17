# Sense:Roscillator Command

* * *

SENSe:ROSCillator: | [CONTrol:AUTO](Roscillator.md#SENSe:ROSCillator:CONT:AUTO) | [EXTernal:FREQuency](Roscillator.md#SENSe:ROSCillator:EXTernal:FREQuency) | [OUTPut:FREQuency](Roscillator.md#SENSe:ROSCillator:OUTPut:FREQuency) | [SOURce](Roscillator.md#SENSe:ROSCillator:SOURce) | [CATalog?](Roscillator.md#catalog) | [CONDition?](Roscillator.md#condition)  
---  
  
[Learn about the Reference Osc.](../../../S2_Opt/Stable.md#ExtFreq)

[See the rear-panel 10 MHz connector.](../../../Rear_Panel/XRtour.md#10M)

* * *

## SENSe:ROSCillator:CONTrol:AUTO <bool>

Applicable Models: N522xB, N524xB (Read-Write) Enables selecting between
locking to an external reference without the ability to change the reference
frequency, or select internal or external reference with the ability to change
the reference frequency.  
---  
Parameters |   
<bool> | ON (or 1) This is the default behavior which locks to an external reference without the ability to change the reference frequency. OFF (or 0) Leaves the reference in its current state and all changes to the reference behavior must be made through the SCPI commands in this topic or by using the [Reference](../../../S1_Settings/Reference.md#Reference_dialog_help) dialog.  
Examples | SENS:ROSC:CONT:AUTO 1 sense:roscillator:control:auto ON  
Query Syntax | SENSe:ROSCillator:CONTrol:AUTO?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe:ROSCillator:EXTernal:FREQuency

Applicable Models: M980xA, P50xxA/B, P93xxB,, N522xB, N524xB (Read-Write) Set
and read Reference Oscillator frequency at the reference input connector. 100
MHz reference is typical for M980xA, P50xxA/B, and P93xxB.  
---  
Parameters |   
<num> | 1E+7 or 1E+8 1E+7: accepts 10 MHZ reference 2E+7: accepts 20 MHz reference (N522xB, N524xB only, synthesizer 7.0 and greater) 8E+7: accepts 80 MHz reference (N522xB, N524xB only, synthesizer 7.0 and greater) 1E+8: accepts 100 MHz reference  
Examples | SENS:ROSC:CONT:AUTO OFF SENS:ROSC:EXT:FREQ 2E7 SENS:ROSC:SOUR EXT  
Query Syntax | SENS:ROSC:EXT:FREQ?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1E+7  
  
* * *

## SENSe:ROSCillator:OUTPut:FREQuency

Applicable Models: M980xxA, P50xxA/B, P93xxB, N522xB, N524xB (Read-Write) Set
and read Reference Oscillator frequency outputted from the reference output
connector. 100 MHz reference is typical for M980xA, P50xxA, and P93xxB.  
---  
Parameters |   
<num> | 1E+7 or 1E+8  1E+7: outputs 10 MHz reference. 1E+8: outputs 100 MHz reference   
Examples | SENS:ROSC:OUTP:FREQ 1E8 sense:roscillator:output:frequency 1E8  
Query Syntax | SENS:ROSC:EXT:FREQ?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1E+7  
  
* * *

## SENSe:ROSCillator:SOURce <state>

Applicable Models: M937xA, P93xxA/B, M98xxA, P50xxA/B, N522xB, N524xB (Read-
Write) Set and read the Reference Oscillator state.  Note: The state can only
be set on instruments with Synthesizer Version 7.0 and greater. Instruments
with Synthesizer Version 6.0 and earlier can only be queried. Use the
[SYSTem:CONFigure:REVision:PNA:SYNThesizer:VERSion?](../System.md#SYSTem:CONFigure:REVision:PNA:SYNthesizer:VERSion)
command to find the Synthesizer Version. Using the GUI, click on Help -> About
NA... to find the Synthesizer Version. Note: This setting is NOT cleared with
Preset. However, it does clear when the M937xA software is restarted. Note:
Using the signal from PXI Chassis backplane degrades the measurement
performance especially absolute measurement. This is due to worse phase noise
on the reference signal from backplane.  
---  
Parameters |   
<state> | Choose from the following: The [SENSe:ROSCillator:SOURce:CATalog?](Roscillator.md#catalog) returns the available reference oscillators  INTernal - Use the internal Reference Oscillator. EXTernal - Use an external Reference Oscillator. Use [SENSe:ROSCillator:SOURce:CONDition?](Roscillator.md#condition) to determine if the analyzer is locked to the external oscillator. PXIBackplane - Use an an external Reference Oscillator via PXI Chassis backplane (PXI only)   
Examples | SENS:ROSC:SOUR INT sense:roscillator:source external  
Query Syntax | Not applicable  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | INTernal  
  
* * *

## SENSe:ROSCillator:SOURce:CATalog?

Applicable Models: All (Read-only) Reads the list of available reference
oscillator.  INTernal - Internal Reference Oscillator. EXTernal \- External
Reference Oscillator.  PXIBackplane - External Reference Oscillator via PXI
Chassis backplane (PXI only)  
---  
Examples | SENS:ROSC:SOUR:CAT? sense:roscillator:source:catalog?  
Return Type | Character, available oscillators list with comma separated chars  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe:ROSCillator:SOURce:CONDition?

Applicable Models: M937xA, P93xxB, M98xxA, P50xxA/B, N522xB, N524xB  (Read-
only) Reads the Reference Oscillator 'locked' condition.  When SENS:ROSC:SOUR
is set to Internal, this command will always return "LOCKed". When
SENS:ROSC:SOUR is set to External, then this function takes about 100 usec to
read the state of the hardware.  
---  
Examples | SENS:ROSC:SOUR:COND?  
sense:roscillator:source:condition?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

