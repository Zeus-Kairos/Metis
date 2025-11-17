# Local Lockout (LLO) Message

* * *

Normally, a GPIB instrument is put in remote mode by asserting the Remote
Enable (REN) GPIB line. At that time, all front panel keys (except the Local
key) are locked to prevent user interaction.

Sending the LLO message over the GPIB further locks out the keyboard, mouse,
and Local key during execution of your GPIB program. The syntax of the LLO
message depends on the GPIB driver you are using. Consult your GPIB driver
software users manual.

The VNA requires these two actions to occur in order:

  1. Controller sends the LLO (Local Lockout) message

  2. Controller asserts the REN (Remote Enable) GPIB line

The VNA will then go into remote mode with full lockout capability.

This feature is also supported using SICL over LAN.

Use the
[LocalLockoutState](../COM_Reference/Properties/LocalLockoutState_Property.md)
COM command when using TCPIP/LAN.

* * *

