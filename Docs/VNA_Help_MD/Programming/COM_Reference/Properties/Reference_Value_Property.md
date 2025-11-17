##### Write/Read

|

##### [About Reference Level](../../../S1_Settings/Scale.md#Ref_Level)  
  
---|---  
  
## ReferenceValue Property

* * *

#### Description

|  Sets or returns the value of the Y-axis Reference Level of the active
trace.  
---|---  
  
####  VB Syntax

|  trce.ReferenceValue = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trce |  A Trace (object)  
value |  (double) - Reference Value. Units and range depend on the current data format.  
  
#### Return Type

|  Double  
  
#### Default

|  Not applicable  
  
#### Examples

|  meas.ReferenceValue = 0 'Write  
rlev = meas.ReferenceValue 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ReferenceValue(double *pVal)  
HRESULT put_ReferenceValue(double newVal)  
  
#### Interface

|  ITrace

