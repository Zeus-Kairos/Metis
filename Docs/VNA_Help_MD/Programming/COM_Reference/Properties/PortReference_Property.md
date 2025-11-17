##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortReference Property

* * *

#### Description

|  Sets and reads the port to be used as a reference when controlling phase
for the specified <port>. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Refer To setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortReference (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (String) Reference port. Use [SourcePortNames](SourcePortNames_Property.md) to return a list of valid port names. The two internal VNA sources are available ONLY at specific ports. For example on a 4-port PNA-X, the possible port pairings are: 1/3, 1/4, 2/3, or 2/4. Port 1 can NOT be paired with Port 2, and Port 3 can NOT be paired with Port 4. [Learn more about these limitations.](../../../S0_Start/Internal_Second_Source.md#Restrictions)  
  
#### Return Type

|  String  
  
#### Default

|  Depends on <port>  
  
#### Examples

|  oDIQ.PortReference("port 1") = "Port 3"  
Value = oDIQ.PortReference("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortReference(BSTR port, BSTR* PortReference); HRESULT
put_PortReference(BSTR port, BSTR PortReference);  
  
#### Interface

|  IDIQ  
  
* * *

