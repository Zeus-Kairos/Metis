##### Read/Write

|

#####  
  
---|---  
  
## ThruPortList Property

* * *

#### Description

|  Note: Do NOT send this command to rely on SmartCal to determine the most
accurate Thru port pairs for the cal. You can send the query form of this
command to learn the port pairs determined by SmartCal. Sets and returns the
Thru connection port pairs for the calibration. Send the query form of this
command to learn the Thru pairs determined by SmartCal. See [Thru Pairs
Sequence](../Objects/GuidedCalibration_Object.htm#THRUPairs) to learn how to
send this and other Thru commands. Learn more about [Thru method and port
pairings](../../../S3_Cals/Calibration_Wizard.htm#ModifyThru). See an example
of a [4-port guided calibration using
COM](../../COM_Example_Programs/Perform_a_Guided_Cal_using_COM.htm).  
---|---  
  
#### VB Syntax

|  guidedCal.ThruPortList = t1a, t1b, t2a, t2b, t3a, t3b  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
t1a, t1b... |  (Variant) Port numbers in pairs - a one-dimensional array of Long integers. t1a, t1b (Thru1 - port A and port B) t2a, t2b (Thru2 - port A and port B) t3a, t3b (Thru3 - port A and port B)  
  
#### Return Type

|  Variant - a one-dimensional array of Long integers.  
  
#### Default

|  The most accurate port pairs for the cal.  
  
#### Example

|  thruList = Array(1,2,1,3,1,4) guided.ThruPortList = thruList 'Sets the
following three thru connections for a 4-port calibration:  
Thru 1 - ports 1 and 2  
Thru 2 - ports 1 and 3  
Thru 3 - ports 1 and 4  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ThruPortList(VARIANT* portList); HRESULT
put_ThruPortList(VARIANT portList);  
  
#### Interface

|  IGuidedCalibration  
  
* * *

