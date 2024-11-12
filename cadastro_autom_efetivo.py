from selenium.webdriver import Firefox
from pyautogui import hotkey
import time
import random

navegador = Firefox()
url = 'http://localhost:5173/'

def entrar_e_logar():
    navegador.get(url)

    usuario = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/input')
    senha = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[3]/div/input')
    botao_entrar = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/button')

    esperar(5)
    hotkey('ctrl', '-')
    hotkey('ctrl', '-')
    hotkey('ctrl', '-')
    usuario.send_keys('1234567')
    senha.send_keys('senha123')
    botao_entrar.click()

def esperar(tempo):
    time.sleep(tempo)

def gerar_numero(inicio, final):
    return random.randint(inicio, final)

def cadastro_efetivo_automatico(inicio, final):
    for indice in range(inicio, final):
        esperar(1)
        cadastrar_efetivo = navegador.find_element('xpath', '//*[@id="root"]/div/div[2]/div[1]/button')
        cadastrar_efetivo.click()

        campo_numero_de_ordem = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[1]/input')
        campo_numero_de_ordem.send_keys(f'{numeros_de_ordem[indice]}')

        campo_nome_completo = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[2]/input')
        campo_nome_completo.send_keys(f'{nomes[indice]} {sobrenomes[indice]}')

        campo_nome_de_guerra = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[3]/input')
        campo_nome_de_guerra.send_keys(f'{sobrenomes[indice]}')

        numero1 = gerar_numero(3, 16)
        campo_posto = navegador.find_element('xpath', f'/html/body/div/div/div[3]/div[2]/div[1]/div[4]/select/option[{numero1}]')
        campo_posto.click()

        numero2 = gerar_numero(2, 14)
        campo_unidades = navegador.find_element('xpath', f'/html/body/div/div/div[3]/div[2]/div[1]/div[5]/select/option[{numero2}]')
        campo_unidades.click()

        nome_email = sobrenomes[indice]
        campo_email = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[2]/div[1]/input')
        campo_email.send_keys(f'{nome_email.lower()}@fab.mil.br')

        campo_situacao = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/select/option[2]')
        campo_situacao.click()

        campo_numero_cnh = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[2]/div[3]/input')
        campo_numero_cnh.send_keys(f'{numeros_cnh[indice - 201]}')

        campo_validade_cnh = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[2]/div[4]/input')
        campo_validade_cnh.send_keys(f'{datas[indice - 201]}')

        confirmar = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[2]/div[3]/div[2]/button[2]')
        confirmar.click()

