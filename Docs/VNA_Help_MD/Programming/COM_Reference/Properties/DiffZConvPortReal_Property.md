##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffZConvPortReal Property

* * *

#### Description

|  Sets the real part of the impedance value for the differential port
impedance conversion function.  
---|---  
  
####  VB Syntax

|  fixture.DiffZConvPortReal(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2, or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (Double) Real part of the Impedance value. Choose a value between 0 and 1E18  
  
#### Return Type

|  Double  
  
#### Default

|  See Differential Port Z Conversion Default  
  
#### Examples

|  fixture.DiffZConvPortReal(2) = 75 'Write  
value = fixture.DiffZConvPortReal(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffZConvPortReal( short portNum, double *pVal)  
HRESULT put_DiffZConvPortReal( short portNum, double newVal)  
  
#### Interface

|  IFixturing2  
  
* * *

