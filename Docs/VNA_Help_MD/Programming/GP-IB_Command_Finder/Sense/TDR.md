# SENSe:TDR Commands

These commands control bandwidth, DUT information, avoid spurious function,
and sweep.

SENSe:TDR BWIDth | [:RESolution] DLENgth | AUTO | IMMediate | DATA SPURious | AVOid | IMMediate | STATe? | INPut | DRATe | STATe? SWEep | AVERage | MODE | SINGLe  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:TDR:BWIDth[:RESolution] <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the IF bandwidth value.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | IF bandwidth value in Hz.  
Examples | SENS:TDR:BWID:RES 100E3  
sense:tdr:bwidth:resolution 100e3  
Query Syntax | SENSe<cnum>:TDR:BWIDth[:RESolution]?  
Return Type | Double  
Default | 100 kHz  
  
* * *

## SENSe<cnum>:TDR:DLENgth:AUTO:IMMediate

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes auto DUT length setting.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:TDR:DLEN:AUTO:IMM  
sense:tdr:dlength:auto:immediate  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:TDR:DLENgth:DATA <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the DUT length value.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | DUT length value in seconds. The range is 6.26n to 416n  
Examples | SENS:TDR:DLEN:DATA 6.26E-9  
sense:tdr:dlength:data 6.26e-9  
Query Syntax | SENSe<cnum>:TDR:DLENgth:DATA?  
Return Type | Double  
Default | 6.26n  
  
* * *

## SENSe<cnum>:TDR:SPURious:AVOid:IMMediate

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes avoid spurious.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:TDR:SPUR:AVO:IMM  
sense:tdr:spurious:avoid:immediate  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:TDR:SPURious:AVOid:STATe?

Applicable Models: All with TDR Options (S9x011A/B) (Read-only) This command
queries the avoid spurious state. This command is used only with Hot TDR mode.

  * This command is ON when :SENS:TDR:SPURious:AVOid:IMMediate command succeeds.
  * This command is OFF when :SENS:TDR:SPURious:AVOid:IMMediate command fails to find a spur.

  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:TDR:SPUR:AVO:STAT?  
sense:tdr:spurious:avoid:state?  
Return Type | Boolean 1 - ON 0 - OFF  
  
* * *

## SENSe<cnum>:TDR:SPURious:INPut:DRATe <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the value of input bit rate for avoid spurious.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | Value of input bit rate in bits per second (bps). The range is 1.21E6 to 60.8E9.  
Examples | SENS:TDR:SPUR:INP:DRAT 1.5E9  
sense:tdr:spurious:input:drate 1.5e9  
Query Syntax | SENSe<cnum>:TDR:SPURious:INPut:DRATe?  
Return Type | Double  
Default | 1E9  
  
* * *

## SENSe<cnum>:TDR:SPURious:STATe?

Applicable Models: All with TDR Options (S9x011A/B) (Read-only) This command
queries the Hot TDR mode status.

  * To turn ON Hot TDR mode, use :SENSe:TDR:SPURious:AVOid:IMMediate
  * To turn OFF Hot TDR mode, use [:SYSTem:PRESet](../System.md#pre)

  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:TDR:SPUR:STAT?  
sense:tdr:spurious:state?  
Return Type | Boolean 1 - ON 0 - OFF  
  
* * *

## SENSe<cnum>:TDR:SWEep:AVERage <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the TDR averaging trigger state on/off. When averaging trigger is on, one
trigger makes one averaging measurement. For example, if the averaging factor
is set at 16, one trigger makes a measurement 16 times.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> | ON or 1 \- Turns averaging trigger on.   
OFF or 0 \- Turns averaging trigger off.  
Examples | SENS:TDR:SWE:AVER ON  
sense:tdr:sweep:average on  
Query Syntax | SENSe<cnum>:TDR:SWEep:AVERage?  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<cnum>:TDR:SWEep:MODE <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets trigger mode.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> | Trigger mode. Choose from: HOLD \- Trigger is on hold until the conditions are met, then the trigger event starts. SINGle \- Trigger event is run once. RUN \- Trigger event runs continuously.  
Examples | SENS:TDR:SWE:MODE RUN  
sense:tdr:sweep:mode run  
Query Syntax | SENSe<cnum>:TDR:SWEep:MODE?  
Return Type | String  
Default | RUN  
  
* * *

## SENSe<cnum>:TDR:SWEep:SINGle

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes single trigger.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:TDR:SWE:SING  
sense:tdr:sweep:single  
Default | Not Applicable  
  
* * *

##

