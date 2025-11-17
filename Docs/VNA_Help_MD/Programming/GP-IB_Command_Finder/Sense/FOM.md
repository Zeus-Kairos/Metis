# Sense:FOM (Frequency Offset) Commands

* * *

Controls the frequency offset settings which cause stimulus and response
frequencies to be different.

Note: These commands replace the [previous FOM commands](Offset_SCPI.md).
Although the old commands will continue to work, they can NOT be mixed with
these new commands.

![](../../../assets/images/Programming/senseFOM.gif)

Click on a red keyword to view the command details.

See Also

  * [FOM Example Program](../../GPIB_Example_Programs/Create_an_FOM_Measurement.md)

  * [Learn about Frequency Offset](../../../FreqOffset/Frequency_Offset_Mode.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:FOM[:STATe] <bool>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Turns Frequency Offset ON and OFF. Frequency offset settings are
not enabled until this setting is ON. Send this command (FOM ON) AFTER sending
other FOM settings to avoid 'out-or-range' errors.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<bool> | ON (or 1) - turns FOM ON. OFF (or 0) - turns FOM OFF.  
Examples | SENS:FOM 1  
sense2:fom:state on  
Query Syntax | SENSe<cnum>:FOM:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<cnum>:FOM:CATalog?

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-only) Returns a comma-separated list of available range names in the
VNA. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names.
Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers.
Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific
name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a
specific number. External devices can appear in the list of range names.
[Learn more.](../../../System/Configure_an_External_Device.md)  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
Examples | SENS:FOM:CAT? 'returns "Primary, Source, Receivers"  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:FOM:COUNt?

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-only) Returns the number of valid range numbers in the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
Examples | SENS:FOM:COUN?  
sense2:fom:count?  
Query Syntax | SENSe<cnum>:FOM:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:FOM:DISPlay:SELect <string>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Select the range to be displayed on the VNA x-axis. All traces in
the channel have this same x-axis scaling.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<string> | Range name. Case insensitive. Use [SENSe:FOM:CAT?](FOM.md#cat) to see a list of available frequency range names.  
Examples | SENS:FOM:DISPlay:SELect "source2"  
sense2:fom:display:select "source"  
Query Syntax | SENSe<cnum>:FOM:DISPlay:SELect?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Receivers  
  
* * *

## SENSe<cnum>:FOM:RNUM? <string>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-only) Returns the number of a specified range name. The FOM range items
are typically numbered as follows:

  1. Primary
  2. Source
  3. Receivers
  4. Source2 (if present)
  5. Source3 (if present)

Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use
[SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use
[SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific
number. External devices can appear in the list of range names. [Learn
more.](../../../System/Configure_an_External_Device.htm)  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<string> | Range name for which a number is being queried. Case insensitive.  
Examples | SENS:FOM:RNUM? "receivers"  
sense2:fom:rnum? "Source2"  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:COUPled <bool>

Applicable Models:All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the state of coupling (ON or OFF) of the
specified range to the primary range.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number to couple to primary range. An error is returned when attempting to couple to the Primary range (1). Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<bool> | ON (or 1) - Couple range to primary range. OFF (or 0) - Do NOT couple to primary range.  
Examples | SENS:FOM:RANG:COUP 1  
sense2:fom:range2:coupled 0  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:COUPled?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON (or 1) Coupled  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:FREQuency:CW <num>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the CW frequency. This setting is valid for the
primary range, or if the specified range is already
[uncoupled](FOM.md#coupled) from the primary range and if the [sweep
type](FOM.htm#SwpType) is CW.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<num> | CW frequency value in Hz. Choose any frequency within the range of the VNA.  
Examples | SENS:FOM:RANG:FREQ:CW 1e9  
sense2:fom:range2:frequency:cw 10000000  
Query Syntax | SENSe<cnum>:FOM:RANGe:<n>:FREQuency:CW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Center frequency of the VNA.  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:FREQuency:DIVisor <num>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the divisor value. This setting is valid only if
the specified range is [coupled](FOM.md#coupled) to the primary range.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<num> | Divisor value (unitless).  
Examples | SENS:FOM:RANG:FREQ:DIV 3  
sense2:fom:range2:frequency:divisor 0  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:FREQuency:DIVisor?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:FREQuency:MULTiplier <num>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the multiplier value to be used when coupling
this range to the primary range. This setting is valid only if the specified
range is [coupled](FOM.md#coupled) to the primary range.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<num> | Multiplier value. (Unitless)  
Examples | SENS:FOM:RANG:FREQ:MULT 1  
sense2:fom:range2:frequency:multiplier 2  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:FREQuency:MULTiplier?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:FREQuency:OFFSet <num>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the offset value to be used when coupling this
range to the primary range. [Learn more about offset
value.](../../../FreqOffset/Frequency_Offset_Mode.htm#FreqOffsDiag) This
setting is valid only if the specified range is [coupled](FOM.md#coupled) to
the primary range.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<num> | Offset value. (Unitless)  
Examples | SENS:FOM:RANG:FREQ:OFFS 1E9  
sense2:fom:range2:frequency:offset 10000000  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:FREQuency:OFFSet?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:FREQuency:STARt <num>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the Start value of frequency range. Also specify
[Stop frequency.](FOM.md#FStop) This setting is valid for the primary range,
or if the specified range is already [uncoupled](FOM.md#coupled) from the
primary range and if the [sweep type](FOM.md#SwpType) is LOG or LINear.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<num> | Start value in Hz. Choose any frequency within the range of the VNA.  
Examples | SENS:FOM:RANG:FREQ:STAR 1GHz  
sense2:fom:range2:frequency:start 100000000  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Minimum frequency of the VNA.  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:FREQuency:STOP <num>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the Stop value of frequency range. Also specify
[Start frequency.](FOM.md#FStart) This setting is valid for the primary
range, or if the specified range is already [uncoupled](FOM.md#coupled) from
the primary range and if the [sweep type](FOM.md#SwpType) is LOG or LINear.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<num> | Stop value in Hz. Choose any frequency within the range of the VNA.  
Examples | SENS:FOM:RANG:FREQ:STOP 1e12  
sense2:fom:range2:frequency:stop 10000000000  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum frequency of the VNA.  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:NAME?

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-only) Returns the name of range<n>. The FOM range items are typically
named as follows:

  1. Primary
  2. Source
  3. Receivers
  4. Source2 (if present)
  5. Source3 (if present)

Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use
[SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use
[SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1.  
Examples | SENS:FOM:RANG:NAME?  
sense2:fom:range2:name?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:FOM:RANGe<n>:SWEep:TYPE <char>

Applicable Models: All with FOM Options (S9x080A/B, S9x082A/B, S9x083A/B)
(Read-Write) Sets and returns the sweep type to be used with the specified
range. This setting is valid only if the specified range is already
[uncoupled](FOM.md#coupled) from the primary range. Learn about [Unsupported
Sweep Type
combinations.](../../../FreqOffset/Frequency_Offset_Mode.htm#SweepType)  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<n> | Range number. If unspecified, value is set to 1. Use [SENS:FOM:CAT?](FOM.md#cat) to see a list of available range names. Use [SENS:FOM:COUNt?](FOM.md#count) to see a list of available range numbers. Use [SENS:FOM:RNUM?](FOM.md#rnum) to see the range number for a specific name. Use [SENS:FOM:RANG:NAME?](FOM.md#NameQuery) to see the range name for a specific number.  
<char> | Sweep type. Choose from: CW \- Also specify [CW frequency.](FOM.md#FCW) LINear \- Also specify frequency Start/Stop or Center/Span LOG \- Also specify frequency Start/Stop or Center/Span PHASe \- See all [Phase sweep](../SourcePhase.md) settings. POWer \- Also specify power Start/Stop or Center/Span SEGMent \- Also specify [segment sweep](FOMSegm.md) settings.  
Examples | SENS:FOM:RANG:SWE:TYPE LOG  
sense2:fom:range2:sweep:type linear:  
Query Syntax | SENSe<cnum>:FOM:RANGe<n>:SWEep:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Linear  
  
* * *

