##### Read/Write

|

##### [About Cal Methods](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## PathCalMethod Property

* * *

#### Description

|  Note: This command replaces [ThruCalMethod](ThruCalMethod_Property.md).
(Read-Write) Specifies the calibration method for each port pair. Note:
Sending this command will overwrite the VNAs SmartCal determinations for the
most accurate cal method for your connector settings and Cal Kits. Send this
command ONLY if you have a deliberate reason for overwriting the SmartCal
logic. You can send the query form of this command to learn the cal method
determined by SmartCal. See [Thru Pairs
Sequence](../Objects/GuidedCalibration_Object.htm#THRUPairs) to learn how to
send this and other Thru commands. After sending this command, send the query
form to be sure that the command was accepted. If not, then the chosen Cal
method is not compatible with the specified Thru method. For example, if the
specified Thru method is Unknown Thru, an attempt to set Enhanced Response Cal
should be rejected. See an example of a [4-port guided calibration using
COM](../../COM_Example_Programs/Perform_a_Guided_Cal_using_COM.htm).  
---|---  
  
#### VB Syntax

|  guidedCal.PathCalMethod (port1, port2) = "caltype1[,caltype2]"  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
port1 |  First port of the pair to be calibrated.  
port2 |  Second port of the pair to be calibrated.  
"caltype1,[caltype2]" |  (String) Cal types for 1st and 2nd ports of the pair, enclosed in a single pair of quotes. NOT case-sensitive. caltype1 Cal type for the pair if caltype2 is not specified. Otherwise, Cal type for port 1.Choose from:

  * TRL
  * SOLT
  * QSOLTN
  * EnhRespN

For the last two arguments, replace N with the port to be used as the source
port, which MUST be one of the port pair. [caltype2] Optional argument. Use
only when performing an adapter removal cal on the pair. This argument
specifies the Cal Type on the second port; caltype1 then specifies the Cal
Type of the first port. Choose from the same arguments as caltype1.  
  
#### Return Type

|  String - Returns comma-separated cal types.  
  
#### Default

|  The most accurate cal method for the current cal.  
  
#### Example

|  guidedCal.PathCalMethod(2,3) = "TRL" 'Write trl for port pair
guidedCal.PathCalMethod(1,4) = "TRL,SOLT" 'Write adapter removal cal,
consisting of trl on port 1 and solt on port 4  
calmethod = guided.PathCalMethod(1,4) 'Read previous example, returns:
"TRL,SOLT"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PathCalMethod(long firstport, long secondport, BSTR
*calMethod); HRESULT put_PathCalMethod(long firstport, long secondport, BSTR
calMethod);  
  
#### Interface

|  IGuidedCalibration3  
  
* * *

