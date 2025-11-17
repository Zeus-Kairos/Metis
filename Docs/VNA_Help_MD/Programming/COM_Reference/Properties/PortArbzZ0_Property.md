##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortArbzZ0 Property

* * *

#### Description

|  Sets and returns the Real portion of the impedance value for the specified
single-ended port. The imaginary portion is automatically set to 0.0. To set
both values separately, use [PortArbzReal](PortArbzReal_Property.md) and
[PortArbzImag](PortArbzImag_Property.md).  
---|---  
  
####  VB Syntax

|  fixture.PortArbzZ0(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Single-ended port number to receive impedance value.  
value |  (Double) Impedance value. Choose a value between 0 to 1E7  
  
#### Return Type

|  Double  
  
#### Default

|  50  
  
#### Examples

|  fixture.PortArbzZ0(2) = 75 'Write  
value = fixture.PortArbzZ0(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortArbzZ0( short portNum, double *pVal)  
HRESULT put_PortArbzZ0( short portNum, double newVal)  
  
#### Interface

|  IFixturing3

