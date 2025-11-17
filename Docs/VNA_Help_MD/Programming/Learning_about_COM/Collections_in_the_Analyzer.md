# Collections in the Analyzer

* * *

Collections are a gathering of similar objects. They are a convenience item
used primarily to iterate through the like objects in order to change their
settings. Collections generally provide the following generic methods and
properties:

Item(n)  
Count  
Add(n)  
Remove(n)

where (n) represents the number of the item in the collection. Some
collections may have unique capabilities pertinent to the objects they
collect.

[Other Topics about COM Concepts](Learning_about_COM.md)

### Collections are Dynamic

A collection does not exist until you ask for it. When you request a Channels
object (see Getting a Handle to an Object /
[Collection](Getting_a_Handle_to_an_Object.md#coll)), handles to each of the
channel objects are gathered and placed in an array.

For example, if channels 2 and 4 are the only channels that exist, then the
array will contain only 2 items. The command 'channels.Count' will return the
number 2, and:

  * Channels(1) will contain the channel 2 object.

  * Channels(2) will contain the channel 4 object.

The ordering of objects within the collection should not be assumed. If you
add a channel to the previous example, as in:

Pna.Channels.Add(3)

'channels.Count' will now return 3 and:

  * Channels(1) will contain the channel 2 object.

  * Channels(2) will contain the channel 3 object.

  * Channels(3) will contain the channel 4 object.

Primarily, collections are useful for making this type of iteration possible:

Dim ch as Channel  
For each ch in pna.Channels  
Print ch.Number  
Print ch.StartFrequency  
Print ch.StopFrequency  
Next ch

As soon as this for-each block has been executed, the Channels object goes out
of scope.

* * *

