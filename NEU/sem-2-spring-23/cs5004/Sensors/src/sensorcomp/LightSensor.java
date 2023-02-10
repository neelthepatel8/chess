package sensorcomp;

/**
 * The type Light sensor.
 */
public class LightSensor implements IDiscreteSensor {
  private boolean onOff;

  /**
   * Instantiates a new Light sensor.
   */
  public LightSensor() {
    this.onOff = false;
  }

  @Override
  public boolean status() {
    return this.onOff;
  }

  @Override
  public void flipStatus() {
    this.onOff = !this.onOff;
  }

  public void setStatus(boolean value) {
    this.onOff = value;
  }
}
