##### Write/Read

|

##### [About Power Level](../../../S1_Settings/Power_Level.md)  
  
---|---  
  
# PowerSpinResolution Property

* * *

#### Description

| Sets and returns the resolution of the front panel knob when it is used to
adjust Source Power manually.  
---|---  
  
####  VB Syntax

| disp.PowerSpinResolution = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
disp | A [Display](../Objects/Display_Object.md) (object)  
value | (Double) \- Power level knob resolution. The range of acceptable values is 0.01 to 100.   
  
#### Return Type

| Double  
  
#### Default

| 0.1  
  
#### Examples

| app.disp.PowerSpinResolution = 0.01 'Write - Every tick of the front panel
knob will change the Power Level by 0.01 dBm.  
resolution = app.disp.PowerSpinResolution 'Read - Get the current knob
resolution.  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PowerSpinResolution(double* resolution) HRESULT
put_PowerSpinResolution(double resolution)  
  
#### Interface

| IDisplay

