##### Write/Read

|

##### About Integrated Pulsed App  
  
---|---  
  
## PrimaryFrequency Property

* * *

#### Description

| Sets the pulse repetition frequency (PRF) for ALL internal pulse generators.
This setting is equal to 1/period which is set with [PrimaryPeriod
Property](MasterPeriod_Property.htm) Note: On the Pulse Setup dialog, this
command is a "Basic" setting, intended to be used with the 'Auto' selections
set to ON.  
---|---  
  
####  VB Syntax

| pulse.PrimaryFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
value | (Double) PRF in Hz.  
  
#### Return Type

| Double  
  
#### Default

| 1 kHz  
  
#### Examples

| pulse.PrimaryFrequency = 1e4 'Write  
value = pulse.PrimaryFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PrimaryFrequency(double* value); HRESULT
put_PrimaryFrequency(double value);  
  
#### Interface

| IPulseMeasurementControl2  
  
* * *

* * *

