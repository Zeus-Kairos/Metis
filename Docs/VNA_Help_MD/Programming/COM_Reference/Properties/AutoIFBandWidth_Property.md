##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## AutoIFBandWidth Property - Superseded

* * *

#### Description

|  This command is replaced by: [AutoCWSweepTime
Property](AutoCWSweepTime_Property.htm). In Wideband pulse mode, choose to set
the IF bandwidth automatically or manually.  
---|---  
  
####  VB Syntax

|  pulseMeas.AutoIFBandWidth = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  False \- Manually set the IFBW for the measurement. True \-  Automatically set the IFBW for the measurement.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.AutoIFBandWidth = True 'Write  
value = pulse.AutoIFBandWidth 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoIFBandWidth(VARIANT_BOOL *pVal); HRESULT
put_AutoIFBandWidth(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

