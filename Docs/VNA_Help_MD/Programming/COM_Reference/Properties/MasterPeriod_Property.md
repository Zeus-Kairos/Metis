##### Write/Read

|

##### About Integrated Pulsed App  
  
---|---  
  
## PrimaryPeriod Property

* * *

#### Description

| Sets the period for ALL internal pulse generators. This setting is equal to
1/PRF which is set with [MasterFrequency
Property](MasterFrequency_Property.htm). Note: On the Pulse Setup dialog, this
command is a 'Basic setting, which is intended to be used with the 'Auto'
selections set to ON.  
---|---  
  
####  VB Syntax

| pulse.PrimaryPeriod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseMeasurementControl Object](../Objects/PulseMeasControl_Object.md) (object)  
value | (Double) Period in seconds.  
  
#### Return Type

| Double  
  
#### Default

| 1 msec  
  
#### Examples

| pulse.PrimaryPeriod = 1e-4 'Write  
value = pulse.PrimaryPeriod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PrimaryPeriod(double* Period); HRESULT put_PrimaryPeriod(double
Period);  
  
#### Interface

| IPulseMeasurementControl2  
  
* * *

* * *

* * *

