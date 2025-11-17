##### Write/Read

|

##### [About Receiver
Overload](../../../System/Preferences.htm#SourceOFFOverload)  
  
---|---  
  
## RFOffOnReceiverOverload Property

* * *

#### Description

|  Set and return whether to turn source power OFF when a receiver is
overloaded.  
---|---  
  
####  VB Syntax

|  pref.RFOffOnReceiverOverload = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True Turn OFF source power to ALL ports when a receiver is overloaded. False Power remains ON when a receiver is overloaded.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.RFOffOnReceiverOverload = True 'Write  
value = pref.RFOffOnReceiverOverload 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RFOffOnReceiverOverload (VARIANT_BOOL* preference);  
HRESULT put_RFOffOnReceiverOverload (VARIANT_BOOL val)  
  
#### Interface

|  IPreferences12  
  
* * *

