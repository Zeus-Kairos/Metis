##### Read-only

|

##### [About LFE](../../../IFAccess/Low_Frequency_Extension/Overview.md)  
  
---|---  
  
# HasLowFrequencyExtension Property

* * *

#### Description

| Returns whether or not the VNA has the low frequency extension (LFE)
installed. [Learn
more](../../../IFAccess/Low_Frequency_Extension/Overview.htm).  
---|---  
  
####  VB Syntax

| value = chan.HasLowFrequencyExtension  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value | (boolean) False \- LFE is not installed. True \- LFE is installed.  
cap | [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

| Not applicable  
| hasLFE = cap.HasLowFrequencyExtension 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_HasLowFrequencyExtension(VARIANT_BOOL* hasLFE);  
  
#### Interface

| ICapabilities16  
  
* * *

