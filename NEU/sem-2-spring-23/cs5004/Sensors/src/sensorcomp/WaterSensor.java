package sensorcomp;

/**
 * The type Water sensor.
 */
public class WaterSensor implements IDiscreteSensor {

  private boolean flooding;
  private double currentValue;
  private double lastValue;


  /**
   * Instantiates a new Water sensor.
   */
  public WaterSensor() {
    this.flooding = false;
    this.currentValue = this.lastValue = 0;
  }

  @Override
  public boolean status() {
    return this.flooding;
  }

  @Override
  public void flipStatus() {
    this.setStatus(!this.flooding);
  }

  @Override
  public void setStatus(boolean value) {
    this.flooding = value;
  }

  @Override
  public double takeNewReading() {
    this.lastValue = this.currentValue;
    this.currentValue = SensorData.currentReading();

    double FLOOD_THRESHOLD = 0.5;
    this.setStatus(this.currentValue > FLOOD_THRESHOLD);

    return this.currentValue;
  }

  @Override
  public double lastReading() {
    return this.lastValue;
  }
}
