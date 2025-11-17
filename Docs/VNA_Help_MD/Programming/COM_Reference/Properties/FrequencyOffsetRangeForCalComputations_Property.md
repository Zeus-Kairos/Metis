##### Write/Read

|  
---|---  
  
## FrequencyOffsetRangeForCalComputations Property

* * *

#### Description

|  Specifies the FOM frequency range to use when performing calibration.  
---|---  
  
####  VB Syntax

|  pref.FrequencyOffsetRangeForCalComputations = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Enum as NACalFOMRange) \- Choose from: 0 - naCalFOMRangeAuto \- All other calibration situations. 1 - naCalFOMRangePrimary \- Used for calibrating at the mmWave frequencies when NOT using a test set. [Learn more.](../../../IFAccess/mmWave_Measurement_w_No_Test_Set.md)  
  
#### Return Type

|  Enum  
  
#### Default

|  naCalFOMRangeAuto  
  
#### Examples

|  pref.FrequencyOffsetRangeForCalComputations = naCalFOMRangePrimary 'Write  
calPref = pref.FrequencyOffsetRangeForCalComputations 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyOffsetRangeForCalComputations(tagNACalFOMRange * val);
HRESULT put_FrequencyOffsetRangeForCalComputations((tagNACalFOMRange val);  
  
#### Interface

|  IPreferences10  
  
* * *

