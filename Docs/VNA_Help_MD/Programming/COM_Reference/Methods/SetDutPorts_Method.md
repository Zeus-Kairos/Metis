##### Write-only

|

##### [About Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## SetDutPorts Method

* * *

#### Description

|  Sets the VNA to DUT port map for FCA measurements. Use
[DeviceInputPort](../Properties/DeviceInputPort_Property.md) and
[DeviceOutputPort](../Properties/DeviceOutputPort_Property.md) to read these
values. Changing the ports may limit your ability to use an internal second
source. If a selected port is shared by one of the sources, then that source
will not be available as an LO source. [Learn more about Internal second
sources](../../../S0_Start/Internal_Second_Source.htm).  
---|---  
  
####  VB Syntax

|  mixer.SetDUTPorts (inputPort,outputPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A [IMixer](../Objects/IMixer_Interface.md) Interface pointer to the [Meas](../Objects/Measurement_Object.md) (object)  
inputPort |  (Long) VNA port to be connected to the DUT input.

  * For SMC, choose any unused VNA port.
  * For VMC, set to 1

  
outputPort |  (Long) VNA port to be connected to the DUT output. Choose any unused port for SMC and VMC.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  1,2  
  
#### Examples

|  mixer.SetDUTPorts =2,1  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetDutPorts(long inputPort,long OutputPort);  
  
#### Interface

|  IMixer8  
  
* * *

