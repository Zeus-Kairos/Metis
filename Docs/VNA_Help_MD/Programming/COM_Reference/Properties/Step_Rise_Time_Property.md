##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## StepRiseTime Property

* * *

#### Description

|  Sets or returns the Rise time of the stimulus in Low Pass Step Mode.  
---|---  
  
####  VB Syntax

|  trans.StepRiseTime = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A Transform (object)  
value |  (double) - Rise time in seconds. Choose any number between 5.0e-13 and 1.63e-14.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  trans.StepRiseTime = 1.0e-14 'sets the step rise time to 100 psec. -Write  
rt = trans.StepRiseTime 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StepRiseTime(double *pVal)  
HRESULT put_StepRiseTime(double newVal)  
  
#### Interface

|  ITransform

