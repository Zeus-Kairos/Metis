##### Write/Read

|

##### [About Traces](../../../S0_Start/Traces_Channels_and_Windows.md#trace)  
  
---|---  
  
## Name (Measurement) Property

* * *

#### Description

|  Sets (or returns) the Name of the measurement. Measurement names must be
unique among the set of measurements. Measurement names cannot be an empty
string. Note: This is the same name as trace.Name; when one changes, the other
changes.  
---|---  
  
####  VB Syntax

|  meas.Name = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (string) - A user defined name of the measurement  
  
#### Return Type

|  String  
  
#### Default

|  "CH1_S11_1" \- name of the default measurement  
  
#### Examples

|  meas.Name = "Filter BPass" 'Write  
MName = meas.Name 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Name(BSTR *pVal)  
HRESULT put_Name(BSTR newVal)  
  
#### Interface

|  IMeasurement

