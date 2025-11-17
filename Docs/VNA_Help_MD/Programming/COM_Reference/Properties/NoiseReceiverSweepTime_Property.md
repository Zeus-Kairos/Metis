##### Read-only

|

##### [About NoiseFigure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseReceiverSweepTime Property

* * *

#### Description

|  Returns the APPROXIMATE time the channel will take to make one noise
receiver sweep given the current setup. This, along with the sweep time for a
standard receiver measurement and the following calculations, can tell you how
long a single sweep would take so that you can set an appropriate "timeout"
in your program. Use [Sweep Time Property](Sweep_Time_Property.md) to perform
the standard sweep time query, shown as SSwpTime below. To calculate the total
sweep time: Noise Figure on amplifiers (Vector Correction ON):

  * 2*SSwpTime + X*NoiseReceiverSweepTime
  * Where X = the number of noise receiver impedance state sweeps. (Default is 4).

Noise Figure on converters (NFX) correction on - increased number of sweeps
due to extra mixer sweeps and source pulling:

  * 4*SSwpTime + X*NoiseReceiverSweepTime (without source pulling)
  * 8*SSwpTime + X*NoiseReceiverSweepTime (with source pulling)
  * Where X = the number of noise receiver impedance state sweeps. (Default is 4).

Note: The number of sweeps to perform a noise measurement is annotated at the
bottom of the Noise Figure screen.  
---|---  
  
####  VB Syntax

|  swpTime = NF.NoiseReceiverSweepTime  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
swpTime |  Variable to store the returned sweep time value (in seconds).  
NF |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  swpTiime = NF.NoiseReceiverSweepTime()  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseReceiverSweepTime (Double* SwpTime);  
  
#### Interface

|  INoiseFigure3  
  
* * *

