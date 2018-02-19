from selenium import webdriver
import unittest

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
        self.fail('Finish the test')

        # Marry เลือกแท็บ “ร้านนั่งอ่านหนังสือ”

        # Marry กับเพื่อนของเธอต้องการร้านที่ใกล้ที่สุด จึงกดปุ่ม “ใกล้สุด”

        # Marry จะใช้อินเตอร์เน็ต เธอต้องการ Wi-Fi จึงกดปุ่มร้านที่มี “Wi-Fi”

        # Marry กับเพื่อนของเธอขับรถไป จึงต้องการที่จอดรถด้วย จึงกดปุ่มร้านที่มี “ที่จอดรถ”

        # พวกเธอได้ร้านที่ต้องการแล้ว ต้องการจะดูข้อมูล จึงกดปุ่มดูข้อมูลร้านค้า

        # พวกเธอจะไปร้านนี้ จึงกดเลือกว่า “ไปร้านนี้” เว็บจึงนำทางไปที่นั่นผ่านแผนที่

        # Marry และเพื่อนของเธอถึงที่หมายโดยปลอดภัย และได้ออกจากหน้าเว็บไป

if __name__ == '__main__':
    unittest.main(warnings='ignore')
