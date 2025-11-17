# SENSe:CORRection:TDR Commands

These commands control loss compensation, fixture compensation after an ECal,
auto port extension, and reference impedance value.

SENSe:CORRection:TDR COLLection | DLComp | LOAD | OPEN | SAVE | THRU | ECAL | FCOMp | IMMediate | IMMediate DCONstant EXTension | AUTO | IMMediate | STANdard RIMPedance  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:CORRection:TDR:COLLection:DLComp:LOAD <int>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes load measurement, as a part of Loss Compensation sequence.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<int> | Port number where load measurement is executed. The range is 1 to 4.  
Examples | SENS:CORR:TDR:COLL:DLC:LOAD 1  
sense:correction:tdr:collection:dlcomp:load 1  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:COLLection:DLComp:OPEN <int>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes open (with Thru) measurement, as a part of Loss Compensation
sequence. This is used for Single Ended 1 Port only.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<int> | Port number where open measurement is executed. The range is 1 to 4.  
Examples | SENS:CORR:TDR:COLL:DLC:OPEN 1  
sense:correction:tdr:collection:dlcomp:open 1  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:COLLection:DLComp:SAVE

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
saves the result of the Loss Compensation sequence.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:CORR:TDR:COLL:DLC:SAVE  
sense:correction:tdr:collection:dlcomp:save  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:COLLection:DLComp:THRU <num>,<num>

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes a thru measurement, as a part of Loss Compensation sequence.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<num>,<num> | Enter the port numbers where the thru is connected. For example, 1,2 indicates that the thru is connected between ports 1 and 2. The range is 1 to 4.  
Examples | SENS:CORR:TDR:COLL:DLC:THRU 1,2  
sense:correction:tdr:collection:dlcomp:thru 1,2  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:COLLection:ECAL:FCOMp:IMMediate

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes fixture compensation after ECAL.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:CORR:TDR:COLL:ECAL:FCOM:IMM  
sense:correction:tdr:collection:ecal:fcomp:immediate  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:COLLection:ECAL:IMMediate

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes full calibration using the ECal module.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:CORR:TDR:COLL:ECAL:IMM  
sense:correction:tdr:collection:ecal:immediate  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:DCONstant <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the dielectric constant value.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | Dielectric constant value. The range is 10m to 100.  
Examples | SENS:CORR:TDR:DCON 0.01  
sense:correction:tdr:dconstant 0.01  
Query Syntax | SENSe<cnum>:CORRection:TDR:DCONstant?  
Return Type | Double  
Default | 1  
  
* * *

## SENSe<cnum>:CORRection:TDR:EXTension:AUTO:IMMediate

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes deskew (auto port extension).  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples | SENS:CORR:TDR:EXT:AUTO:IMM  
sense:correction:tdr:extension:auto:immediate  
Default | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TDR:EXTension:AUTO:STANdard <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the standard for deskew (auto port extension).  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> | Standard for deskew. Choose from: OPEN \- Open termination. SHORt \- Short termination.  
Examples | SENS:CORR:TDR:EXT:AUTO:STAN OPEN  
sense:correction:tdr:extension:auto:standard open  
Query Syntax | SENSe<cnum>:CORRection:TDR:EXTension:AUTO:STANdard?  
Return Type | String  
Default | OPEN  
  
* * *

## SENSe<cnum>:CORRection:TDR:RIMPedance <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the reference impedance value.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | Reference impedance value. The range is 1m to 10M.  
Examples | SENS:CORR:TDR:RIMP 0.001  
sense:correction:tdr:rimpedance 0.001  
Query Syntax | SENSe<cnum>:CORRection:TDR:RIMPedance?  
Return Type | Double  
Default | 50  
  
* * *

