##### Write/Read

|

##### [About Scale](../../../S1_Settings/Scale.md#Scale_Section)  
  
---|---  
  
## YScale Property

* * *

#### Description

|  Sets or returns the Y-axis Per-Division value of the active trace.  
---|---  
  
####  VB Syntax

|  trace.YScale = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trace |  A Trace (object)  
value |  (double) - Scale /division number. Units and range depend on the current data format.  
  
#### Return Type

|  Double  
  
#### Default

|  10 (db)  
  
#### Examples

|  trac.YScale = 5 'Write  
yscl = trac.YScale 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_YScale(double *pVal)  
HRESULT put_YScale(double newVal)  
  
#### Interface

|  ITrace

