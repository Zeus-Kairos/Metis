# CalKit Object

* * *

### Description

The calkit object provides the properties and methods to access and modify a
calibration kit.

### Accessing a CalKit object

The active cal kit is the kit that is selected for use in Unguided
calibrations. To get a handle to the active kit, use the
[app.ActiveCalKit](../Properties/Active_Cal_Kit_Property.md) property. To
access the CalKit object for a specific cal kit, you must first make that kit
the active kit using [app.CalKitType](../Properties/CalKitType_Property.md).

The CalKit object behaves differently from other objects in that you can only
have a handle to one cal kit -- the active cal kit. Therefore, when you change
the CalKitType from either the [Application object](Application_Object.md) or
the [CalKit object](calKit_Object.md), you may also be changing the object to
which you may have other references.

For example, the following example specifies two CalKit type objects and in
turn, assigns them to two different variables: ck1 and ck2.

Dim app As AgilentPNA835x.Application  
Dim ck1 As calKit  
Dim ck2 As calKit  
  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
app.CalKitType = naCalKit_User1  
Set ck1 = app.ActiveCalKit  
ck1.Name = "My CalKit1"  
  
app.CalKitType = naCalKit_User2  
Set ck2 = app.ActiveCalKit  
ck2.Name = "My CalKit2"  
  
Print "ck1: " & ck1.Name  
Print "ck2: " & ck2.Name  

When the pointer to each of these kits is read (printed), they each have a
pointer to the last kit to be assigned to the active cal kit:

ck1: My CalKit2  
ck2: My CalKit2

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Description  
  
---|---  
[getCalStandard](../Methods/Get_Cal_Standard_Method.md) |  Returns a handle to a calibration standard for modifying its definitions.  
[GetStandardsForClass](../Methods/Get_StandardForClass_Method.md) |  Returns the calibration standard numbers for a specified calibration class.  
[SetStandardsForClass](../Methods/Set_StandardForClass_Method.md) |  Sets the calibration standard numbers for a specified calibration class  
  
### Properties

|

### Description  
  
[CalKitType](../Properties/CalKitType_Property.md) |  Sets or returns the calibration kit type to be used for calibration or for kit modification. Shared with the Application object.  
[Name](../Properties/Name_CalKit_Property.md) |  Sets and returns the name of the cal kit  
[PortLabel](../Properties/PortLabel_Property.md) |  Labels the ports for the kit; only affects the cal wizard annotation.  
[StandardForClass](../Properties/StandardForClass_Property.md) |  Superseded with Use [GetStandardForClass](../Methods/Get_StandardForClass_Method.md) and [SetStandardForClass](../Methods/Set_StandardForClass_Method.md). Maps a standard device to a cal class.  
  
### ICalKit History

Interface |  Introduced with VNA Rev:  
---|---  
ICalKit |  1.0

