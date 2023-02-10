package sensorcomp;

/**
 * The type Tire pressure sensor.
 */
public class TirePressureSensor implements ISensor {
  private final static double HG_TO_PSI = 2.036;
  private AtmosphericSensor sensor;

  /**
   * Instantiates a new Tire pressure sensor.
   */
  public TirePressureSensor() {
    this.sensor = new AtmosphericSensor();
  }

  /**
   * Instantiates a new Tire pressure sensor.
   *
   * @param clone the clone
   */
// copy constructor
  public TirePressureSensor(TirePressureSensor clone) {
    this.sensor = new AtmosphericSensor(clone.lastReading());
  }

  @Override
  public double takeNewReading() {
    return this.sensor.takeNewReading() / HG_TO_PSI;
  }

  @Override
  public double lastReading() {
    return this.sensor.lastReading() / HG_TO_PSI;
  }

  /**
   * Reset tpm.
   */
  public void resetTPM() {
    this.sensor = new AtmosphericSensor(36 * HG_TO_PSI);
  }
}
