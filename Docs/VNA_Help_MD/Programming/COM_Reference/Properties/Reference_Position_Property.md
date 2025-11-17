##### Write/Read

|

##### [About Reference Position](../../../S1_Settings/Scale.md#Ref_Pos)  
  
---|---  
  
## ReferencePosition Property

* * *

#### Description

|  Sets or returns the Reference Position of the active trace.  
---|---  
  
####  VB Syntax

|  trce.ReferencePosition = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trce |  A Trace (object)  
value |  (double) - Reference position on the screen measured in horizontal graticules from the bottom of the screen. Choose from any number between: 0 and 10.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  meas.ReferencePosition = 5 'Middle of the screen -Write  
rpos = meas.ReferencePosition -Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ReferencePosition(double *pVal)  
HRESULT put_ReferencePosition(double newVal)  
  
#### Interface

|  ITrace

