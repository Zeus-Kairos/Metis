##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage1Frequency Property

* * *

#### Description

|  Sets and returns the Numerically Controlled Oscillator (NCO) frequency of
the Stage 1 filter. This command is only used when [FilterMode
Property](FilterMode_Property.htm) is set to Manual.  
---|---  
  
####  VB Syntax

|  spm4.Stage1Frequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
value |  (Double) Stage 1 Frequency. Min value= 0 Hz Stage 1 Frequency. Min value= 0 Hz With DSP 4 versions, Max value= 15 MHz. With DSP 5 versions, Max value = 38 MHz. [Learn more about DSP versions.](../../../S0_Start/HelpAbout.md#DSPchanges) Or programmatically use [MinimumIFFrequency Property](MinimumIFFrequency_Property.md) and [MaximumIFFrequency Property](MaximumIFFrequency_Property.md) to determine the range of settable values.  
  
#### Return Type

|  Double  
  
#### Default

|  Nominal IF Frequency. [Learn
more](../../../IFAccess/IF_Path_Configuration.htm#IFFrquencies)  
  
#### Examples

|  spm4.Stage1Frequency = 9E6 'Write  
mode = spm4.Stage1Frequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage1Frequency(double *val); HRESULT
put_Stage1Frequency(double val);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

  

