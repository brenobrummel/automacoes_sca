from selenium.webdriver import Firefox
import pyautogui as pt
import time

pt.PAUSE = 0.4

navegador = Firefox()
url = 'http://localhost:5173/'

def esperar(tempo):
    time.sleep(tempo)

def entrar_e_logar():
    navegador.get(url)

    usuario = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/input')
    senha = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[3]/div/input')
    botao_entrar = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/button')

    esperar(3)
    pt.hotkey('ctrl', '-')
    pt.hotkey('ctrl', '-')
    pt.hotkey('ctrl', '-')
    usuario.send_keys('7470428')
    senha.send_keys('senha123')
    botao_entrar.click()

numeros_de_ordem = [6366001, 6495934, 5692673, 3281439, 6827755, 3310728, 5273564, 4482752, 1159160, 2344736,
7311311, 1243706, 6930382, 5583796, 3361038, 1892718, 9086314, 5993913, 3259450, 2679525, 5529577, 1826861, 2567233,
5003709, 1139046, 6905095, 1382426, 8799322, 7187114, 1294170, 9889747, 1395833, 9772511, 7115047, 3231222, 2704466,
2561451, 4202825, 9959395, 7911750, 2567892, 4600554, 1171221, 7429508, 6664589, 4573296, 9026498, 4515327, 9402259,
2689763, 3028194, 5233632, 1773569, 4019720, 3917383, 9221486, 5627988, 9984747, 7851750, 3601431, 3739743, 9567300,
5462065, 5017301, 4581627, 8114932, 5651205, 8804531, 4592197, 5326569, 8568662, 2531015, 2412588, 1838963, 8848857,
3908198, 1255303, 6957390, 4598679, 9107288, 9463383, 4099967, 6198390, 9849636, 8334936, 1794325, 5811090, 6764336,
2579429, 3233556, 2596399, 8643613, 6722109, 5915818, 2943370, 2546422, 5866186, 7472038, 7018966, 8007920, 3237432,
5139274, 5834118, 9626486, 8871078, 3387440, 3114413, 7454025, 2603820, 5909296, 7080636, 9333858, 6095958, 9866959,
4407219, 2992224, 4679421, 9280858, 6066985, 6815199, 9356129, 9286625, 6926929, 2789169, 5790931, 2952817, 6812078,
2033616, 7717301, 8143047, 9741577, 6534444, 1218421, 8141985, 9724553, 3052255, 5297640, 2850035, 8670192, 3777824,
5792850, 5939121, 3093299, 1845381, 9715262, 4665156, 1655251, 8432511, 3300055, 5522355, 1721095, 7336488, 9643937,
7003881, 9383747, 4505467, 9713898, 9167001, 5191298, 3563502, 9361366, 9340535, 6259725, 7730662, 7705581, 6305016,
7395037, 6509494, 2623031, 5291330, 5475042, 3706882, 1978988, 8105186, 5676764, 1839793, 6404763, 4680910, 4691479,
8546814, 6582617, 8611731, 1036532, 9729885, 5566881, 9824064, 3763244, 1171982, 9968035, 5869256, 6433333, 5440326,
8821856, 7364924, 6609085, 5306147, 8228673, 9357765, 5669382, 7268090, 9831545, 7285034, 5156847, 7647719, 9467666,
6965174, 8843804, 3639554, 4601677, 3917328, 1922329, 7882690, 4506766, 1103538, 3204380, 4965369, 8788733, 2600806,
1927241, 2957853, 1143832, 1099353, 9010366, 3029193, 1574623, 2932487, 8451524, 2623587, 7589067, 8475685, 8906745,
2406753, 4966529, 1139001, 9555692, 2641486, 7033412, 8697879, 6846492, 4929178, 5765804, 9228109, 1938514, 6311890,
1036077, 3677393, 9435046, 4166273, 1513511, 5277902, 3906829, 6524770, 5984278, 1053304, 6820896, 6907005, 2515112,
5061431, 4884477, 2505560, 5745166, 2601052, 4500967, 3026724, 3157348, 3350712, 2536254, 6931543, 4913621, 4362252,
1387911, 3486343, 4707526, 9320755, 9647275, 9707538, 7152180, 9595879, 9969253, 2773619, 1464742, 3980398, 6902837,
1642285, 4111291, 2223850, 8881939, 2771324, 7951655, 5814975, 2321003, 1521381, 5695993, 4232437, 4862652, 3161158,
1266968, 1426536, 2806863, 4379308, 7902054, 1149941, 9292888, 8841689, 9996697, 5420127, 7126665, 1706659, 8169983,
6893532, 8610032, 5103026, 3611753, 7472405, 6784479, 1688211, 6427304, 3310196, 9103682, 1363522, 7754419, 3977334,
9112505, 8133967, 2292282, 8011678, 8281996, 3112859, 6258697, 3647330, 7989640, 3950314, 6960779, 6684025, 6153530,
5246304, 9740837, 6029535, 7848677, 4829858, 9648733, 5037868, 6181709, 3181536, 7789103, 9211842, 5806098, 9944460,
4640097, 4431211, 2495442, 3075722, 9906049, 4541889, 9470865, 3240727, 3632083, 7650555, 1544542, 4509932, 2055988,
8719600, 6982814, 6948939, 2180005, 5572759, 7074376, 7329439, 1977722, 5877341, 1256194, 5340104, 9292215, 5858419,
4367565, 9716063, 2855588, 2827104, 6808210, 6092767, 9273424, 5658545, 6517141, 5689303, 8627827, 7959896, 9538525,
8134950, 2585985, 1318799, 2991274, 8760651, 9194384, 8671971, 7131521, 1217876, 1619619, 9971522, 9072660, 9319579,
2223666]

def selecionar_foto():
    esperar(0.5)
    pt.click(x=297, y=350, clicks= 2, interval= 0.2)
    pt.click(x=260, y=188)
    pt.hotkey('enter')

def adicionar_foto():
    for indice in range(368, len(numeros_de_ordem)):
        esperar(0.2)
        pt.click(x=154, y=306)
        esperar(0.2)
        pt.hotkey('ctrl', 'a')
        pt.hotkey('backspace')

        busca_numero_de_ordem = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/div[1]/input')
        busca_numero_de_ordem.send_keys(f'{numeros_de_ordem[indice]}')

        botao_pesquisar = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/button')
        botao_pesquisar.click()

        esperar(0.5)
        pt.click(x=1795, y=410)

        botao_adicionar_foto = navegador.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div[2]/div[5]/label')
        botao_adicionar_foto.click()

        esperar(0.5)
        selecionar_foto()

        botao_confirmar = navegador.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div[3]/div[2]/button')
        botao_confirmar.click()

entrar_e_logar()

esperar(1.5)

pt.click(x=42, y=284)

esperar(1)

adicionar_foto()