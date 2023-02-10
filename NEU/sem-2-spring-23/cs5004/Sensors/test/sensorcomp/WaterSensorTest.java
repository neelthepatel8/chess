package sensorcomp;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

import java.util.Random;

/**
 * The type Water sensor test.
 */
public class WaterSensorTest {

  /**
   * The Sensor.
   */
  ISensor sensor;

  /**
   * Sets up.
   *
   * @throws Exception the exception
   */
  @Before
  public void setUp() throws Exception {
    sensor = new WaterSensor();
  }

  private double generateWaterLevel(double min, double max) {
    Random random = new Random();
    return random.nextDouble(min, max);
  }

  /**
   * Test water level non flood.
   */
  @Test
  public void testWaterLevelNonFlood() {
    for (int i = 0; i <= 100; i++) {
      sensor.takeNewReading();
      if (sensor.lastReading() > 0.5)
        assertFalse(((IDiscreteSensor) sensor).status());
    }
  }
}