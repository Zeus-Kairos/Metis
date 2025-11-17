##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## Channels Property

* * *

#### Description

| Sets and returns the list of channels to be calibrated during the Cal All
session.  
---|---  
  
####  VB Syntax

| calAll.Channels = chans  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll | A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
chans | (Variant) Array of channel numbers to be calibrated, separated by commas. These channels must already exist.  
  
#### Return Type

| Variant  
  
#### Default

| The existing channels  
  
#### Examples

| calAll.Channels = Array(1,2,3) 'sets channels to be cal'd chans =
calAll.Channels 'returns the channel numbers to be cal'd  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Channels (VARIANT selectedChannels); HRESULT put_Channels
(VARIANT* selectedChannels);  
  
#### Interface

| ICalibrateAllChannels  
  
* * *

* * *

