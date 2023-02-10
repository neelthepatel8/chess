package sensorcomp;

/**
 * The type Atmospheric sensor.
 */
public class AtmosphericSensor implements ISensor {

  private double currentValue;
  private double lastValue;

  /**
   * Instantiates a new Atmospheric sensor.
   */
  public AtmosphericSensor() {
    this.currentValue = this.lastValue = 0;
  }

  /**
   * Instantiates a new Atmospheric sensor.
   *
   * @param value the value
   */
  public AtmosphericSensor(double value) {
    this.currentValue = value;
    this.lastValue = 0;
  }

  @Override
  public double takeNewReading() {
    this.lastValue = this.currentValue;
    // this.currentValue = Math.random() * 100 / 3;
    this.currentValue = SensorData.currentReading();
    return this.currentValue;
  }

  @Override
  public double lastReading() {
    return this.lastValue;
  }

  /**
   * Initialize with.
   *
   * @param value the value
   */
  protected void initializeWith(double value) {
    this.currentValue = lastValue = value;
  }
}
