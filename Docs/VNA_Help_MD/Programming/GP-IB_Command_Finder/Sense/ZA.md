# SENSe:ZA Commands

These commands control the compensation in the Impedance Measurement class.

SENSe:ZA CORRection:CSET:IMPort | [FIXTure](ZA.md#CorrCsetImpFixt) | [SPARm](ZA.md#CorrCsetImpSpar) FIXTURE | [RESPonse:FILE](ZA.md#FixtRespFile) | CKIT | OPEN | [G](ZA.md#FixtCkitOpenG) | [C](ZA.md#FixtCkitOpenC) | SHORt | [R](ZA.md#FixtCkitShorR) | [L](ZA.md#FixtCkitShorL) [PORT](ZA.md#Port)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:ZA:CORRection:CSET:IMPort:FIXTure <bool>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) Sets and returns the ON |OFF state of Fixture Compensation .The Fixture
Compensation data from the selected Cal Sets is enabled.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | ON | OFF state. Choose from 0 - Fixture Compensation is disabled 1 - Fixture Compensation is enable  
Examples | SENS:ZA:CORR:CSET:IMP:FIXT ON sense2:za:correction:cset:import:fixture 1  
Query Syntax | SENSe<cnum>:ZA:CORRection:CSET:IMPort:FIXTure?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<cnum>:ZA:CORRection:CSET:IMPort:SPARam <bool>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) Sets and returns the ON |OFF state of S-Parameter calibration .The
S-Parameter calibration data from the selected Cal Sets is enabled.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | ON | OFF state. Choose from 0 - S-Parameter calibration is disabled 1 - S-Parameter calibration is enable  
Examples | SENS:ZA:CORR:CSET:IMP:SPAR ON sense2:za:correction:cset:import:sparam 1  
Query Syntax | SENSe<cnum>:ZA:CORRection:CSET:IMPort:SPARm?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<cnum>:ZA:FIXTure:RESPonse:FILE <FileName>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) This command selects the fixture (16198A-010) calibration data file
(.dat) which is provided by Keysight.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<FileName> | calibration data file  
Examples | SENS:ZA:FIXT:SEL "C:\Fixture_Data_xxxxxxxxx.dat"  
sense:za:fixture:select "C:\Fixture_Data_xxxxxxxxx.dat"  
Query Syntax | SENSe<cnum>:ZA:FIXTure:SELect?  
Return Type | String  
Default | Null  
  
* * *

## SENSe<cnum>:ZA:FIXTure:CKIT:OPEN:G <value>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) This command sets/returns the G value of Open Standard for the fixture
compensation.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | G value of Open Standard  
Examples | SENS:ZA:FIXT:CKIT:OPEN:G 1e-5 sense:za:fixture:ckit:open:g 1e-5  
Query Syntax | SENSe<cnum>:ZA:FIXTure:CKIT:OPEN:G?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:ZA:FIXTure:CKIT:OPEN:C <value>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) This command sets/returns the capacitance value of Open Standard for
the fixture compensation.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | C value of Open Standard  
Examples | SENS:ZA:FIXT:CKIT:OPEN:C 1e-5 sense:za:fixture:ckit:open:c 1e-5  
Query Syntax | SENSe<cnum>:ZA:FIXTure:CKIT:OPEN:C?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:ZA:FIXTure:CKIT:SHORt:R <value>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) This command sets/returns the resistance value of Short Standard for
the fixture compensation.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | R value of Open Standard  
Examples | SENS:ZA:FIXT:CKIT:SHOR:R 1e-5 sense:za:fixture:ckit:short:r 1e-5  
Query Syntax | SENSe<cnum>:ZA:FIXTure:CKIT:SHORt:R?  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:ZA:FIXTure:CKIT:SHORt:L <value>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) This command sets/returns the inductance value of Short Standard for
the fixture compensation.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | L value of Open Standard  
Examples | SENS:ZA:FIXT:CKIT:SHOR:L 1e-5 sense:za:fixture:ckit:short:l 1e-5  
Query Syntax | SENSe<cnum>:ZA:FIXTure:CKIT:SHORt:L?  
Return Type | Numeric  
Default | 0  
  
* * *

* * *

## SENSe<cnum>:ZA:PORT <string>

Applicable Models: All with Impedance Measurement Options (S9x041B) (Read-
Write) This command sets/returns the port for the impedance  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<string> | Port number  
Examples | SENS:ZA:PORT "1" sense:za:port "2"  
Query Syntax | SENSe<cnum>:ZA:PORT?  
Return Type | Numeric  
Default | "1"