nomes = [
    'Ana', 'Maria', 'Pedro', 'João', 'José', 'Francisco', 'Antonio', 'Carlos', 'Paulo', 'Lucas',
    'Rafael', 'Gabriel', 'Felipe', 'Gustavo', 'Vinícius', 'Fernando', 'Juliana', 'Patrícia', 'Aline', 'Larissa',
    'Marcelo', 'Roberto', 'Daniel', 'Julio', 'Eduardo', 'Luana', 'Bruna', 'Tatiane', 'Sofia', 'Isabela',
    'Claudia', 'Renata', 'Mariana', 'Jessica', 'Larissa', 'Camila', 'Cristina', 'Simone', 'Marcela', 'Viviane',
    'Tatiane', 'Amanda', 'Letícia', 'Carla', 'Raquel', 'Monique', 'Gabriela', 'Priscila', 'Kelly', 'Silvia',
    'Márcia', 'Daniele', 'Eliane', 'Cristiane', 'Joana', 'Mônica', 'Viviane', 'Eliane', 'Natália', 'Beatriz',
    'Francisca', 'Elaine', 'Tânia', 'Daniella', 'Marcia', 'Sandra', 'Sérgio', 'Tiago', 'Leandro', 'André',
    'Renan', 'Júlio', 'Vitor', 'Fábio', 'Diego', 'Wellington', 'Arthur', 'Samuel', 'Henrique', 'Guilherme',
    'Ivan', 'Murilo', 'Marcelo', 'Eduardo', 'Robson', 'Rodrigo', 'Guilherme', 'Nathália', 'Samantha', 'Caroline',
    'Ana Paula', 'Ana Clara', 'Lucas', 'Mateus', 'Bruno', 'João Pedro', 'Vinícius', 'Marcos', 'Jéssica', 'Raul',
    'José Antônio', 'Anderson', 'Luciana', 'Kátia', 'Neide', 'Sueli', 'Marilene', 'Ana Carolina', 'Silvia',
    'Igor', 'Vânia', 'Marlene', 'Michele', 'Graziele', 'Aline', 'Aline', 'Angela', 'Lúcia', 'Regina', 'Lúcia',
    'Mariana', 'Janaína', 'Joana', 'Talita', 'Gisele', 'Sandra', 'Célia', 'Edna', 'Heloísa', 'Erica', 'Janaína',
    'Fátima', 'Verônica', 'Rosa', 'Sílvia', 'Rosângela', 'Renata', 'Sônia', 'João Vítor', 'Vânia', 'Gisele',
    'Nádia', 'Débora', 'Simone', 'Aparecida', 'Tatiane', 'Tânia', 'Larissa', 'Viviane', 'Ana Beatriz', 'Fátima',
    'James', 'Mary', 'John', 'Patricia', 'Robert', 'Linda', 'Michael', 'Barbara', 'William', 'Elizabeth',
    'David', 'Jennifer', 'Richard', 'Maria', 'Joseph', 'Susan', 'Charles', 'Margaret', 'Thomas', 'Dorothy',
    'Daniel', 'Lisa', 'Matthew', 'Nancy', 'Anthony', 'Karen', 'Mark', 'Betty', 'Donald', 'Helen',
    'Steven', 'Sandra', 'Paul', 'Donna', 'Andrew', 'Carol', 'Joshua', 'Ruth', 'Kenneth', 'Shirley',
    'Kevin', 'Angela', 'Brian', 'Melissa', 'George', 'Deborah', 'Edward', 'Stephanie', 'Ronald', 'Laura',
    'Timothy', 'Rebecca', 'Jason', 'Sharon', 'Jeffrey', 'Cynthia', 'Ryan', 'Kathleen', 'Jacob', 'Amy',
    'Gary', 'Shirley', 'Nicholas', 'Angela', 'Eric', 'Anna', 'Stephen', 'Jessica', 'Larry', 'Emily',
    'Justin', 'Charlotte', 'Frank', 'Samantha', 'Scott', 'Victoria', 'Brandon', 'Alyssa', 'Benjamin', 'Grace',
    'Adam', 'Julia', 'Nathan', 'Sophia', 'Jonathan', 'Olivia', 'Samuel', 'Isabella', 'Patrick', 'Lily',
    'Alexander', 'Evelyn', 'Jack', 'Mia', 'Ryan', 'Amelia', 'Dylan', 'Harper', 'Henry', 'Aria',
    'Isaac', 'Chloe', 'Elijah', 'Ella', 'Andrew', 'Madison', 'Jameson', 'Scarlett', 'Gage', 'Zoey',
    'Christian', 'Eleanor', 'Austin', 'Layla', 'Cole', 'Riley', 'Lucas', 'Hannah', 'Owen', 'Lillian',
    'Ethan', 'Addison', 'Aiden', 'Maya', 'Jaxon', 'Aubrey', 'Grayson', 'Aurora', 'Levi', 'Nora',
    'Caleb', 'Hazel', 'Hunter', 'Camila', 'Mason', 'Peyton', 'Brayden', 'Eli', 'Jackson', 'Sarah',
    'Myles', 'Luna', 'Zachary', 'Chloe', 'Mila', 'Aiden', 'Zoey', 'Jasper', 'Riley', 'Max',
    'Stella', 'Henry', 'Ella', 'Leo', 'Ivy', 'Sebastian', 'Sophie', 'Owen', 'Aria', 'Eli',
    'Hazel', 'Axel', 'Aurora', 'Evan', 'Nova', 'Jax', 'Elena', 'Easton', 'Everly', 'Grayson',
    'Mila', 'Ryker', 'Cora', 'Elijah', 'Bella', 'Jaxon', 'Avery', 'Lincoln', 'Leah', 'Kai',
    'Harper', 'Waylon', 'Addison', 'Camden', 'Brooklyn', 'Maddox', 'Lyla', 'Jaxon', 'Olivia', 'Lucas',
    'Ava', 'Leo', 'Harrison', 'Sophie', 'Liam', 'Charlotte', 'Ethan', 'Hazel', 'Asher', 'Emily',
    'Silas', 'Zoe', 'Jace', 'Gianna', 'Ryder', 'Clara', 'Ryker', 'Lila', 'Josiah', 'Maya', 'Maria', 
    'Ana', 'João', 'Gabriel', 'Miguel', 'Arthur', 'Pedro', 'Lucas', 'Matheus', 'Davi',
    'Laura', 'Alice', 'Helena', 'Valentina', 'Sophia', 'Beatriz', 'Isabela', 'Manuela', 'Júlia', 'Luiza',
    'Rafael', 'Guilherme', 'Felipe', 'Bernardo', 'Enzo', 'Gustavo', 'Nicolas', 'Henrique', 'Samuel', 'Daniel',
    'Mariana', 'Lara', 'Camila', 'Emanuelly', 'Heloísa', 'Giovanna', 'Lívia', 'Isadora', 'Yasmin', 'Clara']

