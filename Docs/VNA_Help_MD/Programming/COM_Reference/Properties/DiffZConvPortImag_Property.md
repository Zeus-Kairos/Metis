##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffZConvPortImag Property

* * *

#### Description

|  Sets the imaginary part of the impedance value for the differential port
impedance conversion function.  
---|---  
  
####  VB Syntax

|  fixture.DiffZConvPortImag(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2, or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (Double) Imaginary part of the Impedance value. Choose a value between 0 and 1E18  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.DiffZConvPortImag(2) = 75 'Write  
value = fixture.DiffZConvPortImag(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffZConvPortImag( short portNum, double *pVal)  
HRESULT put_DiffZConvPortImag( short portNum, double newVal)  
  
#### Interface

|  IFixturing2

