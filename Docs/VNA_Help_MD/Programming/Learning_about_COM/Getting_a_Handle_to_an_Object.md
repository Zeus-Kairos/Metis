# Getting a Handle to an Object

* * *

The following are discussed in this topic:

  * [What Is a Handle](Getting_a_Handle_to_an_Object.md#handle)
  * [Declaring an Object Variable](Getting_a_Handle_to_an_Object.md#declare)
  * [Assigning an Object Variable](Getting_a_Handle_to_an_Object.md#assign)
  * [Navigating the Object Hierarchy](Getting_a_Handle_to_an_Object.md#nav)
  * [Getting a Handle to a Collection](Getting_a_Handle_to_an_Object.md#handle)

[Other Topics about COM Concepts](Learning_about_COM.md)

### What Is a Handle

In SCPI programming, you must first select a measurement before changing or
reading settings. With COM, you first get a handle to the object (or
collection) and refer to that object to change or read its settings. The
following analogy illustrates this:

A CAR could be called an object. More precisely, CAR is a class of objects.
For example, one of the properties of the CAR class is "Color". You can read
(by looking) or set (by painting) the color property of A car object. In other
words, you can only read or set properties of a specific car object; not the
entire car class. Therefore, to read or set a property, you need to get "a
handle", or an instance of the object.

This process is also called "accessing an object", "getting an instance of an
object", "returning an object". or "referring to an object". You can have
handles to many instances of an object at the same time.

### Accessing VNA Objects

The VNA Application object is the highest object in the VNA object model
hierarchy. Because of that, it is the only object that must be 'created'
before it, or any other objects, can be accessed and used. During the creation
process, the application object is assigned to a variable name, or handle.
Throughout your program, that object is used by referring to that variable.
All VNA objects can be assigned to a variable, and subsequently referred to,
in this same manner.

The following example shows how to create the VNA Application object, as well
as illustrate the general steps of get a handle to an object.

There are two steps in the process of getting a handle to analyzer objects:

  1. Declaring a Variable

  2. Assigning an Object to the Variable

### 1\. Declaring a Variable

Note: The examples in these topics use the Visual Basic Programming Language.
See the short section regarding [Visual Basic
syntax.](COM_Fundamentals.htm#vb)

Use the Dim statement or one of the other declaration statements (Public,
Private, or Static) to declare a variable. The type of variable that refers to
an object must be a Variant, an Object, or a specific type of object. Some
programming languages, such as VBScript and Keysight VEE, do not allow you to
specify variable types.

The following examples ALL declare the variable VNA. Each subsequent statement
is more specific than the previous:

  * Dim pna 'Variant data type.

  * Dim pna As Object 'Object data type.

  * Dim pna As AgilentPNA835x.Application ' Specific Application type

  * Dim pna As AgilentPNA835x.IApplication ' Interface type

  1. If you use a variable without declaring it first, the data type of the variable is Variant. If you don't care about using automatic type checking, and willing to run code less efficiently, this method is very safe and is useable on all programming environments.

  2. If you know the specific object type, and your programming environment allows it, you can declare the variable as an object.

  3. Declaring a specific object type provides automatic type checking (Intellisense), faster code, and improved readability.

  4. Declaring the interface is the most specific way and is beneficial when developing code for multiple firmware revisions. [Learn more about Interfaces.](PNA_Automation_Interfaces.md)

### 2\. Assigning an Object to a Variable

To assign an object instance to a variable, use the Set keyword before the
object variable that was declared previously. In the following line of code,
we SET the current AgilentPNA835x Application to "pna".

Set pna = AgilentPNA835x.Application

As mentioned earlier, the AgilentPNA835x object is unique because it is the
highest level of object in the VNA object model hierarcy. Therefore, we must
use the CreateObject keyword with the (classname,server name) parameters.

  * The classname for the analyzer object is always "AgilentPNA835x.Application".

  * To find your analyzer's server name, see [View or change full computer name](../../S0_Start/ComputerProperties.md#computerName)

The following statements create an instance of the Analyzer object.

Dim pna AS AgilentPNA835x.Application  
Set pna = CreateObject("AgilentPNA835x.Application", "Analyzer46")

Note: These statements will start the VNA application if it is not already
running on your instrument.

### Navigating the Object Hierarchy

Once an instance of the VNA Application is "created", you access all of the
VNA objects by navigating the object hierarchy. Navigating the object model
hierarchy can be tricky. In addition, you also need to know how to refer to a
specific instance of that object. For example, if you have three measurements
present on the VNA, how do you refer to the channel 1 measurement? Each object
on the VNA Object Model image is linked to an object page. At the top of each
object page is a Description section and another called "Accessing the ...
Object".  These sections together explain how to navigate the VNA hierarchy to
access a specific instance of that object.

From the previous discussion, you may think that you must always declare and
assign variables to an object before setting or reading its properties. While
this method is best for objects that you will continue to reuse, such as a
measurement, it is not always necessary. You can also refer to an object
directly.

The [TriggerSetup](../COM_Reference/Objects/TriggerSetup_Object.md) object,
which is a child of the Application object. Because we will only need to refer
to this object once to set a couple of properties, and it is easy to access,
we will refer to it directly. From the previous example, we already have a
handle to the Application object in the variable VNA. The following example
uses [Visual basic 'dot" notation](COM_Fundamentals.md#obj) to refer to the
TriggerSetup object, and then the Scope property.

pna.TriggerSetup.Scope = naChannelTrigger

By referring to the TriggerSetup object directly, we must type the same path
whenever we refer to properties on the TriggerSetup object. The following
method assigns the VNA.TriggerSetup object to a variable that can be reused.

Dim trig As Object  
Set trig = pna.TriggerSetup

Once created, you can treat an object variable exactly the same as the object
to which it refers. For example:

trig.Scope = naChannelTrigger  
trig.Source = naTriggerSourceInternal

### Getting a Handle to a Collection

The analyzer has several collections of objects which provide a convenient way
of setting or reading all of the objects in the collection with a single
procedure. Also, there are objects (limit lines for example) that can only be
accessed through the collection.

To get a handle to an item in a collection, you can refer to the object by
item number or sometimes by name. However, you first have to get a handle to
the collection. To assign the collection to a variable, use the same two step
process (1. declare the variable, 2. assign the variable using 'Set').

Dim meass As Measurements

Dim meas As Measurement

You can then iterate through the entire collection of measurements to read or
set properties

Sub setFormat()  
For Each meas In meass  
meas.Format = naDataFormat_LinMag  
Next  
End Sub

Or you can read or set a property on an individual object in the collection:

meass(1).Format = naLinMag

Note: Each object and collection has its own unique way of dealing with item
names, and numbers. Refer to the [Analyzer Object
Model](../COM_Reference/Objects/The_Analyzer_Object_Model.htm) for details.

* * *

