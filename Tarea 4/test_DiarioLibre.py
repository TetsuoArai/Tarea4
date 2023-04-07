from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, os

os.system('cls')

class test_DiarioLibre(unittest.TestCase):
    def setUp(self):
        self.driverChrome = webdriver.Chrome() 
        self.open = self.driverChrome.get("https://www.diariolibre.com/")
        self.wait = WebDriverWait(self.driverChrome, 20)
        self.ruta = r"C:\Users\Lenovo\Desktop\Tarea 4\ScreenShot"

    def test_01_Buscador_de_contenido(self):
        self.open
        self.Buscador_de_contenido = self.driverChrome.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[2]/div/img[1]')
        self.Buscador_de_contenido.click()
        self.Buscador_de_contenido = self.driverChrome.find_element(By.ID, 'search-input')
        self.Buscador_de_contenido.send_keys("ITLA")

        #primera captura
        test01_img_1 = "test_01_Buscador_de_contenido_img_1.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test01_img_1)

        self.Buscador_de_contenido = self.driverChrome.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[2]/div/form/input[2]')
        self.Buscador_de_contenido.click()
        time.sleep(10)

        #segunda captura
        test01_img_2 = "test_01_Buscador_de_contenido_img_2.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test01_img_2)


    def test_02_Inicio_sesion(self):
        self.open
        self.Inicio_sesion = self.driverChrome.find_element(By.ID, 'amiDlbtn')
        self.Inicio_sesion.click()
        self.Inicio_sesion = self.driverChrome.find_element(By.ID, 'login_correo')
        self.Inicio_sesion.send_keys("20212135@itla.edu.do")
        self.Inicio_sesion = self.driverChrome.find_element(By.ID, 'login_pass')
        self.Inicio_sesion.send_keys("20212135")

        #primera captura
        test02_img_1 = "test_02_Inicio_sesion_img_1.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test02_img_1)

        self.Inicio_sesion = self.driverChrome.find_element(By.XPATH, '/html/body/div[11]/div/div/div[1]/form/input[3]')
        self.Inicio_sesion.submit()
        time.sleep(14)

        #segunda captura
        test02_img_2 = "test_02_Inicio_sesion_img_2.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test02_img_2)     
    
    def test_03_Visualizar_noticias_Ultima_Hora(self):
        self.open
        self.Noticias_UltimaHora = self.driverChrome.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[2]/ul/li[3]/a')
        self.Noticias_UltimaHora.click()
        time.sleep(5)

        #primera captura
        test03_img_1 = "test_03_Visualizar_noticias_Ultima_Hora_img_1.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test03_img_1)
    
    def test_04_Acceder_menu_diferentes_secciones(self):
        self.open
        self.MenuSecciones = self.driverChrome.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[1]/div/img')
        self.MenuSecciones.click()
        time.sleep(5)

        #primera captura
        test04_img_1 = "test_04_Acceder_menu_diferentes_secciones_img_1.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test04_img_1)
    
    def test_05_visualizar_una_noticia(self):
        self.open
        self.VerNoticia = self.driverChrome.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[2]/div/img[1]')
        self.VerNoticia.click()
        self.VerNoticia = self.driverChrome.find_element(By.ID, 'search-input')
        self.VerNoticia.send_keys("ITLA")

        #primera captura
        test05_img_1 = "test_05_visualizar_una_noticia_img_1.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test05_img_1)

        self.VerNoticia = self.driverChrome.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[2]/div/form/input[2]')
        self.VerNoticia.click()

        #segunda captura
        test05_img_2 = "test_05_visualizar_una_noticia_img_2.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test05_img_2) 

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/section[1]/div/div/div[1]/div[3]/div[1]/article/div[1]/div[2]/h2/a')))
        self.VerNoticia = self.driverChrome.find_element(By.XPATH, '/html/body/div[7]/section[1]/div/div/div[1]/div[3]/div[1]/article/div[1]/div[2]/h2/a')
        self.VerNoticia.click()
        time.sleep(15)

        #tercera captura
        test05_img_3 = "test_05_visualizar_una_noticia_img_3.png"
        self.driverChrome.save_screenshot(self.ruta + "/" + test05_img_3) 

    def tearDown(self):
        self.driverChrome.close

if __name__ == '__main__' :
    unittest.main() 