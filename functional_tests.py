from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_radio(self):
        # Marry กำลังจะสอบปลายภาค เธอต้องการที่นั่งอ่านหนังสือกับเพื่อนของเธอ
        # Marry เข้าเว็บ Get-A.com
        self.browser.get('http://localhost:8000')
        self.assertIn('Find Place', self.browser.title)

        # Marry กับเพื่อนของเธอต้องการร้านที่ใกล้ที่สุด จึงกดปุ่ม “ใกล้สุด”
        inputbox = self.browser.find_element_by_id('id_radio')
        self.assertEqual(inputbox.get_attribute('name'), 'near')

        time.sleep(3)
        self.fail('Finish the test')
        # Marry จะใช้อินเตอร์เน็ต เธอต้องการ Wi-Fi จึงกดปุ่มร้านที่มี “Wi-Fi”

        # Marry กับเพื่อนของเธอขับรถไป จึงต้องการที่จอดรถด้วย จึงกดปุ่มร้านที่มี “ที่จอดรถ”

        # พวกเธอได้ร้านที่ต้องการแล้ว ต้องการจะดูข้อมูล จึงกดปุ่มดูข้อมูลร้านค้า

        # พวกเธอจะไปร้านนี้ จึงกดเลือกว่า “ไปร้านนี้” เว็บจึงนำทางไปที่นั่นผ่านแผนที่

        # Marry และเพื่อนของเธอถึงที่หมายโดยปลอดภัย และได้ออกจากหน้าเว็บไป

if __name__ == '__main__':
    unittest.main(warnings='ignore')
