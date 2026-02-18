import unittest

from Television.Television import Television


class TelevisionTest(unittest.TestCase):

    def setUp(self):
        self.television = Television()

    def test_initial_state_is_off(self):
        status = self.television.is_on
        self.assertFalse(status)

    def test_power_toggle_turns_on(self):
        status = self.television.is_on
        self.assertFalse(status)
        result = self.television.power()
        self.assertTrue(result)

    def test_power_toggle_turns_off(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.power()
        result = self.television.power()
        self.assertFalse(result)
        self.assertFalse(self.television.is_on)

    def test_that_tv_is_on(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        is_on = self.television.is_on
        self.assertTrue(is_on)

    def test_that_tv_is_off(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        self.television.turn_tv_off()
        turn_off = self.television.turn_tv_on()
        self.assertFalse(turn_off)

    def test_initial_volume_state(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.assertEqual(5, self.television.get_volume())

    def test_that_tv_is_on_and_volume_can_increase(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        self.television.increase_volume()
        self.assertEqual(6, self.television.get_volume())

    def test_that_tv_is_on_and_volume_can_reduce(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        self.television.increase_volume()
        self.television.reduce_volume()
        self.assertEqual(5, self.television.get_volume())

    def test_that_tv_is_off_and_volume_cannot_reduce(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_off()
        self.television.increase_volume()
        self.television.reduce_volume()
        self.assertEqual(self.television.volume, 5)

    def test_that_tv_is_off_and_volume_cannot_increase(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_off()
        self.television.increase_volume()
        self.television.increase_volume()
        self.assertFalse(self.television.is_on)
        self.assertEqual(self.television.volume, 5)

    def test_tv_is_on_and_volume_cannot_exceed_maximum_volume(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        for count in range(0,111):
            self.television.increase_volume()
        self.assertEqual(self.television.volume, 100)

    def test_that_tv_is_on_and_channel_increase(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        self.television.channel_up()
        self.assertTrue(self.television.is_on)
        self.assertEqual(self.television.get_channel(), 2)

    def test_that_tv_is_off_and_channel_cannot_increase(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.channel_up()
        self.assertFalse(self.television.is_on)
        self.assertEqual(self.television.get_channel(), 1)

    def test_that_channel_reduces(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        self.television.channel_down()
        self.assertTrue(self.television.is_on)

    def test_tv_is_on_and_volume_cannot_exceed_maximum_channel(self):
        status = self.television.is_on
        self.assertFalse(status)
        self.television.turn_tv_on()
        for count in range(0,111):
            self.television.channel_up()
        self.assertEqual(self.television.channel, 50)




if __name__ == '__main__':
    unittest.main()