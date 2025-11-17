##### Write/Read

|

##### [About Trace Max](../../../Front_Panel/XScreen.md#Traces)  
  
---|---  
  
## TraceMax Property

* * *

#### Description

|  Maximizes (isolates) or restores the active trace in the active window.
When TraceMax is ON, the active trace is the ONLY trace on the display. All
other traces are hidden.  
---|---  
  
####  VB Syntax

|  meas.TraceMax = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
state |  (boolean) - Choose from: True \- Maximizes / isolates the active trace in the window. False - Restores other traces to be viewed in the window.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.TraceMax = True  
state = meas.TraceMax  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TraceMax(VARIANT_BOOL bState)  
HRESULT put_TraceMax(VARIANT_BOOL* bState)  
  
#### Interface

|  IMeasurement10  
  
* * *

