package sensorcomp;

/**
 * The interface Discrete sensor.
 */
public interface IDiscreteSensor extends ISensor {
  /**
   * Status boolean.
   *
   * @return the boolean
   */
  boolean status();

  /**
   * Flip status.
   */
  void flipStatus();

  /**
   * Sets status.
   *
   * @param value the value
   */
  void setStatus(boolean value);

  default double lastReading() {
    return 0;
  }

  @Override
  default double takeNewReading() {
    return 0;
  }
}
