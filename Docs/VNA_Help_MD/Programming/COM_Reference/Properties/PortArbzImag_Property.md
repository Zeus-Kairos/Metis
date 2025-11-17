##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortArbzImag Property

* * *

#### Description

|  Sets and returns the Imaginary portion of the impedance value for the
specified single-ended port. Use [PortArbzReal](PortArbzReal_Property.md) to
set the real value. Or use [PortArbzZ0](PortArbzZ0_Property.md) to set both
values together.  
---|---  
  
####  VB Syntax

|  fixture.PortArbzImag(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Single-ended port number to receive impedance value.  
value |  (Double) Real Impedance value. Choose a value between -1E18 and 1E18  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortArbzImag(2) = 75 'Write  
value = fixture.PortArbzImag(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortArbzImag( short portNum, double *pVal)  
HRESULT put_PortArbzImag( short portNum, double newVal)  
  
#### Interface

|  IFixturing3

