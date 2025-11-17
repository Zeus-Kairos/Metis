##### Write/Read

|

##### [About Math Operations](../../../S4_Collect/Math_Operations.md)  
  
---|---  
  
## View Property

* * *

#### Description

|  Sets (or returns) the type of trace displayed on the screen.  
---|---  
  
####  VB Syntax

|  meas.View = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A measurement (object)  
value |  (enum NAView) - Type of trace. Choose from: 0 \- naData  
1 \- naDataAndMemory  
2 \- naMemory  
3 \- naNoTrace Note: The naData trace may reflect the result of a
[TraceMath](Trace_Math_Property.md) operation.  
  
#### Return Type

|  NAView  
  
#### Default

|  naData  
  
#### Examples

|  meas.View = naData 'Write  
trceview = meas.View 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_View(tagNAView* pView)  
HRESULT put_View(tagNAView newView)  
  
#### Interface

|  IMeasurement

