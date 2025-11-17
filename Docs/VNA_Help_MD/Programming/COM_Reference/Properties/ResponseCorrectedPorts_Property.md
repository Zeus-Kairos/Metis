##### Read/Write

|

#####  
  
---|---  
  
## ResponseCorrectedPorts Property

* * *

#### Description

|  Sets and returns the selected ports to be corrected with enhanced response
calibration. [Learn
more](../../../S3_Cals/Guided_Power_Calibration.htm#MatchingDialog). Note: The
[CorrectionSubsettingState](CorrectionSubsettingState_Property.md) must be
set to ON to enable the response command.  
---|---  
  
####  VB Syntax

|  value = corrMethods.ResponseCorrectedPorts  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store a comma separated list of ports to include for enhanced response correction.  
corrMethods |  [CorrectionMethods](../Objects/CorrectionMethods_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  All ports included  
  
#### Examples

|  Example #1:  
16-port VNA with an active 16-port calibration  
  
corrMethods.CorrectionSubsettingState = True  
fullportlist = Array(1,2,3,4,5,6)  
fullportlist = corrMethods.FullyCorrectedPorts  
responseportlist = Array(7,8)  
responseportlist = corrMethods.ResponseCorrectedPorts  
  
Result: Full correction on ports 1-6 Enhanced response corrected for
parameters involving ports 7 and 8  
No correction for ports 9-16  
  
Example #2:  
16-port VNA with an active 16-port calibration  
  
corrMethods.CorrectionSubsettingState = True  
fullportlist = Array(0)  
fullportlist = corrMethods.FullyCorrectedPorts  
responseportlist = Array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)  
responseportlist = corrMethods.ResponseCorrectedPorts  
  
Result: Enhanced response correction for parameters involving any ports  
  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ResponseCorrectedPorts(VARIANT *portList); HRESULT
put_ResponseCorrectedPorts(VARIANT portList);  
  
#### Interface

|  ICorrectionMethods2  
  
* * *

