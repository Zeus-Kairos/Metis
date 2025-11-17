##### Write/Read

|

##### [About DC Sources](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
## State Property

* * *

#### Description

|  Sets and returns the ON / Off state of the specified DC source and port.  
---|---  
  
####  VB Syntax

|  dc.State(name,port) = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
dc |  An [DCStimulus](../Objects/DCStimulus_Object.md) (object)  
name,port |  (String) Name of the "DC source, port" Use [Source Property](Source_Property.md) to read a list of configured DC source names. To set the DC source to be always ON, do NOT specify a port.  
state |  Boolean. ON / Off state. Choose from: True - DC source/port enabled. False - DC source/port disabled.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  'Set AO1 to always ON dc.State "AO1",True 'Set MyDCSource to ON when the RF
source for Port 1 is ON dc.State "MyDCSource,Port 1",ON 'Read state for
MyDCSource,Port 1 dc.State? "MyDCSource,Port 1"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_State(BSTR name, VARIANT_BOOL * pValue); HRESULT put_State(BSTR
name, VARIANT_BOOL newValue);  
  
#### Interface

|  IDCStimulus  
  
* * *

* * *

