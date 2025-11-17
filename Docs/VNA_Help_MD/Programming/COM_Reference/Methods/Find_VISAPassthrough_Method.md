##### Read-only

|

##### [About VISAPassthrough](../Objects/VISAPassThrough.md)  
  
---|---  
  
# Find Method

* * *

#### Description

|  Returns a list of either VISA address strings or VISA address aliases.  
---|---  
  
#### VB Syntax

|  value = Vpassthru.Find (regex, findmode)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) \- Variable to store the list of addresses or aliases.  
Vpassthru |  (object) - A [VISAPassthrough](../Objects/VISAPassThrough.md) object  
  
#### regex

|  (String) VISA regular expressions are expressions defined by the user to find devices that have been set up on the VISA interface. The following are examples of VISA regular expressions: | Interface | Expression  
---|---  
GPIB | GPIB[0-9]*::?*INSTR  
PXI | PXI?*INSTR  
VXI | VXI?*INSTR  
GPIB-VXI | GPIB-VXI?*INSTR  
GPIB and GPIB-VXI | GPIB?*INSTR  
All VXI | ?*VXI[0-9]*::?*INSTR  
ASRL | ASRL[0-9]*::?*INSTR  
All | ?*INSTR or ?*  
  
Note that using "INSTR" in the VISA regular expression finds "instruments." To
search all interfaces, use "?*".  
  
#### findmode

|  (enum as NAVISAFindMode) \- Find mode determines the type of return values.
Choose from: 0 \- naAddresses: return VISA address names 1 \- naAliases:
return VISA address aliases Note: The list of aliases may have less‒or
more‒entries than the list of addresses because not all addresses will have
aliases, and one address can have more than one alias.  
  
#### Return Type

|  Variant  
  
#### Default

|  Address  
  
#### Examples

|  value=Vpassthru.Find("?*",1) 'Finds list of aliases  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Find(string reg_expression, enum NAVISAFindMode)  
  
#### Interface

|  IVISAPassthrough

