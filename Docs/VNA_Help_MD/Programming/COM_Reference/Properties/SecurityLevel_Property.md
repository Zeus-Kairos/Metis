##### Write/Read

|

##### [About Security Level](../../../System/Frequency_Blanking.md)  
  
---|---  
  
## SecurityLevel Property

* * *

#### Description

|  Controls the display of frequency information on the VNA screen and
printouts.  
---|---  
  
####  VB Syntax

|  app.SecurityLevel value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (enum NASecurityLevel) -Choose from: 0 - naNoSecurity ALL frequency information is displayed. 1 - naLowSecurity NO frequency information is displayed. Frequency information can be redisplayed using the Security Setting dialog box or this command. 2 - naHighSecurity LOW setting plus [GPIB console](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.md#console) is disabled. Frequency information can be redisplayed ONLY by performing a Preset, recalling an instrument state with None or Low security settings, or using this command. 3 - naExtraSecurity HIGH setting plus:

  * [ASCII data saving](../../../S5_Output/SaveRecall.md#ASCII) is disabled. Same method to redisplay frequency information as HIGH setting.
  * [Mixer setup files](../../../Applications/MixerConverter_Setup.md#AboutMxr) (*.mxr) can NOT be saved.

  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 - None  
  
#### Examples

|  app.SecurityLevel = naLowSecurity 'Write  
level = app.SecurityLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NASecurityLevel(tagNASecurityLevel *level);  
HRESULT put_NASecurityLevel(tagNASecurityLevel level);  
  
#### Interface

|  IApplication4  
  
* * *

