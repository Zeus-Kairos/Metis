##### Read only

## Exists Method

* * *

#### Description

| Returns whether or not the specified Cal Set exists on the VNA.  
---|---  
  
####  VB Syntax

| calsets.Exists (string)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calsets | A [Calsets](../Objects/CalSets_Collection.md) (collection)  
string | (String) Name or GUID of the Cal Set enclosed in quotes.  
  
#### Return Type

| Boolean True \- Cal Set exists False \- Cal Set does NOT exist  
  
#### Default

| Not Applicable  
  
#### Examples

| dim check  
check=calsets.Exists ("MyCalset")  
or  
check=calsets.Exists ("7C4EEA5E-40D2-4D70-A048-33BFFE704163")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT Exists(BSTR nameOrGuid, VARIANT_BOOL * exists)  
  
#### Interface

| ICalSets2  
  
* * *

* * *

