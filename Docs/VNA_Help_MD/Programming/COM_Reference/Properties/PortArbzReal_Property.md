##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortArbzReal Property

* * *

#### Description

|  Sets and returns the Real portion of the impedance value for the specified
single-ended port. Use [PortArbzImag](PortArbzImag_Property.md) to set the
imaginary value. Or use [PortArbzZ0](PortArbzZ0_Property.md) to set both
values together.  
---|---  
  
####  VB Syntax

|  fixture.PortArbzReal(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Single-ended port number to receive impedance value.  
value |  (Double) Real Impedance value. Choose a value between 0 to 1E7  
  
#### Return Type

|  Double  
  
#### Default

|  50  
  
#### Examples

|  fixture.PortArbzReal(2) = 75 'Write  
value = fixture.PortArbzReal(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortArbzReal( short portNum, double *pVal)  
HRESULT put_PortArbzReal( short portNum, double newVal)  
  
#### Interface

|  IFixturing3

