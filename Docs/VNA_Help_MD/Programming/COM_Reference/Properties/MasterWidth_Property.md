##### Write/Read

|

##### About Integrated Pulsed App  
  
---|---  
  
## PrimaryWidth Property

* * *

#### Description

| Sets the pulse width for ALL internal pulse generators. Note: On the Pulse
Setup dialog, this command is a 'Basic setting, which is intended to be used
with the 'Auto' selections set to ON.  
---|---  
  
####  VB Syntax

| pulse.PrimaryWidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseMeasurementControl Object](../Objects/PulseMeasControl_Object.md) (object)  
value | (Double) Pulse width in seconds.  
  
#### Return Type

| Double  
  
#### Default

| 100 microseconds  
  
#### Examples

| pulse.PrimaryWidth = 1e-3 'Write  
value = pulse.PrimaryWidth 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PrimaryWidth(double* Width); HRESULT put_PrimaryWidth(double
Width);  
  
#### Interface

| IPulseMeasurementControl2  
  
* * *

* * *

