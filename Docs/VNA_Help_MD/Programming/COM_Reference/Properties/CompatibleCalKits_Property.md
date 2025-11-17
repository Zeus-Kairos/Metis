##### Read-only

|

#####  
  
---|---  
  
## CompatibleCalKits Property

* * *

#### Description

|  Returns a comma-separated list of valid kits that use the specified
connector type. This includes mechanical cal kits, applicable
characterizations found within ECal modules currently connected to the VNA,
and all user characterizations stored in VNA disk memory. Note: The serial
number is returned for ALL ECal modules that are connected with the connector
type of the specified port. Previously, the returned list would include the
serial numbers to distinguish the ECal modules only when two or more identical
ECal models were connected to the VNA.  
---|---  
  
####  VB Syntax

|  value = obj.CompatibleCalKits (port)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the returned list of Cal Kits.  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) Superseded Replaced with [GetCompatibleCalKits Method](../Methods/GetCompatibleCalKits_Method.md) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object)  
  
#### port

|  (Long) Port number for which you want compatible kits. First set the
[ConnectorType](ConnectorType_Property.md) for the port.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim kits As Variant  
kits = MySMC.CompatibleCalKits(1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompatibleCalKits(long port, VARIANT* Kits);  
  
#### Interface

|  IGuidedCalibration SMCType VMCType  
  
* * *

  

