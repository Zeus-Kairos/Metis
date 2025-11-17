# Sense:Frequency Commands

* * *

Sets the sweep frequencies of the analyzer.

SENSe:FREQuency | [CENTer](Frequency.md#cent) | STEP | [AUTO](Frequency.md#STEPAUTO) | [SIZE](Frequency.md#StepSize) | [CW | FIXed](Frequency.md#cw) | [SPAN](Frequency.md#span) | [FULL](Frequency.md#SpanFull) | [STARt](Frequency.md#start) | [STOP](Frequency.md#stop)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example](../../GPIB_Example_Programs/Setup_Sweep_Parameters_using_GPIB.md) using some of these commands.

  * [Learn about Frequency Sweep](../../../S1_Settings/Sweep.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

  * See [CALCulate:MEASure:X:VALues](../Calculate/MeasureX.md#CALCulate:MEASure:X:VALues) for frequency point data.

* * *

## SENSe<cnum>:FREQuency:CENTer <num>

Applicable Models: All (Read-Write) Sets the center frequency of the analyzer.
Note: When the sweep type is "segment sweep", this command is not used.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Center frequency. Choose any number between the minimum and maximum frequency limits of the analyzer. Units are Hz. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:FREQ:CENT 1000000 sense2:frequency:center 1mhz sense2:frequency:center 1e6  
Query Syntax | SENSe<cnum>:FREQuency:CENTer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Center of the analyzer's frequency span  
  
* * *

## SENSe<cnum>:FREQuency:CENTer:STEP:AUTO <bool>

Applicable Models: All (Read-Write) Sets and reads how the center frequency
step size is set. When TRUE, center steps by 5% of span. When FALSE, center
steps by STEP:SIZE value.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON (or 1) - Step size is set automatically. OFF (or 0) - Step size is set manually using [SENS:FREQ:CENT:STEP:SIZE](Frequency.md#StepSize)  
Examples | SENS:FREQ:CENT:STEP:AUTO 1  
Query Syntax | SENSe<cnum>:FREQuency:CENTer:STEP:AUTO?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<cnum>:FREQuency:CENTer:STEP:SIZE <num>

Applicable Models: All (Read-Write) Sets the center frequency step size of the
analyzer. This command sets the manual step size (only valid when STEP:AUTO is
FALSE).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Step size in Hz. Choose a value below the stop frequency of the analyzer.  
Examples | SENS:FREQ:CENT:STEP:SIZE 1e9  
Query Syntax | SENSe<cnum>:FREQuency:CENTer:STEP:SIZE?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Default is 40 MHz. When STEP:AUTO is TRUE, this value is ignored.  
  
* * *

## SENSe<cnum>:FREQuency[:CW |:FIXed] <num>

Applicable Models: All (Read-Write) Sets the Continuous Wave (or Fixed)
frequency. Must also send [SENS:SWEEP:TYPE CW](Sweep_SCPI.md#ssty) to put the
analyzer into CW sweep mode.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | CW frequency. Choose any number between the minimum and maximum frequency limits of the analyzer. Units are Hz. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:FREQ 1000000  
SENS:FREQ:CW MIN  
sense2:frequency:fixed 1mhz  
Query Syntax | SENSe<cnum>:FREQuency[:CW | :FIXed]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 GHz  
  
* * *

## SENSe<cnum>:FREQuency:SPAN <num>

Applicable Models: All (Read-Write) Sets the frequency span of the analyzer.
Note: When the sweep type is "segment sweep", this command is not used.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Frequency span in Hz. Choose any number from 70 (minimum) and the maximum frequency span of the analyzer. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:FREQ:SPAN 1000000  
sense2:frequency:span max  
Query Syntax | SENSe<cnum>:FREQuency:SPAN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum frequency span of the analyzer  
  
* * *

## SENSe<cnum>:FREQuency:SPAN:FULL

Applicable Models: All (Write-Only) Sets the frequency span to the entire
frequency range of the analyzer.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:FREQ:SPAN:FULL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum frequency span of the analyzer  
  
* * *

## SENSe<cnum>:FREQuency:STARt <num>

Applicable Models: All (Read-Write) Sets the start frequency of the analyzer.
Note: When the sweep type is "segment sweep", this command is not used.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Start frequency. Choose any number between the MIN and MAX frequency limits of the analyzer. Units are Hz. If FREQ:START is set greater than FREQ:STOP, then the stop frequency is set to the start frequency + frequency span. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:FREQ:STAR 1000000 sense2:frequency:start MIN  
Query Syntax | SENSe<cnum>:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Minimum frequency of the analyzer  
  
* * *

## SENSe<cnum>:FREQuency:STOP <num>

Applicable Models: All (Read-Write) Sets the stop frequency of the analyzer.
Note: When the sweep type is "segment sweep", this command is not used.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Stop frequency. Choose any number between 70 (minimum) and maximum frequency limits of the analyzer. Units are Hz. If FREQ:STOP is set less than FREQ:START, then the start frequency is set to the stop frequency - frequency span. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:FREQ:STOP 1000000 sense2:frequency:stop max  
Query Syntax | SENSe<cnum>:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum frequency of the analyzer  
  
* * *

![](../../../assets/images/Programming/Tp.gif)

