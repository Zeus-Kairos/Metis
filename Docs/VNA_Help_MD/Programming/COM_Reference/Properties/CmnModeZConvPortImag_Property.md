##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## CmnModeZConvPortImag Property

* * *

#### Description

|  Sets the imaginary part of the impedance value for the common port
impedance conversion function.  
---|---  
  
####  VB Syntax

|  fixture.CmnModeZConvPortImag(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2, or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (Double) Imaginary part of the Impedance value. Choose a value between 0 and 1E18.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.CmnModeZConvPortImag(2) = 75 'Write  
value = fixture.CmnModeZConvPortImag(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CmnModeZConvPortImag( short portNum, double *pVal)  
HRESULT put_CmnModeZConvPortImag( short portNum, double newVal)  
  
#### Interface

|  IFixturing2

