##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## ListData Property

* * *

#### Description

|  Sets and returns the DC stimulus values per point from the specified DC
source. This setting overrides the Start and Stop DC settings for the channel.
Only the values that are set with this command can be read by this command.
The read command does NOT read the values that are set using the Start and
Stop settings.  
---|---  
  
####  VB Syntax

|  DCStim.ListData(name,port) = values  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DCStim |  A [DCStimulus](../Objects/DCStimulus_Object.md) (object)  
name,port |  (String) Name of the DC source and source port. Use Source Property to read a list of configured DC source names. To set the DC source to be always ON, do NOT specify a port.  
value |  (Variant) DC stimulus value array. The size of the array must equal the sweep point number.  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'The following shows how to set a DC value for each data point dim data(2)
data(0) = 1 data(1) = 2 data(2) = 1 DC.ListData("AO1") = data 'Read varData =
dc.ListData("AO1") for i=0 to 2 msgbox (varData (i)) next  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ListData(BSTR name, VARIANT * pValue); HRESULT
put_ListData(BSTR name, VARIANT newValue);  
  
#### Interface

|  IExternalDCSource  
  
* * *

* * *

