package sensorcomp;

/**
 * The interface Sensor.
 */
public interface ISensor {
  /**
   * Take new reading double.
   *
   * @return the double
   */
  double takeNewReading();

  /**
   * Last reading double.
   *
   * @return the double
   */
  double lastReading();
}
