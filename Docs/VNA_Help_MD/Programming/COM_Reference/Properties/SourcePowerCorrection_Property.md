##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## SourcePowerCorrection Property

* * *

#### Description

|  Sets source power correction ON or OFF for a specific source port on this
channel, or returns the current ON or OFF state of correction for that source
port.  
---|---  
  
####  VB Syntax

|  chan.SourcePowerCorrection (srcPort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object)  A Channel object  
srcPort |  (long integer)  Source port for which to set or return the ON or OFF state of source power correction. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](../Methods/GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (boolean) False  Turns source power correction OFF for the source port. True  Turns source power correction ON for the source port.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False - Source power correction will turn correction ON  
  
#### Examples

|  chan.SourcePowerCorrection(1) = False 'Write  
calOnPort2 = chan.SourcePowerCorrection(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePowerCorrection(VARIANT_BOOL bState); HRESULT
get_SourcePowerCorrection(VARIANT_BOOL *bState);  
  
#### Interface

|  IChannel  
  
* * *

