# SOURce:TDR Commands

SOURce:TDR POWer | LEVel | IMMediate | AMPLitude  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SOURce<cnum>:TDR:POWer[:LEVel][:IMMediate][:AMPLitude] <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the source power level.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> | Source power level in dBm.  
Examples | SOUR:TDR:POW 20 source:tdr:power:level:immediate:amplitude 20  
Query Syntax | SOURce:TDR:POWer[:LEVel][:IMMediate][:AMPLitude]?  
Return Type | Double  
Default | -8 dBm  
  
* * *

##

