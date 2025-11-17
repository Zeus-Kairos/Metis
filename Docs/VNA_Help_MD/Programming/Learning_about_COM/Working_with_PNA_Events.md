# Working with Events

* * *

  * [What are Events?](Working_with_PNA_Events.md#ev)

  * [Using the Analyzer's Events](Working_with_PNA_Events.md#using)

  * [Event ID's](Working_with_PNA_Events.md#ids)

  * [Filtering Events](Working_with_PNA_Events.md#filter)

  * [List of Events](Working_with_PNA_Events.md#list)

  * [Out of Range Errors](Working_with_PNA_Events.md#range)

  * [Troubleshooting Problems with Events](Working_with_PNA_Events.md#prob)

See Also

[Events Example](../COM_Example_Programs/COM_Events_Example.md)

[Errors and the SCPIStringParser
Object](../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

[Other Topics about COM Concepts](Learning_about_COM.md)

### What are Events?

Windows applications work from user-initiated events such as mouse moves and
mouse clicks. A mouse-click produces an event that the programmer can either
ignore or "handle" by providing an appropriate subroutine like this:

Sub DoThis_onClick  
Perform something  
End Sub

If this subroutine were in your program and the mouse-click event occurs on
your PC, it would generate a "Callback" to the client and interrupt whatever
it was doing and handle the event.

A more practical example of an event in the analyzer is Limit test. If limit
test is on and the measurement fails, the analyzer produces a '"Limit-failed"
event. If the measurement passed, the analyzer produces a "Limit-succeeded"
event.

The Analyzer has a very sophisticated Event structure. Your program CAN be
notified when one or more events occur. However, it may not be necessary.

For example, the analyzer has an event that will notify your program when a
sweep is complete. A simpler alternative is to use a synchronous command which
waits for the sweep to complete.

sync = True  
app.ManualTrigger sync  
chan.StartFrequency = 4.5E6

This would NOT work if you want the controller to do other things while
waiting, like setup a power meter or sort some data. In this case you would
like a "callback" from the analyzer to let your program know that the sweep
has completed. For an example of this see [Events
Example](../COM_Example_Programs/COM_Events_Example.htm).

Another reason to use events is when you want to be notified of several
conditions when they occur, such as errors or source unlock conditions. It
would not be practical to routinely poll these conditions while executing your
program.

* * *

### Using Events

If you decide to use the COM events to get a callback, your program must do
two things:

1\. Subscribe to events:

All events in the analyzer are a child of the Application object through the
INetworkAnalyzerEvents Interface. You must tell the Application object that
you are interested in receiving event callbacks. This process is called
subscription.

In Visual Basic, this is done by including "WithEvents" in the declaration
statement. The declaration below dimensions an Application object (myPNA) and
subscribes to the events produced by the Application.

Dim WithEvents myPNA as AgilentPNA835x.Application

In C++, this is a bit more involved. You must queryInterface for the
IconnectionPointContainer interface, locate the InetworkAnalyzerEvents
interface via a call to FindConnectionPoint and call Advise().

2\. Implement the Event Handler

When an event occurs, the Application object will "callback" to the client
through the InetworkAnalyzerEvents interface.

In VB, click on the object window (upper left pane). Find the Application
object and click it. The event interfaces will appear in the upper right pane.
As you click on them, VB supplies the first line of code. You fill in the rest
of the handler routine to service the event. The following is an example of a
event handler subroutine.

Note: In C++, you must type the callback.

Private Sub OnChannelEvent( eventID as Variant, channelNumber as Variant)  
Select Case (eventID)  
Case naEventID_CHANNEL_TRIGGER_COMPLETE:  
GetData( channelNumber )  
Case naEventID_CHANNEL_TRIGGER_ABORTED:  
MsgBox( "Hey don't touch the front panel!")  
End Select  
End Sub

When the trigger is complete, the application object "fires" the event by
making a callback to the event handler Sub OnChannelEvent().

* * *

### Event IDs

3 |  3 |  2 |  2 |  2 |  2 |  2 |  2 |  2 |  2 |  2 |  2 |  1 |  1 |  1 |  1 |  1 |  1 |  1 |  1 |  1 |  1 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
1 |  0 |  9 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |  0 |  9 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |  0 |  9 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |  0  
Sev |  C |  R |  Facility |  Code  
  
* * *

### Filtering Events

There are over 140 different events that you subscribe to when you "Dim
WithEvents..." (or the equivalent in your programming language). Monitoring
all of these conditions slows the speed of the analyzer significantly. The
following methods allow you to filter the events so that you only monitor
specific conditions.

  * [AllowEventMessage](../COM_Reference/Methods/AllowEventMessage_Method.md) \- monitor a specific event

  * [AllowAllEvents](../COM_Reference/Methods/AllowAllEvents_Method.md) \- monitor ALL events

  * [DisallowAllEvents](../COM_Reference/Methods/DisallowAllEvents_Method.md) \- monitor NO events

  * [AllowEventCategory](../COM_Reference/Methods/AllowEventCategory_Method.md) \- monitor specific event categories (discussed later)

  * [AllowEventSeverity](../COM_Reference/Methods/AllowEventSeverity_Method.md) \- monitor events having one or more of the following severity levels associated with them.

Code |  Severity Enumeration  
---|---  
00 |  naEventSeveritySUCCESS - the operation completed successfully  
01 |  naEventSeverityINFORMATIONAL - events that occur without impact on the measurement integrity  
10 |  naEventSeverityWARNING - events that occur with potential impact on measurement integrity  
11 |  naEventSeverityERROR - events that occur with serious impact on measurement integrity  
  
* * *

### List of Events

The following is a list of categories and the general types of events they
include. Click the link view the event details.

Category Enumeration |  Callback  
---|---  
naEventCategory_PARSER |  [OnSCPIEvent](../COM_Reference/Events/OnSCPIEvent.md)  
naEventCategory_MEASURE |  [OnMeasurementEvent](../COM_Reference/Events/OnMeasurementEvent.md)  
naEventCategory_CHANNEL |  [OnChannelEvent](../COM_Reference/Events/OnChannelEvent.md)  
naEventCategory_HW |  [OnHardwareEvent](../COM_Reference/Events/OnHardwareEvent.md)  
naEventCategory_CAL |  [OnCalEvent](../COM_Reference/Events/OnCalEvent.md)  
naEventCategory_USER |  [OnUserEvent](../COM_Reference/Events/OnUserEvent.md)  
naEventCategory_DISPLAY |  [OnDisplayEvent](../COM_Reference/Events/OnDisplayEvent.md)  
naEventCategory_GENERAL |  [OnSystemEvent](../COM_Reference/Events/OnSystemEvent.md)  
  
Note: Use the
[MessageText](../COM_Reference/Properties/Message_Text_Method.md) Method to
get a text message describing the event.

* * *

### Out of Range Errors

When you attempt to set a value on an active function that is beyond the range
(min or max) of the allowable values, the analyzer limits that value to an
appropriate value (min or max) and sets the function to the limited value.
From the front panel controls this is visually evident by the limited value in
the edit box or by the annotation on the display. An example would be
attempting to set the start frequency below 300kHz. The edit control doesn't
allow the number to fall below 300kHz.

When the automation user programs a setting (such as start frequency below the
allowable limits) the same behavior takes place. The analyzer accepts the
limited value. However, in order to learn what setting took place, you have to
read the HRESULT.

All automation calls return HRESULTs. By default the HRESULT returned when an
overlimit occurs is S_NA_LIMIT_OUTOFRANGE. This value is a success code,
meaning that bit 31 in this 32 value is 0. Programmers should check the return
code from all automation calls to determine success or failure.

Some C++ macros (like SUCCEEDED(hr) or FAILED(hr) ) only check bit 31. So if
you are interested in trapping this outOfRange error you will have to check
for S_NA_LIMIT_OUTOFRANGE explicity.

Alternatively, you can configure the analyzer to report outOfRange conditions
with an error code. Use the method:
App.[SetFailOnOverRange](../COM_Reference/Methods/SetFailOnOverRange_Method.md)
(true). With this method set TRUE, any overrange error will return
E_NA_LIMIT_OUTOFRANGE_ERROR.

This method is provided for the benefit of VB clients. VB users can't detect
specific success codes because the VB runtime strips off the HRESULT and only
raises a run time error if bit 31 is set, indicating a fail code.

* * *

### Troubleshooting Problems with Callbacks

When you do callbacks, the client PC becomes the server and the analyzer
(server) becomes the client. Callbacks can only take place when both server
and client are in the same workgroup or in the same domain. See [Configure for
COM](Configure_for_COM-DCOM_Programming.htm).

