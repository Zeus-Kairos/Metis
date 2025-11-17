##### Read/Write

|

#####  
  
---|---  
  
## FullyCorrectedPorts Property

* * *

#### Description

|  Sets and returns the selected ports to include in a full NPort correction.
All other ports are corrected with enhanced response calibration if available.
[Learn more](../../../S3_Cals/Guided_Power_Calibration.md#MatchingDialog).
Note: The [CorrectionSubsettingState](CorrectionSubsettingState_Property.md)
must be set to ON to enable the full command.  
---|---  
  
####  VB Syntax

|  value = corrMethods.FullyCorrectedPorts  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store a comma separated list of ports to include in the full correction.  
corrMethods |  [CorrectionMethods](../Objects/CorrectionMethods_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  All ports included  
  
#### Example

|  16-port VNA with an active 16-port calibration  
  
corrMethods.CorrectionSubsettingState = True  
portlist = Array(1,2,3)  
portlist = corrMethods.FullyCorrectedPorts  
  
Result: Full correction on ports 1, 2, and 3  
All other port parameters are uncorrected  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FullyCorrectedPorts(VARIANT *portList); HRESULT
put_FullyCorrectedPorts(VARIANT portList);  
  
#### Interface

|  ICorrectionMethods2  
  
* * *

