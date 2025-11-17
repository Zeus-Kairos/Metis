##### Write/Read

|

##### [About Trace
Title](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle)  
  
---|---  
  
## TraceTitleState Property

* * *

#### Description

|  Turns display of the Trace Title ON or OFF. When turned OFF, the previous
trace title returns. Create a trace title using [TraceTitle
Property](TraceTitle_Property.htm)  
---|---  
  
####  VB Syntax

|  meas.TraceTitleState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (boolean) - Choose from: True \- Turns the trace title ON False \- Turns the trace title OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.TraceTitleState = False  
title = TraceTitleState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TraceTitleState(VARIANT_BOOL *isTitleON);  
HRESULT put_TraceTitleState(VARIANT_BOOL isTitleON);  
  
#### Interface

|  IMeasurement8  
  
* * *