sobrenomes = [
    'Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Costa', 'Almeida', 'Lima', 'Rocha', 'Martins',
    'Araujo', 'Nascimento', 'Barros', 'Freitas', 'Carvalho', 'Ribeiro', 'Mendes', 'Gomes', 'Silveira', 'Vieira',
    'Moreira', 'Pinto', 'Cardoso', 'Teixeira', 'Gonçalves', 'Melo', 'Campos', 'Cruz', 'Dias', 'Nogueira',
    'Azevedo', 'Barbosa', 'Faria', 'Maciel', 'Lemos', 'Lima', 'Andrade', 'Borges', 'Sá', 'Pinto',
    'Cavalcante', 'Lins', 'Alves', 'Gama', 'Queiroz', 'Dantas', 'Lima', 'Moura', 'Xavier', 'Coutinho',
    'Figueiredo', 'Magalhães', 'Santos', 'Oliveira', 'Cunha', 'Amorim', 'Siqueira', 'Lima', 'Silveira', 'Moraes',
    'Batista', 'Macedo', 'Nunes', 'Sá', 'Guedes', 'Ramos', 'Mello', 'Moraes', 'Pacheco', 'Pereira',
    'Alves', 'Costa', 'Pimentel', 'Matos', 'Assis', 'Arruda', 'Monteiro', 'César', 'Ribeiro', 'Santos',
    'Neto', 'Antunes', 'Pimentel', 'Pinto', 'Feitosa', 'Chaves', 'Duarte', 'Morais', 'Pacheco', 'Pinto',
    'Silva', 'Sousa', 'Cruz', 'Gonçalves', 'Pinheiro', 'Melo', 'Barbosa', 'Viana', 'Melo', 'Freitas',
    'Araujo', 'Ferreira', 'Machado', 'Dias', 'Albuquerque', 'Borges', 'Lemos', 'Teixeira', 'Rodrigues', 'Queiroz',
    'Ribeiro', 'Lima', 'Campos', 'Cavalcante', 'Marques', 'Silva', 'Carvalho', 'Gomes', 'Pereira', 'Nunes',
    'Mendes', 'Santos', 'Melo', 'Cardoso', 'Vieira', 'Maciel', 'Xavier', 'Nogueira', 'Cunha', 'Gama',
    'Dantas', 'Costa', 'Almeida', 'Batista', 'Siqueira', 'Pinto', 'Lima', 'Silveira', 'Oliveira', 'Queiroz',
    'Arruda', 'Morais', 'Macedo', 'Lins', 'Alves', 'Dantas', 'Barros', 'Pereira', 'Nogueira', 'Teixeira',
    'Ferreira', 'Santos', 'Martins', 'Cavalcante', 'Xavier', 'Gonçalves', 'Lima', 'Freitas', 'Sá', 'Neto',
    'Campos', 'Silveira', 'Gonçalves', 'Albuquerque', 'Silva', 'Barbosa', 'Duarte', 'Cunha', 'Pereira', 'Vieira',
    'Ribeiro', 'Farias', 'Lima', 'Cavalcante', 'Maciel', 'Gama', 'Melo', 'Freitas', 'Santos', 'Mendes',
    'Pimentel', 'Queiroz', 'Figueiredo', 'Barbosa', 'Almeida', 'Farias', 'Silva', 'Ribeiro', 'Batista', 'Silva',
    'Gonçalves', 'Faria', 'Xavier', 'Costa', 'Siqueira', 'Mendes', 'Dantas', 'Maciel', 'Teixeira', 'Melo',
    'Silveira', 'Pinto', 'Santos', 'Sousa', 'Ribeiro', 'Lima', 'Cunha', 'Ferreira', 'Martins', 'Queiroz',
    'Lima', 'Nogueira', 'Pereira', 'Barros', 'Batista', 'Melo', 'Silveira', 'Alves', 'Santos', 'Melo',
    'Dantas', 'Ribeiro', 'Xavier', 'Siqueira', 'Oliveira', 'Nunes', 'Cardoso', 'Almeida', 'Lima', 'Teixeira',
    'Ferreira', 'Silveira', 'Santos', 'Farias', 'Queiroz', 'Lima', 'Dantas', 'Melo', 'Moraes', 'Silva',
    'Ribeiro', 'Pereira', 'Melo', 'Freitas', 'Neto', 'Costa', 'Almeida', 'Silva', 'Gomes', 'Vieira', 'Rocha',
    'Martins','Araujo', 'Nascimento', 'Barros', 'Freitas', 'Carvalho', 'Ribeiro', 'Mendes', 'Gomes', 'Vieira',
    'Moreira','Pinto', 'Cardoso', 'Teixeira', 'Gonçalves', 'Melo', 'Campos', 'Cruz', 'Dias', 'Nogueira', 'Azevedo',
    'Barbosa', 'Faria', 'Maciel', 'Lemos', 'Andrade', 'Borges', 'Sá', 'Cavalcante', 'Lins', 'Alves',
    'Gama', 'Queiroz', 'Dantas', 'Moura', 'Xavier', 'Coutinho', 'Figueiredo', 'Macedo', 'Nunes', 'Sá',
    'Guedes', 'Ramos', 'Mello', 'Pacheco', 'Arruda', 'Monteiro', 'Pimentel', 'Matos', 'Assis', 'Albuquerque',
    'Rodrigues', 'Moraes', 'Ferreira', 'Macedo', 'Marques', 'Silveira', 'Duarte', 'Melo', 'Gomes', 'Neto',
    'Antunes', 'Feitosa', 'Chaves', 'Viana', 'Morais', 'Maciel', 'Barros', 'Lima', 'Pereira', 'Neto',
    'Lima', 'Ribeiro', 'Silva', 'Cavalcante', 'Teixeira', 'Mendes', 'Oliveira', 'Siqueira', 'Queiroz',
    'Costa', 'Melo', 'Ferreira', 'Barbosa', 'Almeida', 'Dantas', 'Xavier', 'Martins', 'Santos', 'Silveira',
    'Cunha', 'Ribeiro', 'Silva', 'Barros', 'Santos', 'Sousa', 'Melo', 'Pinto', 'Gonçalves', 'Lima',
    'Pacheco', 'Alves', 'Freitas', 'Queiroz', 'Cavalcante', 'Viana', 'Borges', 'Ramos', 'Gama', 'Dantas'
    'Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Almeida', 'Pereira', 'Lima', 'Gomes',
    'Costa', 'Ribeiro', 'Martins', 'Carvalho', 'Rocha', 'Barbosa', 'Melo', 'Castro', 'Fernandes', 'Araújo',
    'Cardoso', 'Correia', 'Dias', 'Teixeira', 'Moreira', 'Cavalcanti', 'Moura', 'Campos', 'Nunes', 'Vieira',
    'Monteiro', 'Mendes', 'Freitas', 'Duarte', 'Alves', 'Machado', 'Lopes', 'Sousa', 'Ramos', 'Tavares',
    'Pinto']

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

