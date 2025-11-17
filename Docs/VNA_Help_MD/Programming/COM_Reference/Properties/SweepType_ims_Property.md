##### Write/Read

|

##### [About IMSpectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## SweepType Property (IMSpectrum Opt S93087A/B)

* * *

#### Description

| Sets and returns the type of sweep for an IMSpectrum measurement.  
---|---  
  
####  VB Syntax

| ims.SweepType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims | An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value | (Enum as NAIMSSweepType) - Choose from:

  * 0 - naIMSLinearSpan When Tracking is enabled, allows tuning the Response Settings (receiver) to any values within the frequency range of the VNA. When Tracking is NOT enabled also allows setting the Stimulus (sources) to any values within the frequency range or the VNA.
  * 1 - naIMSSecondOrderSpan  The receiver is tuned to view the 2nd order products (f2-f1 and f1+f2) of the main tones that are currently specified in Stimulus Settings. When Tracking is enabled, the main tones are specified in the Swept IMD channel.
  * 2 - naIMSThirdOrderSpan  The receiver is tuned to view the 3rd order products (2f1 -f2 and 2f2-f1) of the main tones that are currently specified in Stimulus Settings. When Tracking is enabled, the main tones are specified in the Swept IMD channel.
  * 3 - naIMSNthOrderSpan The frequency range is set to N * DeltaF. This algorithm will NOT tune the receivers to see the EVEN order products.

  
  
#### Return Type

| Enum  
  
#### Default

| 3 - naIMSNthOrderSpan  
  
#### Examples

| ims.SweepType = naIMSNthOrderSpan 'Write  
swptyp = ims.SweepType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SweepType(tagNAIMSSweepType* pVal)  
HRESULT put_SweepType(tagNAIMSSweepType newVal)  
  
#### Interface

| IMSpectrum  
  
* * *

