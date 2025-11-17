##### Read only

|

##### [About Windows File
Locations](../../../S0_Start/Windows_File_Locations.htm)  
  
---|---  
  
## DirectoryPath Property

* * *

#### Description

| Returns a the path name to the systems documents folders on the VNA.  
---|---  
  
####  VB Syntax

| value = cap.DirectoryPath (enum)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value | (String) - Variable to store the returned directory path.  
cap | A [Capabilities](../Objects/Capabilities_Object.md) (object)  
enum | Type of file. Choose from: 0 - naDirectoryState - This is the location for the storage of state files. 1 - naDirectoryApplication - This is the location of the VNA firmware executable files. 2 - naDirectorySupport - This is the location of private support files for the VNA firmware. [See these file locations](../../../S0_Start/Windows_File_Locations.md).  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| value = cap.DirectoryPath(naDirectoryState) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DirectoryPath(enum DirectoryPathType directoryPathType,BSTR*
path);  
  
#### Interface

| ICapabilities10  
  
* * *