numeros_cnh = [17614713105, 21446056145, 13805859700, 45227274939, 44525352968, 49488564950, 60783577423,
39549409892, 41161024351, 73096843594, 21977379923, 34303372438, 92032825666, 79148809700, 32379079260, 22704904141,
71765984312, 24202298654, 26682985803, 71003322493, 73564791775, 28028722771, 79858550729, 51052989963, 79110600820,
59819506966, 20653381559, 77301834350, 81053014987, 20784207907, 52968100696, 94814543423, 65299833551, 26563491850,
89005978216, 16240996948, 64800673931, 84360708663, 26367155186, 32969067938, 84206633006, 62965197662, 54000121364,
93657563173, 48890392695, 28781694992, 82011845179, 88106212608, 57224983796, 67232302859, 25832613151, 52728258211,
36962514649, 38643033391, 12885327583, 48004821108, 40344863757, 41485966245, 72580008500, 56650112414, 36337443643,
61952453606, 48687020042, 11914489006, 44269473093, 38529499100, 80807269766, 92404719472, 10968414148, 36742400996,
69345281429, 20134291705, 46369605765, 60926129188, 55446261883, 27318167410, 90763955176, 63582108562, 59189779459,
29227780038, 48973891546, 14609000398, 44282651980, 45845648988, 70118972940, 88259666957, 15776203766, 72981932252,
30919869846, 81542073195, 43012104843, 60815034166, 32957929147, 86319355795, 98212117038, 91094020158, 29228782798,
32928525663, 99558957681, 42599075993, 42880217334, 49772123411, 79742537970, 84597277347, 82803388401, 42986574007,
26080446021, 42823664404, 58249190824, 78277172187, 60059896701, 26597117786, 68552322814, 35864243898, 98478775704,
89342172746, 24508411047, 52796500931, 97529442278, 99329372661, 83123391358, 61282197176, 22051035914, 80365859832,
29731522734, 35740443761, 85129957749, 40693366588, 15641588326, 91966111459, 22377383805, 69801737544, 89845857937,
95982036688, 64364116679, 94007417338, 54071925032, 34742872354, 91711630343, 58813848116, 43570844694, 62452573470,
69138629794, 96447986992, 83545132854, 38951058071, 55194153704, 58705148977, 62378976131, 68459057323, 71079486205,
91454727408, 75736153996, 39429714260, 45079325904, 80136137687, 28670424058, 40749466551, 92629328898, 58183983286,
40951901508, 27581865050, 68287883819, 48467191754, 80657853656, 11127529672, 59275113591, 29283903795, 26662193670,
29457626613, 44099760169, 11640718476, 94012571784, 76828278889, 21624146665, 54038683338, 94169017400, 60147553287,
48022003090, 23255223094, 60589787707, 64788037507, 11886476393, 80958354824, 55941224271, 54974535937, 50269290684,
22108360224, 26468931101, 88770112756, 41658064421, 16196765688, 99519909935, 68174101244, 14757711670, 61842039095,
43469093613, 63298477941, 78590579944, 82477936997]

