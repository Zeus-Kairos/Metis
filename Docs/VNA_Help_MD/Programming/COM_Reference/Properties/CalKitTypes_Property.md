##### Read-only

## CalKitTypes Property

* * *

#### Description

|  Returns the names of the available mechanical cal kits in your VNA that can
be used for unguided calibrations.  
---|---  
  
####  VB Syntax

|  value = cal.CalKitTypes (port)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
port |  Port number  
value |  (Variant) Variable to store the returned cal kit types.  
  
#### Return Type

|  Variant  
  
#### Examples

|  value = cal.CalKitTypes(4)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalKitTypes(VARIANT* calkits);  
  
#### Interface

|  ICalibrator10  
  
* * *

  

