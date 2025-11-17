##### Read / Write

|

#####  
  
---|---  
  
## ConnectorType Property

* * *

#### Description

|  Sets or queries the connector type for the specified port.  
---|---  
  
#### VB Syntax

|  obj.ConnectorType (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object)  
port |  (Long) Port number of the connector type. For Guided Cals and SMC, select port number. For VMC calibrations:

  * 1 - Mixer Input.
  * Any unused port can be used for the mixer output.
  * Output port of MUT +1 - Output port of the calibration mixer. Generally this is port 3.

  
  
#### value

|  (String) - Connector type. Case-sensitive. Use [ValidConnectorType
Property](ValidConnectorType_Property.htm) to list connector types.  
  
#### Return Type

|  String  
  
#### Default

|  None  
  
#### Examples

|  SMC.ConnectorType(1) = "APC 3.5 male" value = SMC.ConnectorType(1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ConnectorType(long port, BSTR *connector) HRESULT
put_ConnectorType(long port, BSTR connector)  
  
#### Interface

|  IGuidedCalibration SMCType VMCType  
  
* * *

