##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffPortMatch_R Property

* * *

#### Description

|  Sets the Resistance value of the differential matching circuit.  
---|---  
  
####  VB Syntax

|  fixture.DiffPortMatch_R(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2, or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (Double) Resistance value in ohms. Choose a value between -1E18 to 1E18.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.DiffPortMatch_R(2) = 1e3 'Write  
value = fixture.DiffPortMatch_R(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffPortMatch_R(short portNum, double *pVal)  
HRESULT put_DiffPortMatch_R(short portNum, double newVal)  
  
#### Interface

|  IFixturing2

