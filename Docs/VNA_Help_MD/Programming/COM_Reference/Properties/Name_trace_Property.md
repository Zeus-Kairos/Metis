##### Write/Read

|

##### [About Traces](../../../S0_Start/Traces_Channels_and_Windows.md#trace)  
  
---|---  
  
## Name (trace) Property

* * *

#### Description

|  Sets or returns the name of the Trace. Use the trace name to identify the
trace and refer to the trace in the collection. Note: This is the same name as
meas.Name; when one changes, the other changes.  
---|---  
  
####  VB Syntax

|  trac.Name = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trac |  A Trace (object)  
value |  (String) Trace name  
  
#### Return Type

|  String  
  
#### Default

|  "CH1_S11_1" \- name of the default measurement  
  
#### Examples

|  trace.Name = "myTrace" 'Write  
traceName = Name.Trace 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Name(BSTR name)  
HRESULT get_Name(BSTR *name)  
  
#### Interface

|  ITrace

