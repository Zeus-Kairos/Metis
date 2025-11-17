##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## PortPhaseParameter Property

* * *

#### Description

|  Sets and reads the receivers to be used to measure the phase of the
sources. The phase measurement will be the difference between these two
receivers. Select the receivers based on your application. You are responsible
to make sure that your DUT configuration routes the signals of interest to the
correct receivers. Otherwise, the phase will not be properly controlled. On
the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Control Receiver setting.  
---|---  
  
####  VB Syntax

|  DIQ.PortPhaseParameter (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
port |  (String) Source port name. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of valid source ports.  
value |  (String) Phase parameter using the following syntax: rCont/rRef Where:

  * rCont is the receiver used to measure the controlled source.
  * rRef is the receiver used to measure the reference source.

Only logical receiver notation (a1,b1, etc) is available. [Learn
more](../../../S1_Settings/Measurement_Parameters.htm#RecNotation). Enclose
the entire parameter in quotes.  
  
#### Return Type

|  String  
  
#### Default

|  Depends on <port>  
  
#### Examples

|  oDIQ.PortPhaseParameter("port 1") = "a1/a3"  
Value = oDIQ.PortPhaseParameter("port 2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortPhaseParameter(BSTR port, BSTR* PortPhaseParameter);
HRESULT put_PortPhaseParameter(BSTR port, BSTR PortPhaseParameter);  
  
#### Interface

|  IDIQ  
  
* * *

