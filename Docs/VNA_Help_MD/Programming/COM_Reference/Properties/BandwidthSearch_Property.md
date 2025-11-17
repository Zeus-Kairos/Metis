##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
# BandwidthSearch Property

* * *

#### Description

|  Sets the bandwidth search preference to start a bandwidth or notch search
in either peak or marker mode.  
---|---  
  
####  VB Syntax

|  pref.BandwidthSearch = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Enum) \- Choose from: 0 - searchPeak \- Search starts at the maximum y-value of the full sweep of data. 1 - searchMarker \- Search starts at the x and y position of the active marker.  
  
#### Return Type

|  Enum  
  
#### Default

|  searchPeak  
  
#### Examples

|  pref.BandwidthSearch = 1 'Write  
bwsearchmode = pref.BandwidthSearch 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthSearch(enum BandwidthSearchMode preference)  
HRESULT get_BandwidthTarget(enum BandwidthSearchMode* preference)  
  
#### Interface

|  IPreferences18

