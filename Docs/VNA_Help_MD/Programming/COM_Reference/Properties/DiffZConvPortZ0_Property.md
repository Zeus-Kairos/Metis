##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffZConvPortZ0 Property

* * *

#### Description

|  Sets the impedance value for the differential port impedance conversion
function. Set either this single value or set the
[real](DiffZConvPortReal_Property.md) and
[imaginary](DiffZConvPortImag_Property.md) parts separately. The imaginary
part is set to 0.0 using this command.  
---|---  
  
####  VB Syntax

|  fixture.DiffZConvPortZ0(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2, or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (Double) Impedance value. Choose a value between 0 and 1E18  
  
#### Return Type

|  Double  
  
#### Default

|  See Differential Port Z Conversion Default  
  
#### Examples

|  fixture.DiffZConvPortZ0(2) = 75 'Write  
value = fixture.DiffZConvPortZ0(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffZConvPortZ0( short portNum, double *pVal)  
HRESULT put_DiffZConvPortZ0( short portNum, double newVal)  
  
#### Interface

|  IFixturing2

