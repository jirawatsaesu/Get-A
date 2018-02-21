from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_find_a_place(self):
        # Marry กำลังจะสอบปลายภาค เธอต้องการที่นั่งอ่านหนังสือกับเพื่อนของเธอ
        # Marry เข้าเว็บ Get-A.com
        self.browser.get('http://localhost:8000/')

        # Marry เลือกแท็บ “สถานที่อ่านหนังสือ”
        place_link = self.browser.find_element_by_link_text('Place')
        self.assertEqual(place_link.get_attribute('href'), 'http://localhost:8000/place/')

        time.sleep(1)
        place_link.click()

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


    def test_can_view_a_list_of_book(self):
        # เมื่อกลับถึงบ้าน Mary อยากผ่อนคลาย ไม่รู้จะอ่านหนังสืออะไรดี จึงเข้าเว็บ Get-A.com อีกครั้ง
        self.browser.get('http://localhost:8000')

        # Marry เลือกแท็บ “หนังสือน่าอ่าน”
        book_link = self.browser.find_element_by_link_text('Book')
        self.assertEqual(book_link.get_attribute('href'), 'http://localhost:8000/book/')

        time.sleep(1)
        book_link.click()

        time.sleep(3)
        self.fail('Finish the test')
        # Marry พบเห็นหนังสือแนะนำ 2-3 เล่ม และหมวดหมู่สำหรับค้นหาหนังสือ

        # Marry เลือกหมวดหมู่ “Computer” และพิมพ์ชื่อหนังสือ “Data Structure”

        # Marry พบหนังสือชื่อ “Data Structure and Algorithm” และเห็นคะแนนหนังสือได้ 4 ดาว จาก 5 ดาว

        # Marry ได้หนังสือที่ต้องการจะอ่าน และปิดเว็บไป


if __name__ == '__main__':
    unittest.main(warnings='ignore')