datas = ['13-06-2028', '25-04-2030', '11-01-2026', '28-02-2029', '18-05-2028', '06-06-2024', '06-07-2030',
'16-04-2024', '06-07-2028', '03-11-2028', '07-03-2026', '04-02-2027', '20-11-2030', '13-02-2023', '21-10-2024',
'05-02-2026', '16-12-2025', '23-10-2022', '23-12-2022', '11-09-2029', '18-09-2023', '03-11-2027', '22-03-2022',
'24-06-2026', '16-05-2025', '06-06-2025', '08-05-2030', '05-05-2030', '15-09-2023', '22-08-2028', '25-04-2028',
'07-07-2030', '19-04-2025', '15-01-2025', '23-12-2024', '05-05-2029', '13-06-2026', '18-01-2027', '17-04-2027',
'29-01-2027', '31-12-2030', '06-01-2026', '21-03-2029', '16-10-2022', '07-10-2028', '26-06-2029', '18-04-2022',
'02-07-2022', '21-02-2028', '07-10-2023', '10-05-2023', '07-04-2023', '03-03-2030', '12-11-2025', '12-10-2030',
'22-07-2024', '31-07-2027', '19-08-2027', '22-01-2024', '26-01-2024', '08-02-2027', '07-03-2025', '03-12-2030',
'02-08-2022', '23-03-2028', '14-10-2029', '16-12-2026', '15-02-2028', '08-05-2024', '07-11-2022', '28-08-2030',
'02-05-2026', '20-09-2028', '10-01-2023', '14-07-2025', '08-09-2022', '08-07-2030', '05-12-2029', '24-12-2028',
'06-11-2024', '07-08-2025', '05-02-2028', '12-02-2030', '29-09-2028', '19-01-2023', '15-06-2028', '02-10-2026',
'25-05-2024', '21-01-2030', '13-12-2028', '21-04-2027', '21-10-2025', '09-07-2024', '09-08-2030', '10-10-2029',
'08-08-2022', '10-07-2025', '13-01-2026', '03-09-2027', '08-03-2025', '18-10-2028', '26-05-2028', '02-06-2026',
'03-08-2023', '03-10-2025', '21-01-2024', '14-11-2023', '19-04-2023', '11-07-2029', '15-01-2027', '19-02-2022',
'04-10-2030', '06-11-2027', '17-10-2026', '10-09-2030', '29-07-2025', '09-09-2025', '02-05-2030', '16-05-2029',
'07-10-2022', '24-10-2025', '19-09-2027', '22-10-2026', '28-03-2023', '22-09-2027', '20-11-2023', '03-01-2030',
'13-10-2029', '14-05-2022', '11-04-2025', '21-12-2028', '31-03-2026', '30-07-2024', '02-06-2024', '23-09-2024',
'16-02-2029', '18-03-2025', '04-09-2030', '19-04-2028', '23-10-2025', '17-10-2023', '22-09-2030', '20-11-2028',
'08-07-2029', '07-10-2022', '30-12-2026', '06-08-2026', '04-09-2025', '29-09-2024', '05-02-2025', '10-03-2023',
'03-10-2025', '18-01-2025', '28-06-2029', '17-11-2029', '27-09-2029', '12-11-2025', '23-08-2030', '26-07-2025',
'25-02-2030', '17-10-2023', '06-02-2022', '20-01-2023', '26-12-2022', '14-12-2022', '14-09-2027', '21-02-2029',
'28-12-2025', '31-10-2024', '28-05-2024', '05-07-2024', '11-04-2030', '20-08-2022', '17-04-2027', '23-09-2029',
'01-10-2022', '30-07-2023', '29-11-2022', '19-11-2028', '25-05-2023', '07-04-2026', '21-03-2028', '09-01-2023',
'09-03-2026', '29-06-2030', '18-12-2023', '11-08-2023', '28-09-2025', '20-11-2026', '03-05-2027', '22-10-2028',
'19-04-2024', '23-07-2028', '11-06-2028', '17-07-2023', '06-08-2023', '15-03-2028', '30-06-2022', '19-07-2027',
'22-02-2030']

entrar_e_logar()

esperar(3)

efetivos = navegador.find_element('xpath', '//*[@id="root"]/div/div[1]/div[2]/div[2]/img')
efetivos.click()

#cadastro_efetivo_automatico()