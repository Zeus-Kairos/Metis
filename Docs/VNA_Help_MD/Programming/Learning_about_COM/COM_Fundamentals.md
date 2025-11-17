# COM Fundamentals

* * *

The following terms are discussed in this topic:

  * [Objects](COM_Fundamentals.md#obj)

  * [Interfaces](COM_Fundamentals.md#Interfaces)

  * [Collections](COM_Fundamentals.md#coll)

  * [Methods](COM_Fundamentals.md#method)

  * [Properties](COM_Fundamentals.md#prop)

  * [Events](COM_Fundamentals.md#events)

  * [Visual Basic Syntax](COM_Fundamentals.md#vb)

Note: The information contained in this topic is intended to help an
experienced SCPI programmer transition to COM programming. This is NOT a
comprehensive tutorial on COM programming.

[Other Topics about COM Concepts](Learning_about_COM.md)

### Visual Basic Syntax

The examples in VNA Help use Visual Basic as the programming environment for
COM, which uses 'dot' notation.

To set a property, follow the object reference with:

  * a period (.)

  * property or method

  * an equal sign (=)

  * the new value

For example:

object.property = value 'This Green text following an apostrophe (') is a
comment.

To read a property, a variable to contain the returned value is followed with:

  * an equal sign (=)

  * an object, or reference to an object

  * a period (.)

  * property

For example:

variable = object.property

To execute a method, an object, or reference to an object is followed with:

  * a period (.)

  * the method

  * a blank space

  * any required parameters

For example:

object.method parameters

Some methods return values, such as methods that return data. To return data
from a method, a variable to contain the returned data is followed with:

  * an equal sign (=)

  * an object, or reference to an object

  * a period (.)

  * the method

  * any required parameters enclosed in parenthesis

variable = object.method (parameters)

### Objects

The objects of the Network Analyzer (Application) are arranged in a
hierarchical order. The [VNA object
model](../COM_Reference/Objects/The_Analyzer_Object_Model.htm) lists the
objects and their relationship to one another.

In SCPI programming, you must first select a measurement before making
settings. With COM, you first get a handle to the object (or collection) and
refer to that object in order to change or read settings (properties).

For more information on working with objects, see [Getting a Handle to an
Object.](Getting_a_Handle_to_an_Object.htm)

### Interfaces

A COM Interface is the connection to an object. When you get a handle to an
object, you are actually using an interface to an object. This is important if
you are developing VNA code that will run on multiple code versions. For more
information, see [VNA Interfaces](PNA_Automation_Interfaces.md).

### Collections

A collection is an object that contains several other objects of the same
type. For example, the Channels collection contains all of the channel
objects.

Note: In the following examples, the collections are referred to as a
variable. Before using a collection object, you must first get an instance of
that object. For more information, see [Getting a Handle to an
Object](Getting_a_Handle_to_an_Object.htm)

Generally, items in a collection can be identified by number or by name. The
order for objects in a collection cannot be assumed. They are always unordered
and begin with 1. For example, in the following procedure, chans(1) is used to
set averaging on the first channel in the Channels collection (not necessarily
channel 1).

Sub SetAveraging()  
chans(1).AveragingFactor = 10  
End Sub

The following procedure uses the measurement string name to set the display
format for a measurement in the measurements collection.

meass("CH1_S11_1").Format = 1

You can also manipulate an entire collection of objects if the objects share
common methods. For example, the following procedure sets the dwell time on
all of the segments in the collection.

Sub setDwell()  
For Each seg In segs  
segs.DwellTime = 0.03  
Next  
End Sub

### Methods

A method is an action that is performed on an object. For example,
CreateSParameter is a method on the
[Application](../COM_Reference/Objects/Application_Object.md) object. The
following procedure uses that method to create a new S21 measurement in
channel 1 in a new window.

Sub CreatMeas  
app.CreateSParameter 1,2,1,1  
End Sub

### Properties

A property is an attribute of an object that defines one of the object's
characteristics, such as size, color, or screen location. A property can also
change an aspect of the object's behavior, such as whether the object is
visible. In either case, to change the characteristics of an object, you
change the values of its properties.

For example, the following statement sets the IF Bandwidth of a channel to 1
KHz.

Chan.IFBandwidth = 1e3

You can also read the current value of a property. The following statement
reads the current IF Bandwidth of a channel into the variable Ifbw.

Ifbw = Chan.IFBandwidth

Some properties cannot be set and some cannot be read. The Help topic for each
property indicates if you can:

  * Set and read the property (Write/Read)

  * Only read the property (Read-only)

  * Only set the property (Write-only)

### Events

A COM event is an action recognized by an object, such as clicking the mouse
or pressing a key. Using events, your program can respond to a user action,
program code, or triggered by the analyzer.

The SCPI equivalent of an event is a Service Request (SRQ).

For example:

OnChannelEvent

For more information, see [Working with the Analyzer's
Events.](Working_with_PNA_Events.htm)

* * *

