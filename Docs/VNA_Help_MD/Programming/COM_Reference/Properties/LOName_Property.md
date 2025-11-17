##### Write/Read

|

##### About [Configure an External LO
Source](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## LOName Property

* * *

#### Description

|  Sets or returns the name of the VNA internal source or external source to
use as the LO in an FCA measurement.  
---|---  
  
####  VB Syntax

|  obj.LOName (n) =value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
n |  (Long) \- LO stage number Choose from 1 or 2  
value |  (string) \- LO Source name. Use [SourcePortNames Property](SourcePortNames_Property.md) to return a list of valid source ports. An external source must be configured and selected to be valid. [Learn more about external source configuration.](../../../System/Configure_an_External_Device.md) Note: If the port is defined by a string name, such as an external source or one of the Source 2 outputs on the 2-port, 2-source VNA-x model, then you must use [cap.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
  
#### Return Type

|  String  
  
#### Default

|  "Not controlled"  
  
#### Examples

|  mixer.LOName(1) = "MySource"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LOName(string *pVal) HRESULT put_LOName(string newVal)  
  
#### Interface

|  MIXer IConverter  
  
* * *

  

