##### Write/Read

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Item Property

* * *

#### Description

|  Add or change a name-value pair in the Cal Set, or read the value
associated with a name. After editing,
[Save](../Methods/Save_CalSet_Method.md) the CalSet to the VNA.

### About Name-Value pairs

A Cal Set name-value pair is a general purpose data structure that maps a name
to a value. This property allows you to associate a name with a value. Then,
using this same property, you can read the value using the name. For example,
one of the items added by the VNA firmware to every Cal Set is named 'Created
By'. The value attached to this item is the name of the VNA App that created
the Cal Set. When an SMC cal is performed, you can query the Cal Set for the
'Create By' item, and it will return 'Scalar Mixer/Converter'. The same query
on an NFx channel returns 'Noise Figure Converters'. Warning \- Do NOT change
the name or value of any Items that you did NOT create. Otherwise, the VNA
firmware may behave unpredictably.

### See Also

[EnumerateItems Method](../Methods/EnumerateItems_Method.md) [RemoveItem
Method](../Methods/RemoveItem_Method.htm)  
---|---  
  
#### VB Syntax

|  CalSet.Item (name) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A [Cal Set](../Objects/CalSet_Object.md) object  
name |  (String) - Name of the name-value pair.  
value |  (Variant) - Can be an integer, float, double, string, or a single-dimensioned array of integer, float, double, string.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Example

|  ' Create the VNA object Dim pna Set pna =
CreateObject("AgilentPNA835x.Application") ' Get a handle to the calsets
collection Dim calsets Set calsets = pna.GetCalManager.calsets ' Get a handle
to the cal set to be edited Dim MyCalSet Set MyCalSet =
calsets.Item("CalSet_1") ' Add a name-value pair(item) to MyCalSet
MyCalSet.Item("MyItem")=15 ' Save the edited Cal Set to the VNA MyCalSet.Save
' Loop thru the name-value pairs in the Cal Set Dim CSetItems CSetItems =
MyCalSet.EnumerateItems for i=lbound(CSetItems) to Ubound(CSetItems) ' List
the item names in MyCalSet Dim name name = CSetItems(i) wscript.echo name '
List the value for each item name Dim value value = myCalSet.Item(name)
wscript.echo value Next ' Delete the new name-value pair
MyCalSet.RemoveItem("MyItem")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Item( BSTR name, VARIANT *value); HRESULT put_Item( BSTR name,
VARIANT value);  
  
#### Interface

|  ICalSet6

