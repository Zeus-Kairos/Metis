##### Read/Write

|

##### [About Thru Methods](../../../S3_Cals/Calibration_THRU_Methods.md)  
  
---|---  
  
## PathThruMethod Property

* * *

#### Description

|  Note: This command replaces [ThruCalMethod](ThruCalMethod_Property.md).
(Read-Write) Specifies the calibration THRU method for each port pair. Note:
Sending this command will overwrite the VNAs SmartCal determination for the
thru method. Send this command ONLY if you have a deliberate reason for
overwriting the SmartCal logic.  You can send the query form of this command
to learn the THRU method determined by SmartCal. See [Thru Pairs
Sequence](../Objects/GuidedCalibration_Object.htm#THRUPairs) to learn how to
send this and other Thru commands. See an example of a [4-port guided
calibration using
COM](../../COM_Example_Programs/Perform_a_Guided_Cal_using_COM.htm).  
---|---  
  
#### VB Syntax

|  guidedCal.PathThruMethod (port1, port2) = "ThruType1[,ThruType2]"  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
port1 |  First port of the pair to be calibrated.  
port2 |  Second port of the pair to be calibrated.  
"ThruType1[,ThruType2]" |  (String) Thru methods for 1st and 2nd ports of the pair, enclosed in a single pair of quotes. NOT case-sensitive. thruType1 Calibration thru method for the pair if thruType2 is not specified. Otherwise, thru method for port 1. Choose from:

  * Defined Thru Measures a Thru for which there is a stored definition in the Cal Kit.
  * Zero Thru Measures a Zero length Thru, also known as Flush-Thru.
  * Undefined Thru A thru type for which there is NOT a stored definition in the Cal Kit. Also known as Unknown Thru. Valid ONLY for SOLT [cal type.](PathCalMethod_Property.md)
  * Undefined Thru using a Defined Thru (ECal modules ONLY) Measures the internal Thru as an Unknown Thru.

ThruType2 (String) Optional argument. Use ONLY when Adapter Removal Cal is
specified for the pair using [PathCalMethod](PathCalMethod_Property.md). When
specifying ThruType2, this is the only valid argument: "Defined Thru, Defined
Thru"  
  
#### Return Type

|  String - Returns comma-separated ThruTypes. Always returns two parts: If
the second part of the string is empty, adapter removal is NOT being
performed. If the string is "Defined Thru, Defined Thru", adapter removal IS
being performed.  
  
#### Default

|  The most accurate THRU method for the current cal.  
  
#### Example

|  guidedCal.PathThruMethod(2,3) = "Zero Thru" 'Write for port pair
guidedCal.PathThruMethod(1,4) = "Defined Thru, Defined Thru" 'Write for
adapter removal cal.  
calmethod = guided.PathThruMethod(1,4) 'Read previous example, return:
"Defined Thru, Defined Thru"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PathThruMethod(long firstport, long secondport, BSTR
*thruMethod); HRESULT put_PathThruMethod(long firstport, long secondport, BSTR
thruMethod);  
  
#### Interface

|  IGuidedCalibration3  
  
* * *

