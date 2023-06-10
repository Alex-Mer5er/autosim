from selenium.webdriver.common.by import By

class PersonaForm():
    def __init__(self, familiya, imya, otchestvo, dr, seriya, nomer, vydan, dv, kp=''):
        self.familiya = familiya
        self.imya = imya
        self.otchestvo = otchestvo
        self.dr = dr
        self.seriya = seriya
        self.nomer = nomer
        self.vydan = vydan
        self.dv = dv
        self.kp = kp

    def __str__(self):
        return f"Фамилия: {self.familiya}\nИмя: {self.imya}\nОтчество: {self.otchestvo}\nДата рождения: {self.dr}\nСерия и номер паспорта: {self.seriya}  {self.nomer}\nОрган выдавший документ: {self.vydan}\nКод подразделения: {self.kp if self.kp != '' else 'Не указано'}"

    def toSimForm(self, stranica):
        first_name = stranica.find_element(By.ID, 'last_name')
        first_name.clear()
        first_name.send_keys(self.familiya)

        midle_name = stranica.find_element(By.ID, 'first_name')
        midle_name.clear()
        midle_name.send_keys(self.imya)

        last_name = stranica.find_element(By.ID, 'midle_name')
        last_name.clear()
        last_name.send_keys(self.otchestvo)

        birthday = stranica.find_element(By.ID, 'birthday')
        birthday.clear()
        birthday.send_keys(self.dr)

        doc_seriya = stranica.find_element(By.ID, 'doc_seriya')
        doc_seriya.clear()
        doc_seriya.send_keys(self.seriya)

        doc_number = stranica.find_element(By.ID, 'doc_number')
        doc_number.clear()
        doc_number.send_keys(self.nomer)

        kem_vidan = stranica.find_element(By.ID, 'kem_vidan')
        kem_vidan.clear()
        kem_vidan.send_keys(self.vydan)

        kogda_vidaly = stranica.find_element(By.ID, 'kogda_vidaly')
        kogda_vidaly.clear()
        kogda_vidaly.send_keys(self.dv)


    def send_form(self, stranica):
        send_data = stranica.find_element(By.ID, 'send-data')
        send_data.click()

