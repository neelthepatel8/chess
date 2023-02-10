package sensorcomp;

/**
 * The type Sensor data.
 */
public class SensorData {
  // public static double currentReading() {
  //  return Math.random() * 100 / 3;
  //}

  private static double[] readings = {0.1, 0.4, 0.0, 0.51, 0.5, 0.7, 0.0, 2.2, 1.0};
  private static int counter = 0;

  /**
   * Current reading double.
   *
   * @return the double
   */
  static public double currentReading() {
    int value = counter;
    counter++;
    if (counter >= readings.length) {
      counter = 0;
    }
    return readings[value];
  }

  /**
   * Reset.
   */
  public static void reset() {
    counter = 0;
  }
}
