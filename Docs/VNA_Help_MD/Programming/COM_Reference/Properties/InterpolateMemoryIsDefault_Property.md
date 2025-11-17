##### Write/Read

|

##### [About
Interpolation](../../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation)  
  
---|---  
  
# InterpolateMemoryIsDefault Property

* * *

#### Description

|  Sets and reads the state of the memory data interpolation default
preference. The PNA will return to the default interpolation state after a
Preset, creating a new trace, or closing the PNA application. [Learn
more](../../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation).  
---|---  
  
####  VB Syntax

|  pref.InterpolateMemory = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (boolean)  
False \- Set memory interpolation to OFF as the default. True - Set memory
interpolation to ON as the default.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.InterpolateMemorysSDefault = True 'Write  
prefer = pref.InterpolateMemory 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InterpolateMemory(VARIANT_BOOL *intState)  
HRESULT put_InterpolateMemory(VARIANT_BOOL intState)  
  
#### Interface

|  IPreferences

