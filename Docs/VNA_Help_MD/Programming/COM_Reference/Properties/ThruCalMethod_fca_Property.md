##### Read/Write

|

#####  
  
---|---  
  
## ThruCalMethod Property - Superseded

* * *

#### Description

|  This command is replaced by [PathThruMethod
Property](PathThruMethod_Property.htm). Sets and returns the method for
performing the thru portion of the calibration.  
---|---  
  
#### VB Syntax

|  obj.ThruCalMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  [SMCType](../Objects/SMC_Type_Object.md) (object) or [VMCType](../Objects/VMC_Type_Object.md) (object)  
value |  (String) Specifies the Thru method. Case insensitive - include spaces. Choose from: "Default" "Flush Thru" or "FLUSH" "Unknown Thru" or "UNKN" "Adapter Removal" or "ADAP"  
  
#### Return Type

|  String  
  
#### Default

|  Default  
  
#### Examples

|  SMC.ThruCalMethod = "UNKN"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ThruCalMethod(enum NAThruCalMethod thruMethod); HRESULT
get_ThruCalMethod(enum NAThruCalMethod *thruMethod);  
  
#### Interface

|  SMCType VMCType

