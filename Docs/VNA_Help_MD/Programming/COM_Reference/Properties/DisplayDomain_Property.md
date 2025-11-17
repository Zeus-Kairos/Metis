##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# DisplayDomain Property

* * *

#### Description

|  Set and read the X-axis domain type.  
---|---  
  
####  VB Syntax

|  HotS22.DisplayDomain = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
value |  (Enum as NAAxisDomainType) - Choose from:

  * 0 - naAxisFrequency Sets a linear frequency sweep that is displayed on a standard grid with ten equal horizontal divisions.
  * 1 - naAxisPower  Sets a power sweep at a single specified frequency.
  * 2 - naAxisPhase  Sets a phase sweep.
  * 3 - naAxisDCValue  Sets value of dc source.
  * 4 - naAxisPoints Sets the number of phase points.
  * 5 - TypeNum

  
  
#### Return Type

|  Enum  
  
#### Default

|  naAxisFrequency  
  
#### Examples

|  HotS22.DisplayDomain = naAxisFrequency 'Write  
value = HotS22.DisplayDomain 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DisplayDomain(tagNAAxisDomainType* value)  
HRESULT put_DisplayDomain(tagNAAxisDomainType value)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

