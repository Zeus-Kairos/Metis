# Effects of Accessories

* * *

Accessories in a configuration may affect the results of a device measurement.
You can choose between these analyzer features that reduce ore remove the
effects of accessories.

  * [Power Slope to Compensate for Cable Loss](Effects_Accy.md#slope)

  * [Gating to Selectively Remove Responses](Effects_Accy.md#Gate)

  * De-embedding a 2-port device (separate topic)

[Other topics about Optimizing Measurements](Optimize.md)

Power Slope to Compensate for Cable Loss

If you have a long cable or other accessory in a measurement configuration
where a power loss occurs over frequency, apply the power slope function. This
function increases the analyzer source power by a rate that you define
(dB/GHz).

  1. Press Power > Leveling & Offsets.

  2. If the slope function is not already switched on, click the button beside Slope.

  3. In the Slope box, enter the rate that you want the source power to increase over the frequency sweep.

Gating to Selectively Remove Responses

Gating is a feature in the time domain (option S93010A/B) that allows the
analyzer to mathematically remove responses. You can set the gate for either a
reflection or transmission response, but you will see different results.

  * Gating a reflection response isolates a desired response (such as a filter's return loss), from unwanted responses (such as adapter reflections or connector mismatches).

  * Gating a transmission response isolates a specific path in a multipath device that has long electrical lengths.

See [Time Domain Gating](../Time/TimeDomain.md#Gating) for more information.

* * *

