##### Write/Read

|

##### [About Trace
Title](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle)  
  
---|---  
  
## TraceTitle Property

* * *

#### Description

|  Writes and reads data for the trace title area. The trace title is embedded
in the trace status field. [Learn more about Trace
Titles](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm#TraceTitle)
The title is turned ON and OFF using
[TraceTitleState](TraceTitleState_Property.md).  
---|---  
  
####  VB Syntax

|  meas.TraceTitle = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (string) \- Title to be displayed. Any characters (no spaces), enclosed with quotes.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meas.TraceTitle = "My new s11 measurement"  
title = TraceTitle 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TraceTitle(BSTR *title );  
HRESULT put_TraceTitle(BSTR title );  
  
#### Interface

|  IMeasurement8  
  
* * *

