# Sense:Role Commands

* * *

Controls the path configuration settings.

SENSe:ROLE: | [CATalog?](Path.md#catalog) | [DEVice](Role.md#Device)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:ROLE:CATalog?

Applicable Models: N522xB, N523xB, N524xB (Read-only) This command replaces
[SENS:MIX:ROLE:CATalog?](MIXerSCPI.md#RoleCat) Returns the roles for which
sources can be used for the channel.  
---  
Parameters |   
<ch> |  Channel number of the measurement. If unspecified, value is set to 1.  
Examples |  SENS:ROLE:CAT?  
Return Type |  Comma-separated list of double-quoted strings.  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:ROLE:DEVice <role>,<source>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Set and return the
source to be used in the specified role. For example, use this command to set
a source name to be used as the RF2 tone for a Swept IMD channel.  Note: This
command cannot be used to set the input/output ports for mixer based
applications. For those, you must use a combination of SENS:<APP>:PMAP and
SENS:MIX:PMAP. For example, for IMDX you must use
[SENS:IMD:PMAP](IMD.md#PMap) or [SENS:MIX:PMAP ](MIXerSCPI.md#pmap).  
---  
Parameters |   
<ch> |  Channel number of the measurement. If unspecified, value is set to 1.  
<role> |  (String) Role of the source. Not context-sensitive. Use SENSe:ROLE:CATalog? to read the valid roles for the channel.  
<source> |  (String) Source name to be used in the specified role. Use [SYSTem:CONFigure:EDEVice:CAT?](../SystConfigExternalDevice.md#cat) to read a list of configured sources.  
Examples |  SENS2:ROLE:DEV "RF2","MyEsg"  
Query Syntax |  SENSe<ch>:ROLE:DEVice? <role>  
Return Type |  String  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

* * *

