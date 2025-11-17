##### Write/Read

|

##### [About DC Sources](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
## Stop Property

* * *

#### Description

|  Sets and returns Stop DC value for the specified DC source.  
---|---  
  
####  VB Syntax

|  dc.Stop (name,port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
dc |  An [DCStimulus](../Objects/DCStimulus_Object.md) (object)  
name,port |  (String) Name of the "DC source, port" Use [Source Property](Source_Property.md) to read a list of configured DC source names. To set the DC source to be always ON, do NOT specify a port.  
value |  (Double) DC Stop value. Choose a value within the range of the DC source.  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  'Set AO1 to always ON dc.Stop "AO1", 3 'Read Stop for MyDCSource,Port 1
dc.Stop? "MyDCSource,Port 1"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stop(BSTR name, VARIANT_BOOL * pValue); HRESULT put_Stop(BSTR
name, VARIANT_BOOL newValue);  
  
#### Interface

|  IDCStimulus  
  
* * *

* * *

