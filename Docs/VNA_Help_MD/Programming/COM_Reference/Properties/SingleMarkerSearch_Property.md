##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
# SingleMarkerSearch Property

* * *

#### Description

|  Set and return whether to use one marker for marker search. Enabled
behavior:

  * Only one marker is used for bandwidth, notch, PNOP, and PSAT marker searches. The points of interest are marked with a notational UI element, i.e. a small triangle.
  * Bandwidth, notch, PNOP, and PSAT marker searches are always tracking. Tracking cannot be disabled.
  * One basic search and one advanced search may be set per marker.
  * The advanced search is enabled until the user disables the search or a multi-peak or multi-target search is executed.

Disabled behavior:

  * Bandwidth, notch, PSAT, and PNOP marker searches use multiple markers.
  * One advanced marker search is allowed per trace.
  * A marker may only perform a basic search or be part of an advanced search. Not both.
  * If an advanced marker search is enabled on a trace and then the user performs a basic search, the advanced search is automatically disabled.
  * Advanced searches may enable or disable tracking. Only one search may be tracked.

  
---|---  
  
####  VB Syntax

|  pref.SingleMarkerSearch= bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (boolean)  
False \- Disable single marker search. True - Enable single marker search.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.SingleMarkerSearch = True 'Write  
prefer = pref.SingleMarkerSearch 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SingleMarkerSearch(VARIANT_BOOL *mkrState)  
HRESULT put_SingleMarkerSearch(VARIANT_BOOL mkrState)  
  
#### Interface

|  IPreferences18

