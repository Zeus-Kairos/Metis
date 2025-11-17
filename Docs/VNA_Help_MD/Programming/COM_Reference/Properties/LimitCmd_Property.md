##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
# LimitCmd Property

* * *

#### Description

| Sets and returns a user-defined command string that is used to set the DC
limit of the external DC source. The actual limit value is set using either
the [VoltageLimit](VoltageLimit.md) (voltage) or
[CurrentLimit](CurrentLimit.md) (current). The limit command is sent to the
external DC source at the beginning of a sweep for each channel. The firmware
automatically selects the current or voltage limit value depending on the
external DC source type.  
---|---  
  
####  VB Syntax

| extDC.LimitCmd = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC | An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value | (String) User-defined command name: Include {%f} in the command string which will be substituted by the actual limit value.  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| extDC.LimitCmd = "myDCDevice","Limit Command {%f}" 'Write  
value = extDC.LimitCmd 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_LimitCmd (BSTR* cmd) HRESULT put_LimitCmd (BSTR cmd)  
  
#### Interface

| IExternalDCDevice4  
  
* * *

