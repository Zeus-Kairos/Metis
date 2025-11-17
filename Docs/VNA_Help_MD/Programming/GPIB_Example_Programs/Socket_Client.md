# Socket Client

* * *

The following C# example demonstrates how to send SCPI commands to the VNA via
a TCP socket connection and how to use a TCP 'control' connection. If the
command is a query, the program will read the instrument's response. You can
add or replace the SCPI commands in this program with your own.

[Learn how to enable Sockets communication on the
VNA.](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#LANSCPI)

For both of the following methods, first copy the example text below into a
Notepad file and name it SocketClient.cs.

### To run using Microsoft Visual Studio 2003 or 2005

  1. From the Visual Studio File menu, select New, then Project.

  2. In the New Project window, select the following items (noting the location of the file folder it is creating for you) then click OK.

  * Project Type: Visual C#

  * Template: Console Application

  * Project Name: SocketClient

  1. Copy SocketClient.cs into the folder that was created in the previous step.

  2. In the Solution Explorer window pane, right-click Class1.cs (if Visual Studio 2003) or Program.cs (if Visual Studio 2005). Select Delete to delete that file.

  3. In the Solution Explorer, right-click SocketClient , and select Add, then Existing Item .

  4. Browse to select SocketClient.cs and click OK.

You should then be able to build the project, and test the resulting
SocketClient.exe from a command prompt (shell) window.

### To run using Mono

Mono is a cross-platform version of .NET. You can download a free version of
Mono at [http:/www.mono-project.com](http://www.mono-project.com). Once
downloaded and installed:

  1. Run the Mono command prompt (shell) window.

  2. Navigate to the directory where the example SocketClient.cs is stored.

  3. Type: MCS SocketClient.cs (builds the .exe and saves in that same folder.)

  4. Type mono SocketClient.exe <VNA name or IP address>

This example was compiled and tested successfully with Mono version 1.1.13. It
was run on a PC using the Red Hat version 9.0 distribution of the Linux
operating system. It was also run on a PC using Windows XP. This program has
not been tested with other versions of Mono, or on other operating systems.

### To run with Keysight T&M Toolkit

Keysight T&M Toolkit 2.0 is the first version to support communication using
Sockets.

Use the following to address the Sockets port: TCPIP0::<VNA name or IP
address>::5025::SOCKET

using System; using System.Net; using System.Net.Sockets; // This C# "Console
Application" example program demonstrates SCPI // communication with an
Keysight TCP socket-enabled instrument that // supports socket "control
connections" (such as VNA network analyzers, // which have support for control
connections in their socket // implementation as of VNA Firmware A.08.33.01).
namespace CSharpSocketClient { /// <summary> /// The class supporting the main
entry point for the application. /// </summary> class MainClass { static
AsyncCallback m_pCallbackFunc; static string m_AsyncReply; /// <summary> ///
The main entry point for the application. /// </summary> [STAThread] static
int Main(string[] args) { try { if (args.Length != 1) { Console.WriteLine("");
Console.WriteLine("Usage -- with Microsoft's .NET runtime:");
Console.WriteLine("SocketClient servernameoraddress");
Console.WriteLine("Example: SocketClient 192.168.0.1"); Console.WriteLine("");
Console.WriteLine("Usage -- with Mono's (www.mono-project.com) .NET
runtime:"); Console.WriteLine("mono SocketClient.exe servernameoraddress");
Console.WriteLine("Example: mono SocketClient.exe 192.168.0.1"); return 1; }
string server = args[0]; Int32 port = 5025; // default socket port number for
the VNA // Create the primary client socket instance Socket client = new
Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp); //
Get the DNS IP addresses associated with the instrument. // (if 'server'
string contains the IP address rather than DNS name, this still works)
IPHostEntry hostInfo = Dns.Resolve(server); IPAddress[] IPaddresses =
hostInfo.AddressList; if (IPaddresses.GetLength(0) < 1) return 1; // Create an
endpoint to use for opening the socket connection IPEndPoint endpoint1 = new
IPEndPoint (IPaddresses[0], port); // Open the connection to the server
instrument client.Connect(endpoint1); if(!client.Connected) return 1; // Query
the instrument's ID string. string id = Parse(client, "*IDN?"); // Clear the
instrument's Status Byte Parse(client, "*CLS"); // Enable for the OPC bit (bit
0, which has weight 1) in the instrument's // Event Status Register, so that
when that bit's value transitions from 0 to 1 // then the Event Status
Register bit in the Status Byte (bit 5 of that byte) // will become set.
Parse(client, "*ESE 1"); // Enable for bit 5 (which has weight 32) in the
Status Byte to generate an // SRQ when that bit's value transitions from 0 to
1. Parse(client, "*SRE 32"); // Ask the instrument for the number of a port on
which a 'control' // socket connection can be opened. string controlPortNumStr
= Parse(client, "SYSTem:COMMunicate:TCPip:CONTrol?"); Int32 controlPortNum =
System.Convert.ToInt32(controlPortNumStr); // Create the client "control
connection" socket instance Socket controlClient = new
Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp); //
Create an endpoint to use for opening the control connection IPEndPoint
endpoint2 = new IPEndPoint (IPaddresses[0], controlPortNum); // Connect to the
server instrument via the port number that was returned by the instrument.
controlClient.Connect(endpoint2); if(!controlClient.Connected) return 1; //
Start the control connection listening for an SRQ message.
BeginListeningForAsyncReply(controlClient); // Now send a preset command to
the instrument, accompanied by '*OPC' such // that when that operation is
complete an SRQ event will be generated // which posts the Status Byte message
on the control connection. Parse(client, "SYSTem:PRESet;*OPC"); // Normally at
this point you would want to have your program do other things // right here
until the SRQ callback occurs, instead of just idling here waiting // for it.
do {} while (m_AsyncReply == null); // Now that the SRQ has occurred, we can
issue a Device Clear via the control connection. Parse(controlClient, "DCL");
// The instrument will respond back with "DCL" (and linefeed character
appended // on the end) via the control connection when it has finished
processing the // Device Clear request. Note that this 'Response' method uses
the synchronous // form of 'Receive', so it could potentially time out if the
instrument were // to take a long time to process the Device Clear. So
alternatively the // 'BeginListeningForAsyncReply' could be used for this
instead of 'Response'. string deviceClearResponse = Response(controlClient);
// Close both of the socket client sessions. controlClient.Close();
client.Close(); } catch (ArgumentNullException e) {
Console.WriteLine("ArgumentNullException: {0}", e); } catch (SocketException
e) { Console.WriteLine("SocketException: {0}", e); } Console.WriteLine("/n
Press Enter to continue..."); Console.Read(); return 0; } static string
Parse(Socket client, string command) { // Translate the passed command into
ASCII and store it as a Byte array. Byte[] data =
System.Text.Encoding.ASCII.GetBytes(command);  // Send the command to the
socket-enabled instrument. client.Send(data); // Has to be followed by a
linefeed character as terminator. Byte[] lf = {(Byte)'/n'}; client.Send(lf);
Console.WriteLine("Sent: {0}", command);  // If the message was a query
(involved a question mark), receive the instrument response. if
(command.IndexOf("?") >= 0) { return Response(client); } return ""; } static
string Response(Socket client) { // Buffer to store the response bytes. // For
simplicity of this example, we allocate just for a 256-byte maximum //
response size. Byte[] data = new Byte[256]; // Read the batch of response
bytes. Int32 byteCount = client.Receive(data); // String to store the response
ASCII representation. string responseData =
System.Text.Encoding.ASCII.GetString(data, 0, byteCount);
Console.WriteLine("Received: {0}", responseData); return responseData; }
static void BeginListeningForAsyncReply(Socket client) { if (m_pCallbackFunc
== null) { m_pCallbackFunc = new AsyncCallback(OnMessageReceived); }
SocketPacket socPkt = new SocketPacket(); socPkt.thisSocket = client; // Start
asynchronously listening for a response from this client IAsyncResult result =
client.BeginReceive (socPkt.data, 0, socPkt.data.Length, SocketFlags.None,
m_pCallbackFunc, socPkt); } class SocketPacket { public Socket thisSocket; //
For simplicity of this example, we allocate just for a 256-byte maximum //
response size. public Byte[] data = new Byte[256]; } static void
OnMessageReceived(IAsyncResult asyn) { SocketPacket socPkt =
(SocketPacket)asyn.AsyncState ; Int32 byteCount =
socPkt.thisSocket.EndReceive(asyn); m_AsyncReply =
System.Text.Encoding.ASCII.GetString(socPkt.data, 0, byteCount);
Console.WriteLine("Received: {0}", m_AsyncReply); }  } }  
---  
  
* * *

