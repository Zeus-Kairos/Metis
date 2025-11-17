##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortLevelingMode Property

* * *

#### Description

|  Sets and reads the leveling mode to be used for the specified source port.
On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Leveling Mode setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortLevelingMode (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (String) Leveling mode. Choose from: "Internal" \- Standard internal analyzer leveling mode. "Internal-R<n>,<p>" \- Receiver Leveling, where: <n> is the receiver name. <p> is the source port to be leveled. "Open Loop" \- Open loop leveling, used during pulse conditions with the internal source modulators. NOT available on all models. No leveling is used in setting the source power. The lowest settable power, without attenuation, is limited to -30dBm. The source power level accuracy is very compromised. Use a source power calibration to make the source power somewhat more accurate. "Open Loop-<n>,<p>" \- Open loop leveling, where: <n> is the receiver name. <p> is the source port to be leveled  
  
#### Return Type

|  String  
  
#### Default

|  "Internal"  
  
#### Examples

|  oDIQ.PortLevelingMode("port 2") = "Internal-a2,1"  
Value = oDIQ.PortLevelingMode("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortLevelingMode(BSTR port, BSTR* PortLevelingMode); HRESULT
put_PortLevelingMode(BSTR port, BSTR PortLevelingMode);  
  
#### Interface

|  IDIQ  
  
* * *

