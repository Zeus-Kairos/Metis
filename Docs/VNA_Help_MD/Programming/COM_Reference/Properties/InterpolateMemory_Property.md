##### Write/Read

|

##### [About
Interpolation](../../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation)  
  
---|---  
  
# InterpolateMemory Property

* * *

#### Description

|  Sets and reads the state of the memory data interpolation. [Learn
more](../../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation).  
---|---  
  
####  VB Syntax

|  meas.InterpolateMemory = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
bool |  (boolean)  
False \- Turn memory data interpolation OFF. True - Turn memory data
interpolation ON.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.InterpolateMemory = True 'Write  
state = meas.InterpolateMemory 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InterpolateMemory(VARIANT_BOOL *intState)  
HRESULT put_InterpolateMemory(VARIANT_BOOL intState)  
  
#### Interface

|  IMeasurement18

