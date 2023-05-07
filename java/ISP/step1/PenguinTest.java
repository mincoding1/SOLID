import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class PenguinTest {
    @Test
    public void testItLosesFeathers() {
        Penguin penguin = new Penguin(5);
        penguin.molt();
        assertEquals(4, penguin.numberOfFeathers);
    }

    @Test
    public void testItCantActuallyFly() {
        Penguin penguin = new Penguin(5);
        assertThrows(UnsupportedOperationException.class, () -> penguin.fly());
    }

    @Test
    public void testItCanSwim() {
        Penguin penguin = new Penguin(5);
        penguin.swim();
        assertEquals("in the water", penguin.currentLocation);
    }
}
