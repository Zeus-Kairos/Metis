##### Read-only

# ReceivePort Property

* * *

#### Description

|  Returns the receiver (response) port number of measurement. To understand
how this property is useful, see [IMeasurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface). Note:
Returning a receiver port is only supported for S-Parameter measurements. If
the measurement is not an S-Parameter, then E_NA_BAD_PARAMETER is returned.  
---|---  
  
####  VB Syntax

|  value = meas.ReceivePort  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) \- Variable to store the returned value  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  rp = meas.ReceivePort  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ReceivePort(Long* rcvPort);  
  
#### Interface

|  IMeasurement2

