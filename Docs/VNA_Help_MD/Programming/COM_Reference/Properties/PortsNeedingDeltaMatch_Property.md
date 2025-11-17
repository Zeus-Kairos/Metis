##### Read-only  
  
---  
  
## PortsNeedingDeltaMatch Property

* * *

#### Description

|  Returns the port numbers for which delta match correction is required. 0
(zero) is returned if the Cal does NOT require Delta Match correction for one
of the following reasons:

  * The Cal does NOT involve Unknown Thru or TRL. You specify this using [ThruCalMethod Property](ThruCalMethod_Property.md).
  * The Cal DOES involve Unknown Thru or TRL, but the delta match data can be calculated by the Unknown Thru or TRL Cal. [Learn how this is possible.](../../../S3_Cals/TRL_Calibration.md#4Port) However, you can force the Cal to use the Delta Match data from a Cal Set.

  
---|---  
  
####  VB Syntax

|  value = guided.PortsNeedingDeltaMatch  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the returned list of port numbers.  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim ports As Variant  
ports = guided.PortsNeedingDeltaMatch  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortsNeedingDeltaMatch (VARIANT* portList);  
  
#### Interface

|  IGuidedCalibration2

