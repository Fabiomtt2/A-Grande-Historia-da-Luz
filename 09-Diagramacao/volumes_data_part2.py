#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banco de Dados Literário, Histórico e Pedagógico — Volumes 6 a 10 (Novo Testamento)
Coleção: A Grande História da Luz — A Bíblia Ilustrada para Pequenos Exploradores
Autor: Fábio Motta e Silva (Publicação Independente / Autônoma)
Contém os roteiros completos em Dupla Camada (4-6 anos e 6-10 anos), diálogos,
reconstrução histórica do século I (Joan E. Taylor) e storyboards dos Volumes 6 a 10.
"""

VOLUMES_DATA_NT = [
    # =========================================================================
    # VOLUME 6 — UMA LUZ NASCE NO MUNDO (Nascimento, Infância e Batismo de Jesus)
    # =========================================================================
    {
        "num": 6,
        "slug": "Volume-6-Uma-Luz-Nasce-no-Mundo",
        "md_file": "Volume6_Uma_Luz_Nasce_no_Mundo_Roteiro_e_Storyboard.md",
        "title": "UMA LUZ NASCE NO MUNDO",
        "subtitle": "O menino de Nazaré e o começo de um novo tempo",
        "biblical_range": "Lucas 1–2; Mateus 1–3; Marcos 1; João 1",
        "cover_base_prefix": "vol6_capa_base_aventura",
        "hero_art_prefix": "vol6_cap2_estrela_belem",
        "intro_text": (
            "Bem-vindo ao sexto volume da coleção A Grande História da Luz! Aqui começa o Novo Testamento. Depois de séculos de espera, a Luz prometida pelos antigos profetas finalmente chegou ao mundo de uma maneira surpreendente: não num palácio de mármore, mas numa manjedoura simples em Belém!\n\n"
            "Acompanhe a jovem Maria e o artesão José, os pastores nos campos, os sábios do Oriente seguindo a Estrela, a infância de Jesus na oficina de Nazaré e o início de sua missão às margens do rio Jordão."
        ),
        "map_title": "MAPA DO SÉCULO I: NAZARÉ, BELÉM, JERUSALÉM E RIO JORDÃO",
        "archaeology_section_title": "1. ARQUEOLOGIA DA JUDEIA E DA GALILEIA NO SÉCULO I",
        "archaeology_full": (
            "• As Casas-Caverna de Belém e as Manjedouras de Pedra: No século I, muitas casas da Judeia eram construídas diante de grutas calcárias onde os animais dormiam no nível inferior, aquecendo a família. As manjedouras eram cochos retangulares esculpidos em pedra calcária!\n\n"
            "• A Aldeia Agrícola e Artesanal de Nazaré: Escavações em Nazaré revelaram casas simples de pedra, prensas de vinho e azeite e oficinas de construção (em grego, 'tekton' significava artesão tanto da madeira quanto da pedra).\n\n"
            "• O Rosto Histórico de Jesus (Estudos da Profa. Joan E. Taylor): Como judeu galileu do século I, Jesus tinha pele morena-oliva bronzeada pelo sol mediterrâneo, olhos castanhos, cabelos e barba escuros aparados, túnica de lã não tingida (haluq) e manto com franjas (tzitzit)."
        ),
        "glossary_full": (
            "• MANJEDOURA: Cocho de pedra ou madeira onde se colocava feno para alimentar ovelhas e jumentos.\n"
            "• EMANUEL: Nome hebraico anunciado pelos profetas que significa 'Deus está conosco'.\n"
            "• TEKTON (CARPINTEIRO / ARTESÃO): Profissão de José e do jovem Jesus em Nazaré, trabalhando com madeira e pedra.\n"
            "• SINAGOGA: Casa de reunião, leitura das Escrituras e oração em cada cidade judaica.\n"
            "• DISCÍPULO: Aprendiz e amigo que caminha junto com seu mestre para aprender seu modo de viver."
        ),
        "char_notes": (
            "• MARIA E JOSÉ: Jovem casal judeu galileu do século I com traços semitas autênticos, vestindo túnicas de lã e linho tecidos em tons de índigo, terracota e creme.\n\n"
            "• JESUS CRIANÇA E ADULTO: Fidelidade absoluta à reconstrução histórica e antropológica do século I (pele morena-oliva, cabelos escuros cacheados, olhar acolhedor e sereno).\n\n"
            "• OS PRIMEIROS AMIGOS PESCADORES: Simão Pedro, André, Tiago e João às margens do Mar da Galileia com redes de pesca e barcos de madeira de cedro e carvalho."
        ),
        "back_cover_synopsis": (
            "'O povo que caminhava na escuridão viu uma grande Luz!'\n\n"
            "Neste sexto volume escrito por Fábio Motta e Silva, pequenos exploradores de 4 a 10 anos descobrem a beleza histórica e espiritual do nascimento e da juventude de Jesus de Nazaré — preparando o coração para ouvir suas parábolas inesquecíveis no Volume 7!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "O SIM DE MARIA E O CORAÇÃO DE JOSÉ",
                "ref": "Base Bíblica: Lucas 1:26–56; Mateus 1:18–25",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena6_humanidade_sopro.jpg",
                "main_narrative": (
                    "Na pequena aldeia de Nazaré, nas colinas verdes da Galileia, vivia uma jovem de coração humilde e corajoso chamada Maria. Um dia, a luz mensageira do Céu brilhou em sua casa com uma notícia extraordinária: ela daria à luz o Filho prometido, que se chamaria JESUS!\n\n"
                    "— Eis aqui a serva do Senhor; cumpra-se em mim a Tua palavra! — respondeu Maria, e cantou um hino de alegria celebrando a justiça de Deus. Ao seu lado, o justo artesão José acolheu Maria e a criança com todo amor e proteção."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: O nome Jesus (Yeshua, em hebraico/aramaico) significa 'O Senhor Salva / Liberta'!",
                "seed_4_6": "Na cidadezinha de Nazaré, uma luz brilhante anunciou à jovem Maria que ela seria a mamãe de Jesus, o Salvador prometido! Maria disse 'Sim!' com o coração cheio de alegria, e o bondoso José cuidou dela com todo o carinho.",
                "explorer_dialogue": (
                    "Visitando sua prima Isabel nas montanhas da Judeia, Maria abriu os braços sob o sol da manhã e cantou o 'Magnificat':\n"
                    "— A minha alma engrandece ao Senhor, e o meu espírito se alegra em Deus, meu Salvador! Porque Ele olhou para a humildade de sua serva e estendeu a Sua misericórdia de geração em geração!"
                ),
                "arq_title": "A FONTE DE ÁGUA DE NAZARÉ",
                "arq_text": "Nazaré no século I era uma pequena vila de cerca de 400 moradores abastecida por uma única fonte de água cristalina brotando da rocha, onde as mulheres iam buscar água em cântaros de barro todos os dias.",
                "family_question": "Maria e José confiaram no plano de Deus mesmo sem entender tudo no começo. O que ajuda a sua família a caminhar unida?"
            },
            {
                "num": 2,
                "title": "A ESTRELA DE BELÉM E A CANÇÃO DOS PASTORES",
                "ref": "Base Bíblica: Lucas 2:1–20",
                "dark_mode": True,
                "art_source": "HERO_VOL6",
                "main_narrative": (
                    "Por causa de um recenseamento do império romano, José e Maria viajaram de Nazaré até Belém, a cidade de Davi. Como não havia lugar para eles na hospedaria, o pequeno Jesus nasceu num abrigo simples de pedra e foi deitado com ternura numa manjedoura.\n\n"
                    "Nos campos próximos, pastores que guardavam suas ovelhas à noite viram o céu inteiro se acender de glória dourada: 'Não tenham medo! Hoje, na cidade de Davi, nasceu o Salvador! Glória a Deus nas alturas e paz na Terra!' E correram para encontrar o bebê."
                ),
                "quick_box": "» VOCÊ PERCEBEU? Os primeiros convidados para conhecer o Rei da Luz foram pastores humildes do campo!",
                "seed_4_6": "Quando Maria e José chegaram a Belém, o bebê Jesus nasceu num lugar simples e quentinho junto aos animais e dormiu numa manjedoura! No campo, uma luz linda no céu avisou os pastores, que correram felizes para ver o recém-nascido!",
                "explorer_dialogue": (
                    "Ao entrarem na gruta iluminada pela lamparina de azeite, os pastores tiraram seus gorros de lã e ajoelharam-se diante da manjedoura de pedra:\n"
                    "— É exatamente como a Voz luminosa nos anunciou no campo! — sussurrou o pastor mais velho, emocionado, enquanto Maria guardava cada uma daquelas palavras dentro do coração."
                ),
                "arq_title": "OS CAMPOS DOS PASTORES EM BELÉM (MIGDAL EDER)",
                "arq_text": "Nos arredores de Belém pastavam os rebanhos de ovelhas que ajudavam o Templo de Jerusalém. Foi justamente a esses pastores simples que nasceu a notícia do Cordeiro da Paz!",
                "family_question": "Por que Jesus escolheu nascer num lugar tão simples e acessível, onde qualquer pessoa podia entrar sem medo?"
            },
            {
                "num": 3,
                "title": "OS SÁBIOS DO ORIENTE E OS PRESENTES REAIS",
                "ref": "Base Bíblica: Mateus 2:1–15",
                "dark_mode": True,
                "art_source": "vol2_cap1_estrelas_abraao.jpg",
                "main_narrative": (
                    "Guiados por uma estrela radiante que brilhava no céu, sábios estudiosos dos astros vieram de terras distantes do Oriente até Belém. Ao encontrarem o menino Jesus com sua mãe Maria, encheram-se de imensa alegria e abriram seus cofres com três presentes especiais: ouro, incenso perfumado e mirra.\n\n"
                    "Avisados em sonho para não voltarem ao ciumento rei Herodes, os sábios regressaram por outro caminho, e José levou Maria e o menino em segurança até o Egito, antes de retornarem para Nazaré."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Os sábios vieram de outra nação, mostrando que a Luz de Jesus brilha para todos os povos da Terra!",
                "seed_4_6": "Sábios de uma terra muito distante seguiram uma estrela brilhante no céu até encontrar o pequeno Jesus! Eles trouxeram presentes preciosos — ouro, incenso e mirra — e voltaram para casa pelo caminho da paz.",
                "explorer_dialogue": (
                    "— Vimos a Sua estrela brilhar lá no Oriente e atravessamos desertos e rios para homenageá-Lo! — disseram os sábios, entregando o ouro, o incenso aromático da Arábia e a mirra preciosa.\n"
                    "Naquela noite, José ouviu o aviso protetor da Luz e conduziu a família em segurança até que o perigo passasse."
                ),
                "arq_title": "A ROTA DO INCENSO E OS ASTRÔNOMOS DO ORIENTE",
                "arq_text": "Na antiguidade, sábios da Pérsia, Babilônia e Arábia estudavam atentamente os movimentos dos planetas e estrelas, e o incenso e a mirra eram resinas aromáticas valiosíssimas transportadas por caravanas.",
                "family_question": "Qual é o melhor presente que nós podemos oferecer hoje a quem amamos — algo que não se compra com dinheiro?"
            },
            {
                "num": 4,
                "title": "O MENINO NA OFICINA DE NAZARÉ E NO TEMPLO",
                "ref": "Base Bíblica: Lucas 2:39–52",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena7_nomes_cuidadores.jpg",
                "main_narrative": (
                    "De volta a Nazaré, o menino Jesus crescia forte, cheio de sabedoria e cercado pela graça de Deus. Na oficina com José, aprendia a trabalhar a madeira de oliveira e a pedra calcária; na sinagoga e em casa com Maria, aprendia as Escrituras e os Salmos.\n\n"
                    "Quando completou doze anos, viajou com os pais à festa da Páscoa em Jerusalém. No pátio do Templo, os mestres ficaram admirados ao ver como aquele menino galileu ouvia com atenção e fazia perguntas tão sábias e profundas!"
                ),
                "quick_box": "» VOCÊ PERCEBEU? 'E crescia Jesus em sabedoria, em estatura e em graça diante de Deus e das pessoas' (Lucas 2:52).",
                "seed_4_6": "Jesus cresceu em Nazaré ajudando José na oficina de carpintaria e brincando nas colinas com as outras crianças. Aos doze anos, em Jerusalém, ele conversou com os professores no Templo e encantou a todos com sua sabedoria!",
                "explorer_dialogue": (
                    "Sentado em roda com os doutores da Lei nos pórticos do Templo de Jerusalém, o jovem Jesus perguntava e respondia com tanta clareza que todos se maravilhavam.\n"
                    "Quando Maria e José o encontraram, ele voltou obediente com eles para Nazaré, crescendo dia após dia em amor, conhecimento e bondade."
                ),
                "arq_title": "AS ESCALINATAS DO TEMPLO DE JERUSALÉM (HULDA)",
                "arq_text": "Os largos degraus de pedra do lado sul do Monte do Templo, por onde o menino Jesus e sua família subiam nas festas de peregrinação, existem até hoje em Jerusalém!",
                "family_question": "Aos 12 anos, Jesus gostava de ouvir e fazer boas perguntas aos professores. Qual é a coisa que você mais gosta de aprender e perguntar?"
            },
            {
                "num": 5,
                "title": "A VOZ NO RIO JORDÃO E A POMBA DE LUZ",
                "ref": "Base Bíblica: Mateus 3:1–17; Marcos 1:1–11; João 1:1–14",
                "dark_mode": False,
                "art_source": "vol1_cap2_jardim_eden.jpg",
                "main_narrative": (
                    "Quando Jesus chegou aos trinta anos, seu primo João Batista preparava o coração do povo às margens do rio Jordão, convidando todos a deixarem o egoísmo para trás e começarem uma vida nova e limpa.\n\n"
                    "Jesus entrou nas águas do Jordão para ser batizado por João. Assim que subiu da água, o céu se abriu num facho resplandecente de luz dourada e safira, o Espírito desceu suave como uma pomba luminosa e a Voz do Amor eterno ecoou: 'Este é o meu Filho amado, em quem me alegro!'"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Assim como o Sopro pairava sobre as águas em Gênesis 1, no Jordão começa a Nova Criação!",
                "seed_4_6": "Quando Jesus cresceu, foi até o rio Jordão onde seu primo João Batista estava batizando o povo. Ao sair da água, o céu brilhou com uma luz linda como uma pomba branca e a Voz de Deus disse: 'Este é o meu Filho muito amado!'",
                "explorer_dialogue": (
                    "— Eu é que preciso ser batizado por você, e você vem a mim? — perguntou João Batista, admirado com a humildade de Jesus.\n"
                    "— Deixe assim agora, João — sorriu Jesus com os pés na água fresca do Jordão —, porque é bom cumprirmos juntos toda a justiça!\n"
                    "Depois disso, no silêncio do deserto, Jesus venceu todas as tentações do orgulho e do poder, escolhendo servir apenas ao Amor."
                ),
                "arq_title": "BETÂNIA ALÉM DO JORDÃO (AL-MAGHTAS)",
                "arq_text": "O local histórico do batismo às margens do baixo rio Jordão ficava exatamente na mesma região onde, séculos antes, Josué havia atravessado o rio e Elias havia se despedido de Eliseu!",
                "family_question": "Ouvir 'Você é meu filho amado!' deu força a Jesus para toda a sua missão. Como é bom ouvir e dizer 'Eu amo você' dentro de casa!"
            },
            {
                "num": 6,
                "title": "VENHAM E VEJAM! OS PRIMEIROS AMIGOS NA GALILEIA",
                "ref": "Base Bíblica: Marcos 1:16–20; João 1:35–51",
                "dark_mode": False,
                "art_source": "vol3_cap4_travessia_mar.jpg",
                "main_narrative": (
                    "Caminhando pela praia de pedrinhas do Mar da Galileia ao amanhecer, Jesus não procurou príncipes nem generais para formar sua equipe: ele chamou pescadores trabalhadores como Simão Pedro, seu irmão André, Tiago e João, que consertavam suas redes no barco.\n\n"
                    "— Venham comigo! — convidou Jesus com um sorriso luminoso. — Vocês pescam peixes, mas eu vou ensiná-los a resgatar pessoas com a rede do amor! E logo juntaram-se a eles Filipe, Natanael, Mateus e mulheres fiéis que caminhavam com o grupo."
                ),
                "quick_box": "» O QUE VOCÊ FARIA? Quando André conheceu Jesus, a primeira coisa que fez foi correr para chamar seu irmão Simão Pedro!",
                "seed_4_6": "Na beira do lago da Galileia, Jesus convidou pescadores simples — Pedro, André, Tiago e João — e muitos outros amigos para viajarem com ele espalhando boas notícias, curando os doentes e ensinando o amor de Deus!",
                "explorer_dialogue": (
                    "— Mestre, onde você mora? — perguntaram João e André, caminhando atrás de Jesus.\n"
                    "— Venham e vejam! — respondeu Jesus com hospitalidade calorosa.\n"
                    "Aquele convite simples ('Venham e vejam!') transformou pescadores comuns da Galileia nos maiores mensageiros de esperança da história humana."
                ),
                "arq_title": "O BARCO DE PESCA DA GALILEIA DO SÉCULO I",
                "arq_text": "Em 1986, durante uma seca que baixou o nível do Mar da Galileia, arqueólogos encontraram preservado na lama um barco real de pesca em madeira de cedro e carvalho datado exatamente do século I (época de Jesus e Pedro), com 8 metros de comprimento!",
                "family_question": "Jesus chamou pessoas diferentes para trabalharem juntas como uma equipe de amigos. Quais qualidades você mais admira nos seus amigos?"
            }
        ]
    },

    # =========================================================================
    # VOLUME 7 — AS HISTÓRIAS QUE JESUS CONTOU (Sermão do Monte e Parábolas)
    # =========================================================================
    {
        "num": 7,
        "slug": "Volume-7-As-Historias-que-Jesus-Contou",
        "md_file": "Volume7_As_Historias_que_Jesus_Contou_Roteiro_e_Storyboard.md",
        "title": "AS HISTÓRIAS QUE JESUS CONTOU",
        "subtitle": "Segredos do Reino em parábolas inesquecíveis",
        "biblical_range": "Mateus 5–7, 13; Lucas 10 e 15",
        "cover_base_prefix": "vol7_capa_base_aventura",
        "hero_art_prefix": "vol7_cap3_bom_samaritano",
        "intro_text": (
            "Bem-vindo ao sétimo volume da coleção A Grande História da Luz! Quando as multidões — incluindo muitas mães, pais e crianças — sentavam-se na grama das colinas da Galileia para ouvir Jesus, ele não falava palavras complicadas: ele contava histórias chamadas Parábolas!\n\n"
            "Usando sementes de trigo, passarinhos do céu, lírios do campo, uma ovelhinha fujona, um viajante socorrido na estrada e um pai de braços abertos, Jesus revelou como funciona o Reino da Luz e do Amor."
        ),
        "map_title": "MAPA DAS PARÁBOLAS: COLINAS DA GALILEIA E ESTRADA DE JERICÓ",
        "archaeology_section_title": "1. A NATUREZA E O COTIDIANO DA GALILEIA NAS PARÁBOLAS",
        "archaeology_full": (
            "• A Colina das Bem-Aventuranças (Mar da Galileia): As encostas verdes ao norte de Cafarnaum formam um anfiteatro natural acústico onde a voz de uma pessoa falando normalmente pode ser ouvida por milhares de ouvintes sentados na grama!\n\n"
            "• O Grão de Mostarda e os Lírios do Campo: Na primavera da Galileia, os campos cobrem-se de anêmonas vermelhas e lírios silvestres, e o arbusto da mostarda cresce a partir de uma sementinha de 1 milímetro até alcançar três metros de altura, abrigando os pássaros.\n\n"
            "• A Estrada de Jerusalém a Jericó: Caminho real de 27 km que descia mais de 1.000 metros entre desfiladeiros rochosos do deserto da Judeia, cenário exato da parábola do Bom Samaritano."
        ),
        "glossary_full": (
            "• PARÁBOLA: Uma história simples da vida real contada por Jesus para ensinar uma grande verdade espiritual.\n"
            "• BEM-AVENTURADOS: Pessoas profundamente felizes e abençoadas porque caminham no amor e na paz.\n"
            "• PACIFICADOR: Quem constrói pontes de paz, resolve brigas e aproxima as pessoas.\n"
            "• SAMARITANO: Morador da região da Samaria; na história de Jesus, tornou-se símbolo de quem ajuda o próximo sem preconceito.\n"
            "• PRÓDIGO: Na parábola de Lucas 15, o filho que gastou tudo longe de casa, mas foi recebido pelo pai com perdão total."
        ),
        "char_notes": (
            "• JESUS ENSINANDO NO MONTE: Segue rigorosamente o modelo histórico do século I (Profa. Joan E. Taylor): pele morena-oliva, cabelos e barba escuros aparados, túnica de lã clara (haluq), manto com franjas azuis (tzitzit) e sandálias de couro.\n\n"
            "• PERSONAGENS DAS PARÁBOLAS: O Semeador com bolsa de pano a tiracolo, o Bom Samaritano com jumento e cantil de azeite, o Bom Pastor com a ovelha nos ombros e o Pai abraçando o filho que voltou."
        ),
        "back_cover_synopsis": (
            "'Vocês são a luz do mundo! Assim brilhe a luz de vocês diante das pessoas, para que vejam as boas obras que vocês fazem!'\n\n"
            "Neste sétimo volume escrito por Fábio Motta e Silva, mergulhamos no Sermão do Monte e nas mais belas parábolas de Jesus, aprendendo sobre empatia, perdão, generosidade e confiança no cuidado do Pai!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "A LUZ DO MUNDO NO MONTE DAS OLIVEIRAS E FLORES",
                "ref": "Base Bíblica: Mateus 5:1–16; 6:9–13, 25–34",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena5_animais_jardim.jpg",
                "main_narrative": (
                    "Sentado na encosta florida acima do lago da Galileia, Jesus olhou para as famílias e anunciou as Bem-Aventuranças: 'Felizes os que têm coração humilde, os bondosos, os que têm fome de justiça e os pacificadores, porque serão chamados filhos de Deus!'\n\n"
                    "Apontando para os passarinhos no céu e os lírios coloridos do campo, ensinou a oração do Pai Nosso e disse: 'Vocês são o sal da terra e a luz do mundo! Não coloquem a lâmpada debaixo do cesto, mas no alto, para iluminar todos os que estão na casa!'"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Jesus chamou cada criança e cada discípulo de 'Luz do Mundo' (Mateus 5:14)!",
                "seed_4_6": "No alto de uma colina cheia de flores, Jesus ensinou a oração do Pai Nosso, mostrou como Deus cuida dos passarinhos e das florzinhas do campo e disse uma coisa linda: 'Vocês são a luz do mundo! Brilhem fazendo o bem a todos!'",
                "explorer_dialogue": (
                    "— Olhem para as aves do céu — disse Jesus apontando para as andorinhas que voavam sobre o lago —: elas não guardam comida em celeiros, e o Pai Celestial alimenta cada uma delas! E olhem para os lírios do campo: nem o rei Salomão em toda a sua glória se vestiu com cores tão bonitas!\n"
                    "— Portanto, busquem primeiro o Reino de Deus e a Sua justiça!"
                ),
                "arq_title": "AS LÂMPADAS DE CERÂMICA NAS CASAS DA GALILEIA",
                "arq_text": "Como as casas de pedra tinham janelas pequenas, uma única lamparina de barro colocada num suporte alto na parede central conseguia iluminar o cômodo inteiro para toda a família!",
                "family_question": "Que atitude boa você pode ter hoje em casa ou na escola para funcionar como uma 'lamparinha acesa' que alegra o ambiente?"
            },
            {
                "num": 2,
                "title": "O SEMEADOR E A SEMENTINHA GIGANTE",
                "ref": "Base Bíblica: Mateus 13:1–9, 18–23, 31–32",
                "dark_mode": False,
                "art_source": "vol1_cap4_caim_abel.jpg",
                "main_narrative": (
                    "De dentro de um barco junto à praia, Jesus contou a história de um agricultor que saiu a espalhar sementes: algumas caíram na estrada dura, outras entre pedras, outras entre espinhos, mas muitas caíram na terra boa, macia e preparada — e deram trinta, sessenta e cem vezes mais frutos!\n\n"
                    "— A semente é a Palavra do amor e da verdade — explicou Jesus —, e a terra boa é o coração que ouve, compreende e pratica o bem! Como o pequenino grão de mostarda, um gesto de bondade cresce até virar uma grande árvore."
                ),
                "quick_box": "» VOCÊ PERCEBEU? Um coração atento e bondoso é como a terra fértil regada pela chuva: tudo o que é bom floresce nele!",
                "seed_4_6": "Jesus contou a história de um lavrador que plantou sementinhas no campo. As sementes que caíram na terra fofinha e boa cresceram e deram muitos frutos deliciosos! Assim é o nosso coração quando ouvimos e praticamos o amor.",
                "explorer_dialogue": (
                    "— Mestre, por que você ensina o povo contando histórias da roça e das sementes? — perguntaram os discípulos.\n"
                    "— Porque quem olha para uma simples semente com olhos atentos descobre o segredo do Reino de Deus! — sorriu Jesus, mostrando na palma da mão uma minúscula semente de mostarda."
                ),
                "arq_title": "COMO SE PLANTAVA TRIGO NA GALILEIA ANTIGA",
                "arq_text": "Os camponeses da Galileia caminhavam pelos terraços agrícolas lançando os grãos de trigo com a mão a partir de uma bolsa de linho presa ao ombro, exatamente como descrito em Mateus 13.",
                "family_question": "O que ajuda a manter o nosso coração 'fofinho como terra boa' para que as sementes da paciência e da alegria cresçam nele?"
            },
            {
                "num": 3,
                "title": "QUEM É O MEU PRÓXIMO? O BOM SAMARITANO",
                "ref": "Base Bíblica: Lucas 10:25–37",
                "dark_mode": False,
                "art_source": "HERO_VOL7",
                "main_narrative": (
                    "Quando um mestre da Lei perguntou 'Quem é o meu próximo que eu devo amar?', Jesus contou a história de um viajante que foi assaltado e deixado ferido na estrada de Jerusalém para Jericó. Dois homens religiosos passaram de largo sem ajudar.\n\n"
                    "Mas um viajante samaritano — povo que muitos desprezavam — sentiu compaixão, limpou as feridas do homem com azeite, colocou-o em seu próprio jumento, levou-o a uma hospedaria e pagou todo o tratamento! 'Vá e faça você o mesmo!', concluiu Jesus."
                ),
                "quick_box": "» O QUE VOCÊ FARIA? O verdadeiro amigo do próximo é aquele que para no caminho para socorrer quem precisa!",
                "seed_4_6": "Um viajante caiu machucado na estrada e precisava de ajuda. Um bom samaritano parou seu jumentinho, fez curativos nele com todo o carinho e cuidou dele até sarar! Jesus ensinou que amar o próximo é ajudar qualquer pessoa que precise de nós.",
                "explorer_dialogue": (
                    "Ao terminar a história, Jesus olhou nos olhos do doutor da Lei e perguntou:\n"
                    "— Na sua opinião, qual daqueles três homens que passaram pela estrada mostrou ser o verdadeiro próximo de quem estava ferido?\n"
                    "— Aquele que teve misericórdia e cuidou dele! — respondeu o mestre.\n"
                    "— Então vá e faça exatamente assim! — disse Jesus."
                ),
                "arq_title": "O AZEITE E A HOSPEDARIA (KHAN) NA ANTIGUIDADE",
                "arq_text": "Nas viagens antigas, o azeite de oliva era levado nos alforjes tanto como alimento quanto como bálsamo calmante e protetor para machucados na pele!",
                "family_question": "Se você vir um colega novo ou machucado sentado sozinho no pátio da escola, como você pode agir como o Bom Samaritano?"
            },
            {
                "num": 4,
                "title": "A OVELHINHA ENCONTRADA PELO BOM PASTOR",
                "ref": "Base Bíblica: Lucas 15:1–7; João 10:11–14",
                "dark_mode": False,
                "art_source": "HERO_VOL7",
                "main_narrative": (
                    "Para mostrar o quanto cada pessoa é preciosa aos olhos de Deus, Jesus perguntou: 'Qual de vocês, tendo cem ovelhas e perdendo uma só delas no deserto, não vai atrás da que se perdeu até encontrá-la?'\n\n"
                    "Quando o pastor finalmente escuta o balido fraquinho da ovelha presa entre os espinhos, ele não briga com ela: coloca-a com ternura sobre os ombros e volta para casa cantando: 'Alegrem-se comigo, porque encontrei a minha ovelha que havia se perdido!'"
                ),
                "quick_box": "» CONVERSE COMIGO: Para o Bom Pastor, nenhuma ovelhinha é esquecida — cada vida vale o mundo inteiro!",
                "seed_4_6": "Um pastor tinha cem ovelhinhas, mas uma delas se perdeu nas pedras! O bom pastor procurou até achá-la, colocou a ovelhinha nos ombros com todo o carinho e fez uma festa com os vizinhos porque ela voltou em segurança!",
                "explorer_dialogue": (
                    "— Eu sou o Bom Pastor! — explicou Jesus às crianças e às famílias. — O bom pastor conhece cada uma de suas ovelhas pelo nome, e as ovelhas reconhecem a voz dele porque sabem que são amadas."
                ),
                "arq_title": "OS CURRAIS DE PEDRA DOS PASTORES DA JUDEIA",
                "arq_text": "À noite, os pastores recolhiam o rebanho dentro de cercados circulares de pedra com uma única entrada estreita, onde o próprio pastor se deitava servindo de 'porta viva' para proteger as ovelhas.",
                "family_question": "Você já perdeu algum brinquedo ou objeto querido e sentiu uma alegria imensa quando o encontrou? Imagine o quanto Deus ama cada um de nós!"
            },
            {
                "num": 5,
                "title": "OS BRAÇOS ABERTOS DO PAI QUE ESPERAVA",
                "ref": "Base Bíblica: Lucas 15:11–32 (A Parábola do Filho Pródigo)",
                "dark_mode": True,
                "art_source": "vol2_cap6_abraco_perdao.jpg",
                "main_narrative": (
                    "Em seguida, Jesus contou a história de um pai que tinha dois filhos. O mais novo pediu sua parte da herança, viajou para longe e gastou tudo de forma imprudente. Passando fome e arrependido, decidiu voltar para casa pedindo apenas um lugar humilde.\n\n"
                    "Mas, quando ele ainda estava longe na estrada, o pai o avistou, sentiu profunda compaixão, correu ao seu encontro, lançou os braços ao seu pescoço e o beijou! E convidou também o irmão mais velho a vencer o ciúme e entrar na festa do perdão."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Na cultura antiga, um patriarca idoso nunca corria na rua — mas o pai correu por puro amor ao filho!",
                "seed_4_6": "Um filho foi morar longe, fez escolhas erradas e ficou com muita saudade de casa. Quando ele voltou arrependido pela estrada, o papai correu de braços abertos para abraçá-lo e beijá-lo, mostrando que o amor de Deus sempre nos recebe de volta!",
                "explorer_dialogue": (
                    "— Pai, eu errei contra o Céu e contra o senhor! — disse o jovem com lágrimas nos olhos.\n"
                    "Antes mesmo que ele terminasse a frase, o pai pediu túnica limpa, sandálias novas para seus pés descalços e abraçou também o filho mais velho no pátio:\n"
                    "— Meu filho, você está sempre comigo, e tudo o que é meu é seu; mas tínhamos de celebrar, porque este seu irmão estava perdido e foi encontrado!"
                ),
                "arq_title": "AS SANDÁLIAS E O ANEL DA FAMÍLIA",
                "arq_text": "Na antiguidade, andar descalço era sinal de servidão, enquanto receber sandálias nos pés e o anel no dedo significava ser restaurado plenamente como filho amado da casa!",
                "family_question": "Por que na história de Jesus o pai saiu para abraçar tanto o filho mais novo (que errou longe) quanto o filho mais velho (que estava com raiva na porta)?"
            },
            {
                "num": 6,
                "title": "A CASA CONSTRUÍDA SOBRE A ROCHA FIRME",
                "ref": "Base Bíblica: Mateus 7:12, 24–27; 13:44–46",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena3_ceu_mar_terra.png",
                "main_narrative": (
                    "Para encerrar seus ensinamentos no monte, Jesus deixou a Regra de Ouro: 'Tudo o que vocês quiserem que os outros façam por vocês, façam também vocês por eles!' E contou a parábola dos dois construtores:\n\n"
                    "Quem ouve as palavras de Jesus e as coloca em prática no dia a dia é como um construtor prudente que edificou sua casa sobre a rocha firme: caiu a chuva, transbordaram os rios, sopraram os ventos, mas a casa não caiu, porque estava alicerçada na Rocha do Amor!"
                ),
                "quick_box": "» REGRA DE OURO (MATEUS 7:12): Trate todas as pessoas exatamente com o mesmo carinho e respeito com que você gosta de ser tratado!",
                "seed_4_6": "Jesus contou que quem ouve suas palavras de amor e ajuda as pessoas é como um construtor esperto que fez sua casinha em cima da rocha firme: mesmo quando vem a chuva e o vento forte, a casa fica firme e segura!",
                "explorer_dialogue": (
                    "Quando Jesus terminou de pronunciar aquelas palavras, as famílias desceram da colina maravilhadas:\n"
                    "— Vocês ouviram como ele ensina? — comentavam os pais segurando a mão das crianças. — Suas palavras têm autoridade viva e acendem uma luz dentro da nossa casa!"
                ),
                "arq_title": "AS FUNDAÇÕES DE BASALTO EM CAFARNAUM",
                "arq_text": "Nas chuvas de inverno da Galileia, enxurradas repentinas varriam qualquer construção feita direto na areia; por isso os construtores sábios cavavam até assentar os alicerces na rocha basáltica!",
                "family_question": "Quais são as 'pedras firmes' (como a verdade, o respeito, a oração e a união) sobre as quais a sua família constrói o lar todos os dias?"
            }
        ]
    },

    # =========================================================================
    # VOLUME 8 — QUANDO O AMOR FAZ MILAGRES (Sinais, Curas e Cuidado de Jesus)
    # =========================================================================
    {
        "num": 8,
        "slug": "Volume-8-Quando-o-Amor-Faz-Milagres",
        "md_file": "Volume8_Quando_o_Amor_Faz_Milagres_Roteiro_e_Storyboard.md",
        "title": "QUANDO O AMOR FAZ MILAGRES",
        "subtitle": "Encontros de cura, tempestades acalmadas e mesas abertas",
        "biblical_range": "Marcos 2, 4, 5, 10; Lucas 19; João 2 e 6",
        "cover_base_prefix": "vol8_capa_base_aventura",
        "hero_art_prefix": "vol8_cap3_milagres_galileia",
        "intro_text": (
            "Bem-vindo ao oitavo volume da coleção A Grande História da Luz! Jesus não apenas contava belas histórias sobre o amor de Deus: por onde ele passava, suas mãos estendidas enxugavam lágrimas, devolviam a saúde aos enfermos, acalmavam ventos furiosos no mar e multiplicavam o pão para os famintos.\n\n"
            "Neste livro você verá quatro amigos leais abrindo um telhado em Cafarnaum, um menino repartindo seu lanche de cinco pães e dois peixinhos, Zaqueu descendo da figueira e Jesus abraçando as crianças!"
        ),
        "map_title": "MAPA DOS SINAIS: CANÁ, CAFARNAUM, MAR DA GALILEIA E JERICÓ",
        "archaeology_section_title": "1. ARQUEOLOGIA DE CAFARNAUM E DO MAR DA GALILEIA",
        "archaeology_full": (
            "• As Casas com Telhado de Terra Batida em Cafarnaum (Marcos 2): As casas da Galileia tinham escadas externas de pedra que subiam ao terraço plano, feito de vigas de madeira cobertas de ramos e barro compactado — por isso os quatro amigos conseguiram abrir um espaço no teto!\n\n"
            "• Os Pães de Cevada e os Peixes da Galileia (João 6): O pão de cevada era o alimento diário das famílias mais simples, acompanhado da 'tilápia-da-galileia' (conhecida até hoje como Peixe de São Pedro).\n\n"
            "• Os Sicômoros de Jericó (Lucas 19): A árvore em que Zaqueu subiu ('ficus sycomorus') possui tronco baixo e galhos largos muito fáceis de escalar, oferecendo excelente visão da avenida principal."
        ),
        "glossary_full": (
            "• SINAL / MILAGRE: Uma obra extraordinária de amor e compaixão que revela a presença curadora de Deus.\n"
            "• CAFARNAUM: Aldeia de pescadores na margem norte do Mar da Galileia onde Jesus morou durante seu ministério.\n"
            "• COMPARTILHAR: Repartir com alegria o que temos para que ninguém fique com fome ou excluído.\n"
            "• SICÔMORO: Grande árvore aparentada da figueira, típica do vale quente de Jericó.\n"
            "• RESTITUIÇÃO: Devolver e reparar com generosidade qualquer prejuízo causado a alguém, como fez Zaqueu."
        ),
        "char_notes": (
            "• JESUS E AS CRIANÇAS: Jesus aparece sentado ao nível do olhar das crianças galileias, acolhendo meninos e meninas com ternura e impondo as mãos para abençoá-los.\n\n"
            "• O MENINO DOS CINCO PÃES E DOIS PEIXINHOS: Criança galileia de cerca de 8 anos com cestinho de vime trançado oferecendo seu lanche com um sorriso generoso.\n\n"
            "• ZAQUEU EM JERICÓ: Homem de baixa estatura em túnica bordada sentado nos galhos de um sicômoro frondoso e depois recebendo Jesus em sua mesa."
        ),
        "back_cover_synopsis": (
            "'Deixem vir a mim as criancinhas e não as impeçam, porque o Reino de Deus pertence aos que são semelhantes a elas!'\n\n"
            "Neste oitavo volume escrito por Fábio Motta e Silva, acompanhamos os encontros mais emocionantes de Jesus pelas estradas e águas da Galileia, aprendendo que o maior milagre começa quando abrimos o coração para cuidar das pessoas!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "QUATRO AMIGOS NO TELHADO E A FESTA EM CANÁ",
                "ref": "Base Bíblica: João 2:1–11; Marcos 2:1–12",
                "dark_mode": False,
                "art_source": "vol3_cap5_pao_do_ceu_sinai.jpg",
                "main_narrative": (
                    "Depois de levar alegria a uma festa de casamento em Caná da Galileia a pedido de sua mãe Maria, Jesus voltou para Cafarnaum. A casa onde ele ensinava ficou tão cheia de gente que não cabia mais ninguém nem na porta!\n\n"
                    "Foi então que quatro amigos trouxeram um companheiro paralítico deitado numa esteira. Não conseguindo entrar pela porta, subiram pela escada externa, abriram cuidadosamente o telhado de ramos e barro e desceram o amigo bem diante de Jesus! Vendo a fé daquela amizade, Jesus o perdoou e o curou completamente."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: 'Jesus, vendo a fé que aqueles amigos tinham...' (Marcos 2:5) — a amizade deles abriu o caminho!",
                "seed_4_6": "A casa onde Jesus estava ficou tão lotada que quatro amigos subiram no telhado e desceram seu amigo doente numa esteira bem na frente de Jesus! Maravilhado com o carinho daqueles amigos, Jesus curou o homem, que saiu andando e pulando de alegria!",
                "explorer_dialogue": (
                    "Quando a luz do sol entrou pela abertura do telhado de Cafarnaum e a esteira pousou no chão, Jesus sorriu para os quatro amigos lá em cima e disse ao homem:\n"
                    "— Filho, tenha bom ânimo! Os seus pecados estão perdoados. Levante-se, pegue a sua esteira e volte caminhando para casa!\n"
                    "Todos abriram espaço maravilhados, glorificando a Deus e dizendo: 'Nunca vimos coisa igual!'"
                ),
                "arq_title": "A CASA DE PEDRO EM CAFARNAUM",
                "arq_text": "Arqueólogos escavaram em Cafarnaum, a poucos metros da praia do lago, uma residência de pescadores de pedra basáltica negra do século I que se tornou o primeiro local de reunião dos amigos de Jesus!",
                "family_question": "Aqueles quatro amigos não desistiram diante da porta cheia. Como podemos ser amigos criativos e solidários quando alguém precisa de ajuda?"
            },
            {
                "num": 2,
                "title": "QUIETO, VENTO! PAZ, MAR! E A MENINA DE JAIRO",
                "ref": "Base Bíblica: Marcos 4:35–41; 5:21–43",
                "dark_mode": True,
                "art_source": "vol3_cap4_travessia_mar.jpg",
                "main_narrative": (
                    "Atravessando o Mar da Galileia ao anoitecer no barco de madeira, desabou das montanhas uma tempestade súbita. As ondas batiam com força e os discípulos gritaram assustados. Jesus levantou-se na proa e disse às águas: 'Aquiete-se! Fique em paz!' No mesmo instante o vento cessou e fez-se grande bonança!\n\n"
                    "Ao chegar à outra margem, Jesus foi à casa de Jairo, cuja filhinha de doze anos estava sem forças. Segurando a mão da menina com ternura, disse em aramaico: 'Talita cumi!' ('Menina, levante-se!'), devolvendo-a viva aos braços dos pais!"
                ),
                "quick_box": "» VOCÊ PERCEBEU? Depois de levantar a menina de doze anos, Jesus pediu com carinho: 'Deem alguma coisa para ela comer!'",
                "seed_4_6": "Quando uma tempestade forte balançou o barco no lago, Jesus estendeu a mão e disse: 'Paz, fique quieto!' e o mar ficou calminho na hora! Depois ele segurou a mãozinha de uma menina de doze anos que estava muito doente e a devolveu saudável para o papai e a mamãe!",
                "explorer_dialogue": (
                    "Enquanto o barco deslizava sobre o espelho calmo do lago iluminado pelas estrelas, Jesus perguntou com brandura aos amigos:\n"
                    "— Por que vocês ficaram com tanto medo? Ainda não confiam que a Luz do Pai está conosco no barco?\n"
                    "E na casa de Jairo, o cuidado de Jesus mostrou que para Deus até a fome de uma criança recém-curada importa."
                ),
                "arq_title": "OS VENTOS SÚBITOS DO MAR DA GALILEIA",
                "arq_text": "Como o Mar da Galileia fica 210 metros abaixo do nível do mar e é cercado pelas colinas altas do Golã, correntes de ar frio descem pelos vales criando tempestades repentinas em poucos minutos!",
                "family_question": "Quando uma 'tempestade' de medo ou preocupação aparece no seu dia, o que ajuda o seu coração a ouvir a voz de paz de Jesus?"
            },
            {
                "num": 3,
                "title": "O LANCHE DE UM MENINO QUE ALIMENTOU A MULTIDÃO",
                "ref": "Base Bíblica: João 6:1–14; Marcos 6:34–44",
                "dark_mode": False,
                "art_source": "HERO_VOL8",
                "main_narrative": (
                    "Mais de cinco mil pessoas acompanharam Jesus até uma colina verdejante para ouvi-lo o dia inteiro. Quando a tarde caiu e todos sentiram fome, André apresentou a Jesus um menino que havia trazido seu pequeno cesto de viagem: 'Aqui está um garoto que tem cinco pães de cevada e dois peixinhos; mas o que é isso para tanta gente?'\n\n"
                    "Jesus agradeceu o gesto generoso do menino, pediu que as famílias se sentassem na grama, ergueu os olhos ao céu dando graças e repartiu o alimento: todos comeram à vontade e ainda sobraram doze cestos cheios!"
                ),
                "quick_box": "» O QUE VOCÊ FARIA? O grande milagre começou quando uma criança decidiu não esconder o seu lanche, mas compartilhá-lo!",
                "seed_4_6": "Uma multidão enorme estava com fome no campo, e um menino ofereceu a Jesus seu cestinho com cinco pães e dois peixinhos! Jesus agradeceu ao Pai do Céu, repartiu o lanche e multiplicou a comida até alimentar todo mundo com fartura!",
                "explorer_dialogue": (
                    "— Mestre, pode usar os meus cinco pãezinhos e os dois peixes que minha mãe preparou! — disse o menino, entregando o cesto a Jesus com os olhos brilhando.\n"
                    "— Obrigado, meu pequeno amigo! — sorriu Jesus. — Quando o pouco que temos é colocado nas mãos do Amor e repartido com generosidade, ele se multiplica para abençoar a todos!"
                ),
                "arq_title": "O MOSAICO DOS PÃES E PEIXES EM TABGHA",
                "arq_text": "Na margem noroeste do Mar da Galileia (em Tabgha, região das sete fontes), preserva-se até hoje um famoso mosaico bizantino do século V mostrando o cesto com os pães e os dois peixes!",
                "family_question": "O menino achava que seu lanche era pequeno demais, mas fez toda a diferença. Como um pequeno gesto seu pode ajudar muita gente?"
            },
            {
                "num": 4,
                "title": "OS OLHOS DE BARTIMEU E A DESCIDA DE ZAQUEU",
                "ref": "Base Bíblica: Marcos 10:46–52; Lucas 19:1–10",
                "dark_mode": False,
                "art_source": "vol1_cap2_jardim_eden.jpg",
                "main_narrative": (
                    "Ao chegar à cidade das palmeiras, Jericó, Jesus ouviu o clamor do cego Bartimeu sentado à beira do caminho. Enquanto muitos mandavam Bartimeu calar-se, Jesus parou, chamou-o pelo nome e perguntou: 'O que você quer que eu lhe faça?' 'Mestre, que eu torne a ver!', respondeu ele, e no mesmo instante seus olhos se encheram de luz e cores!\n\n"
                    "Mais adiante, Zaqueu — um cobrador de impostos baixinho que havia subido numa figueira-brava — ouviu Jesus olhar para cima e dizer: 'Zaqueu, desça depressa, porque hoje preciso ficar na sua casa!' Tocado por aquele acolhimento, Zaqueu mudou de vida e repartiu seus bens com os pobres."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Jesus nunca passava apressado demais a ponto de não enxergar quem estava à margem ou em cima da árvore!",
                "seed_4_6": "Em Jericó, Jesus parou para devolver a visão ao cego Bartimeu e depois olhou para o alto de uma grande árvore onde o baixinho Zaqueu estava escondido: 'Zaqueu, desça daí, hoje vou almoçar na sua casa!' Aquele carinho transformou o coração de Zaqueu!",
                "explorer_dialogue": (
                    "Deslizando pelo tronco do sicômoro com o coração batendo forte de alegria, Zaqueu recebeu Jesus em sua sala e declarou diante de toda a cidade:\n"
                    "— Senhor, resolvi dar metade de tudo o que tenho aos pobres; e, se cobrei alguma coisa a mais de alguém, vou devolver quatro vezes mais!\n"
                    "— Hoje a salvação e a paz entraram nesta casa! — celebrou Jesus."
                ),
                "arq_title": "JERICÓ: A CIDADE DOS SICÔMOROS E DO BÁLSAMO",
                "arq_text": "Jericó era um grande centro comercial e alfandegário na fronteira da Judeia, cercado por avenidas sombreadas por sicômoros, tamareiras e jardins de plantas aromáticas.",
                "family_question": "O acolhimento de Jesus mudou o coração de Zaqueu muito mais do que as críticas das pessoas. Por que o respeito transforma as pessoas?"
            },
            {
                "num": 5,
                "title": "DEIXEM VIR A MIM AS CRIANÇAS!",
                "ref": "Base Bíblica: Marcos 10:13–16; Mateus 18:1–5",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena7_nomes_cuidadores.jpg",
                "main_narrative": (
                    "Muitos pais e mães traziam seus filhos pequenos para que Jesus os tocasse e abençoasse. Achando que o Mestre estava ocupado demais com assuntos de adultos, os discípulos tentaram afastar as crianças.\n\n"
                    "Ao ver aquilo, Jesus indignou-se e disse uma das frases mais importantes de todos os Evangelhos: 'Deixem vir a mim as criancinhas e não as impeçam, porque o Reino de Deus pertence aos que são semelhantes a elas!' Então tomou as crianças nos braços, ouviu suas histórias e as abençoou com todo amor."
                ),
                "quick_box": "» CONVERSE COMIGO: No Reino da Luz, as crianças não ficam no último lugar da fila — elas estão bem no centro do abraço de Jesus!",
                "seed_4_6": "Alguns adultos acharam que Jesus estava ocupado demais para conversar com as crianças. Mas Jesus abriu os braços sorrindo e disse: 'Deixem as criancinhas virem até mim, porque o Reino de Deus é delas!' E abraçou e abençoou cada uma!",
                "explorer_dialogue": (
                    "Chamando uma criança pequena para ficar no meio da roda dos discípulos, Jesus apontou para a sinceridade e a alegria nos olhos dela:\n"
                    "— Eu digo a verdade a vocês: vocês, adultos, é que precisam aprender com as crianças a confiar sem orgulho! E quem recebe uma criança como esta em meu nome, está recebendo a mim mesmo!"
                ),
                "arq_title": "A VALORIZAÇÃO DAS CRIANÇAS NOS ENSINAMENTOS DE JESUS",
                "arq_text": "No mundo greco-romano antigo, as crianças quase não tinham voz pública. Ao colocá-las no centro da roda como modelo do Reino de Deus, Jesus inaugurou uma nova visão sobre a dignidade sagrada da infância!",
                "family_question": "Se você estivesse naquela roda sentado ao lado de Jesus, o que você gostaria de contar ou perguntar para ele?"
            },
            {
                "num": 6,
                "title": "A CASA DE BETÂNIA: MARTA, MARIA E LÁZARO",
                "ref": "Base Bíblica: Lucas 10:38–42; João 11:1–44",
                "dark_mode": True,
                "art_source": "vol3_cap3_noite_liberdade.jpg",
                "main_narrative": (
                    "Perto de Jerusalém, na pequena aldeia de Betânia, moravam três grandes amigos de Jesus: as irmãs Marta e Maria e o irmão delas, Lázaro. Ali Jesus sempre encontrava descanso, boa conversa e amizade sincera.\n\n"
                    "Quando Lázaro adoeceu gravemente e faleceu, Jesus chorou junto com suas amigas, mostrando que Ele sente a nossa dor. Em seguida, diante da gruta de pedra, declarou: 'Eu sou a Ressurreição e a Vida!' e chamou com voz cheia de luz: 'Lázaro, venha para fora!' E Lázaro saiu vivo para o abraço das irmãs!"
                ),
                "quick_box": "» VOCÊ PERCEBEU? 'Jesus chorou' (João 11:35) é o versículo mais curto da Bíblia e mostra o quanto o coração d'Ele é cheio de empatia!",
                "seed_4_6": "Em Betânia moravam três grandes amigos de Jesus: Marta, Maria e Lázaro. Quando Lázaro ficou muito doente, Jesus consolou suas amigas e, com o poder da Luz de Deus, trouxe Lázaro de volta à vida para a alegria de toda a família!",
                "explorer_dialogue": (
                    "— Senhor, se você estivesse aqui, meu irmão não teria partido — disse Marta entre lágrimas, mas acrescentou com fé: — Ainda assim, sei que você é o Filho de Deus que veio ao mundo!\n"
                    "E quando Lázaro saiu da gruta sob a luz dourada da manhã, Jesus disse aos amigos: 'Desamarrem as faixas dele e deixem-no caminhar livre!'"
                ),
                "arq_title": "A ALDEIA DE BETÂNIA NO MONTE DAS OLIVEIRAS",
                "arq_text": "Betânia ficava na encosta leste do Monte das Oliveiras, a apenas três quilômetros de Jerusalém (cerca de 40 minutos de caminhada), cercada de figueiras, amendoeiras e tamareiras.",
                "family_question": "Saber que Jesus chorou junto com os amigos que estavam tristes mostra que não precisamos esconder nossas lágrimas. Quem consola você quando você chora?"
            }
        ]
    },

    # =========================================================================
    # VOLUME 9 — O AMOR MAIS FORTE QUE O MEDO (Páscoa, Entrega e Ressurreição)
    # =========================================================================
    {
        "num": 9,
        "slug": "Volume-9-O-Amor-Mais-Forte-que-o-Medo",
        "md_file": "Volume9_O_Amor_Mais_Forte_que_o_Medo_Roteiro_e_Storyboard.md",
        "title": "O AMOR MAIS FORTE QUE O MEDO",
        "subtitle": "A última semana em Jerusalém e a manhã que mudou tudo",
        "biblical_range": "Mateus 21, 26–28; Marcos 14–16; Lucas 22–24; João 13, 19–21",
        "cover_base_prefix": "vol9_capa_base_aventura",
        "hero_art_prefix": "vol9_cap5_jardim_pascoa",
        "intro_text": (
            "Bem-vindo ao nono volume da coleção A Grande História da Luz! Chegamos à semana mais decisiva de toda a história bíblica. Jesus entrou em Jerusalém não num cavalo de guerra, mas num jumentinho manso, saudado pelas crianças com ramos de palmeira!\n\n"
            "Com delicadeza poética, verdade bíblica e foco luminoso, acompanharemos a ceia da amizade onde Jesus lavou os pés dos amigos, o dia em que o céu escureceu e a gloriosa manhã de domingo no jardim, quando a pedra rolou e a Vida venceu para sempre!"
        ),
        "map_title": "MAPA DE JERUSALÉM NO SÉCULO I: CENÁCULO, GETSÊMANI E JARDIM",
        "archaeology_section_title": "1. ARQUEOLOGIA DA JERUSALÉM DO SÉCULO I",
        "archaeology_full": (
            "• O Jardim das Oliveiras (Getsêmani): Ao pé do Monte das Oliveiras existem até hoje oliveiras milenares cujas raízes descendem das árvores da época de Jesus; 'Gath-Shemanim' significa 'Prensa de Azeite'.\n\n"
            "• Os Túmulos Escavados na Rocha com Pedra Rolante: Na Jerusalém do século I, os túmulos de jardim eram câmaras talhadas na rocha calcária branca fechadas por uma grande pedra circular em formato de roda ('golal') que corria sobre um trilho de pedra.\n\n"
            "• A Praia de Tabgha / Cafarnaum (João 21): Onde Jesus preparou pão e peixe assado na brasa ao amanhecer para receber de volta seus amigos pescadores."
        ),
        "glossary_full": (
            "• HOSANA: Palavra hebraica de aclamação e alegria usada pelas famílias e crianças na entrada de Jerusalém.\n"
            "• LAVA-PÉS: Gesto de humildade de Jesus mostrando que o verdadeiro líder é aquele que serve com amor.\n"
            "• GETSÊMANI: Jardim de oliveiras onde Jesus orou ao Pai entregando sua vida por amor à humanidade.\n"
            "• RESSURREIÇÃO: O despertar vitorioso de Jesus na manhã de domingo, vencendo a morte com a Luz eterna.\n"
            "• EMAÚS: Aldeia próxima a Jerusalém para onde dois discípulos caminhavam quando reconheceram Jesus ao partir o pão."
        ),
        "char_notes": (
            "• PROTOCOLO VISUAL SENSÍVEL (SEM VIOLÊNCIA GRÁFICA): Seguindo rigorosamente a diretriz psicopedagógica da coleção (4–10 anos), a entrega na cruz é tratada com reverência poética e simbólica (silhueta ao longe sob o céu dramático que se abre num feixe de luz de perdão), concentrando o esplendor visual na manhã luminosa do Jardim da Ressurreição.\n\n"
            "• MARIA MADALENA E AS MULHERES NO JARDIM: Primeiras testemunhas da Ressurreição ao nascer do sol, vestindo mantos de linho e lã em tons de aurora."
        ),
        "back_cover_synopsis": (
            "'Por que vocês procuram entre os mortos Aquele que vive? Ele não está aqui: ressuscitou!'\n\n"
            "Neste nono volume escrito por Fábio Motta e Silva, crianças e famílias contemplam o triunfo do amor, da humildade e do perdão de Jesus na manhã de Páscoa — abrindo as portas para o grande encerramento da coleção no Volume 10 (*A Luz Continua*)!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "RAMOS DE PALMEIRA E O REI DA PAZ EM JERUSALÉM",
                "ref": "Base Bíblica: Mateus 21:1–16; Zacarias 9:9",
                "dark_mode": False,
                "art_source": "vol1_cap2_jardim_eden.jpg",
                "main_narrative": (
                    "Quando chegou a semana da festa da Páscoa, Jesus subiu a Jerusalém montado num jumentinho manso, cumprindo a profecia antiga de que o Rei justo viria com humildade e paz, e não com carros de guerra.\n\n"
                    "As famílias estenderam seus mantos pelo caminho e balançaram ramos verdes de palmeira e oliveira! E no pátio do Templo, as crianças cantavam em coro: 'Hosana ao Filho de Davi! Bendito o que vem em nome do Senhor!'"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Os generais entravam nas cidades em cavalos de guerra; os reis em missão de paz vinham num jumentinho!",
                "seed_4_6": "Jesus entrou em Jerusalém montado num jumentinho bem manso para mostrar que ele é o Rei da Paz! As crianças abanavam folhas verdes de palmeira pelo caminho e cantavam bem alto: 'Hosana! Viva o Filho de Davi!'",
                "explorer_dialogue": (
                    "Ao ouvirem as vozes alegres dos meninos e meninas ecoando nas colunas do Templo, alguns líderes mal-humorados reclamaram com Jesus:\n"
                    "— Você não está ouvindo o que essas crianças estão cantando?\n"
                    "Jesus sorriu com ternura para as crianças e respondeu:\n"
                    "— Sim! Vocês nunca leram no Salmo 8 que 'dos lábios dos pequeninos Deus preparou o mais belo louvor'?"
                ),
                "arq_title": "O CAMINHO DO MONTE DAS OLIVEIRAS AO TEMPLO",
                "arq_text": "A estrada que descia do Monte das Oliveiras oferecia uma vista panorâmica deslumbrante de toda a cidade de Jerusalém e dos muros dourados do Templo ao sol da manhã.",
                "family_question": "Jesus mostrou que a mansidão e a paz são mais fortes que a arrogância. Como podemos ser mensageiros de paz na nossa semana?"
            },
            {
                "num": 2,
                "title": "A BACIA DE ÁGUA, O PÃO REPARTIDO E O NOVO MANDAMENTO",
                "ref": "Base Bíblica: João 13:1–17, 34–35; Lucas 22:14–20",
                "dark_mode": True,
                "art_source": "vol3_cap3_noite_liberdade.jpg",
                "main_narrative": (
                    "Reunido com seus amigos numa sala no andar superior em Jerusalém para a ceia da Páscoa, Jesus levantou-se da mesa, amarrou uma toalha na cintura, despejou água limpa numa bacia e começou a lavar e enxugar os pés empoeirados de cada um dos discípulos!\n\n"
                    "Depois repartiu o pão e o cálice como sinal de sua entrega por amor e deixou o seu Novo Mandamento: 'Amem-se uns aos outros! Assim como Eu amei vocês, que vocês também se amem uns aos outros!'"
                ),
                "quick_box": "» O QUE VOCÊ FARIA? O Mestre de todos ajoelhou-se com uma toalha nas mãos para ensinar que amar é servir com alegria!",
                "seed_4_6": "No jantar da Páscoa com seus amigos, Jesus pegou uma bacia de água morna e uma toalha e lavou os pés cansados dos discípulos! Depois ele repartiu o pão na mesa e disse: 'Amem uns aos outros assim como eu amo vocês!'",
                "explorer_dialogue": (
                    "— Senhor, você vai lavar os meus pés?! — espantou-se Simão Pedro.\n"
                    "Terminando de enxugar os pés dos doze, Jesus vestiu novamente o manto, sentou-se à mesa e explicou:\n"
                    "— Vocês me chamam de Mestre e Senhor, e dizem bem. Pois, se Eu, sendo o Mestre, lavei os pés de vocês, também vocês devem cuidar uns dos outros com humildade! Por esse amor todos saberão que vocês são meus discípulos."
                ),
                "arq_title": "O CENÁCULO (SALA SUPERIOR) EM JERUSALÉM",
                "arq_text": "As casas amplas do Bairro Alto de Jerusalém no século I possuíam no segundo andar um grande salão de banquetes ('anagaion') mobiliado com tapetes e mesas baixas em formato de 'U' ('triclinium').",
                "family_question": "Qual gesto simples de ajuda dentro de casa (como arrumar a mesa, guardar os brinquedos ou ajudar alguém cansado) imita o exemplo de Jesus?"
            },
            {
                "num": 3,
                "title": "O JARDIM DAS OLIVEIRAS E O AMOR QUE NÃO DESISTE",
                "ref": "Base Bíblica: Lucas 22:39–46; 23:33–46 (Tratamento Sensível e Poético)",
                "dark_mode": True,
                "art_source": "vol1_cap3_escolha_jardim.jpg",
                "main_narrative": (
                    "Naquela noite, sob as antigas árvores do jardim do Getsêmani, Jesus orou profundamente ao Pai, escolhendo o caminho da entrega e da paz. Mesmo quando foi preso injustamente e seus amigos correram assustados, inclusive Pedro que chorou arrependido por tê-lo negado, o coração de Jesus permaneceu cheio de compaixão.\n\n"
                    "Na colina fora dos muros da cidade, quando o céu do meio-dia escureceu, Jesus entregou sua vida por amor a toda a humanidade e pronunciou as palavras supremas de misericórdia: 'Pai, perdoa-lhes, porque não sabem o que fazem!' E José de Arimateia depositou seu corpo num túmulo novo dentro de um jardim."
                ),
                "quick_box": "» CONVERSE COMIGO: Mesmo no momento mais difícil, a resposta de Jesus foi o perdão — porque a Luz nunca se transforma em ódio!",
                "seed_4_6": "Homens injustos prenderam Jesus porque tinham inveja do bem que ele fazia. Mesmo sofrendo na cruz, Jesus orou pedindo a Deus que perdoasse a todos! Seus amigos ficaram muito tristes achando que era o fim, mas o domingo da Luz já estava chegando!",
                "explorer_dialogue": (
                    "Enquanto a tarde caía silenciosa sobre Jerusalém, um oficial romano que observava a serenidade e o amor com que Jesus havia entregado a vida tirou o capacete e declarou emocionado:\n"
                    "— Verdadeiramente, este homem era justo e Filho de Deus!\n"
                    "No jardim silencioso, uma grande pedra redonda fechou o túmulo na sexta-feira à tarde. Mas uma semente plantada na terra logo brotaria para a vida eterna!"
                ),
                "arq_title": "A SEMENTE DE TRIGO QUE BROTA DA TERRA (JOÃO 12:24)",
                "arq_text": "Poucos dias antes, o próprio Jesus havia explicado aos amigos: assim como um grão de trigo colocado na terra renasce multiplicado em muitas espigas douradas, sua entrega traria vida para o mundo inteiro!",
                "family_question": "Por que escolher o perdão e a paz, mesmo quando alguém é injusto conosco, mostra a maior força que existe no Universo?"
            },
            {
                "num": 4,
                "title": "A MANHÃ DO JARDIM ILUMINADO: ELE VIVE!",
                "ref": "Base Bíblica: Mateus 28:1–10; Marcos 16:1–8; João 20:1–18",
                "dark_mode": False,
                "art_source": "HERO_VOL9",
                "main_narrative": (
                    "No domingo bem cedinho, quando os primeiros raios dourados da aurora tocavam as oliveiras de Jerusalém, Maria Madalena e suas amigas caminharam até o jardim levando perfumes. Ao chegarem lá, pararam maravilhadas: a pesada pedra redonda havia sido rolada para o lado, e o túmulo estava completamente vazio e banhado de luz!\n\n"
                    "Dois mensageiros em vestes resplandecentes como o sol anunciaram: 'Não tenham medo! Por que vocês procuram entre os mortos Aquele que vive? Ele não está aqui: RESSUSCITOU!' E ali mesmo no jardim, Jesus vivo chamou carinhosamente: 'Maria!' e enxugou todas as suas lágrimas!"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Assim como a história humana começou num jardim (o Éden), a Nova Criação amanheceu num jardim em Jerusalém!",
                "seed_4_6": "No domingo de manhãzinha, quando o sol nasceu, a grande pedra do túmulo tinha rolado para o lado e uma luz linda brilhava lá dentro: Jesus estava vivo! Ele chamou Maria Madalena pelo nome no jardim florido e encheu o mundo inteiro de alegria!",
                "explorer_dialogue": (
                    "Chorando perto do túmulo aberto, Maria Madalena ouviu uma voz suave e conhecida atrás de si:\n"
                    "— Maria!\n"
                    "Reconhecendo na hora a voz do Mestre querido, ela voltou-se radiante de alegria:\n"
                    "— Rabôni! ('Meu Mestre!')\n"
                    "— Vá contar aos meus irmãos esta grande notícia! — pediu Jesus sorrindo. E Maria correu para anunciar aos discípulos: 'Eu vi o Senhor vivo!'"
                ),
                "arq_title": "OS TÚMULOS DE JARDIM EM JERUSALÉM",
                "arq_text": "Na Jerusalém do século I, túmulos novos escavados em rocha calcária ficavam frequentemente cercados por hortas, pomares de oliveiras e cisternas de água, exatamente como descreve João 19:41.",
                "family_question": "Maria Madalena reconheceu Jesus assim que ele a chamou pelo nome com carinho. Como você se sente quando alguém querido chama o seu nome com alegria?"
            },
            {
                "num": 5,
                "title": "OS DOIS AMIGOS NA ESTRADA DE EMAÚS",
                "ref": "Base Bíblica: Lucas 24:13–35",
                "dark_mode": False,
                "art_source": "vol3_cap6_terra_prometida.jpg",
                "main_narrative": (
                    "Na tarde daquele mesmo domingo, dois discípulos caminhavam cabisbaixos pela estrada até a aldeia de Emaús. Jesus aproximou-se e caminhou ao lado deles, explicando pelas Escrituras — desde Moisés e os Profetas — como tudo aquilo fazia parte do plano de amor de Deus.\n\n"
                    "Ao chegarem à aldeia, convidaram aquele viajante amigo: 'Fique conosco, porque já é tarde e o dia está declinando!' Quando sentaram à mesa e Jesus tomou o pão, deu graças, partiu-o e o entregou a eles, seus olhos se abriram e o reconheceram! 'Não ardia o nosso coração enquanto ele nos falava pelo caminho?'"
                ),
                "quick_box": "» VOCÊ PERCEBEU? Os dois amigos reconheceram Jesus pelo gesto carinhoso de dar graças e repartir o pão na mesa!",
                "seed_4_6": "Dois amigos caminhavam tristes pela estrada de Emaús quando Jesus veio andando junto com eles! Na hora do jantar, quando Jesus abençoou e partiu o pão quentinho na mesa, eles reconheceram o Mestre e voltaram correndo para contar a novidade!",
                "explorer_dialogue": (
                    "Assim que perceberam que era o próprio Jesus vivo quem havia partido o pão diante deles, Cléopas e seu companheiro olharam um para o outro com um sorriso imenso:\n"
                    "— Não estava o nosso coração quentinho e brilhando dentro do peito enquanto ele nos explicava as Escrituras pela estrada?\n"
                    "Naquela mesma hora levantaram-se e voltaram apressados a Jerusalém, onde encontraram os outros amigos reunidos, e Jesus apareceu no meio deles dizendo: 'Paz seja com vocês!'"
                ),
                "arq_title": "A CAMINHADA DE JERUSALÉM A EMAÚS",
                "arq_text": "A aldeia de Emaús ficava a cerca de 11 quilômetros (60 estádios) de Jerusalém, uma caminhada de duas horas pelas colinas pontilhadas de oliveiras e fontes de água da Judeia.",
                "family_question": "O que deixa o seu coração 'quentinho por dentro' de alegria quando você está reunido à mesa com a sua família?"
            },
            {
                "num": 6,
                "title": "CAFÉ DA MANHÃ NA PRAIA E A GRANDE PROMESSA",
                "ref": "Base Bíblica: João 21:1–17; Mateus 28:18–20",
                "dark_mode": False,
                "art_source": "HERO_VOL8",
                "main_narrative": (
                    "De volta ao Mar da Galileia, ao raiar do dia, os pescadores viram Jesus esperando por eles na praia ao lado de uma fogueirinha com peixe assando sobre as brasas e pão fresco: 'Venham tomar café da manhã!' Ali, à beira da água, Jesus perguntou três vezes a Simão Pedro: 'Simão, você me ama? Cuide das minhas ovelhinhas!', curando completamente a tristeza do amigo.\n\n"
                    "E no alto da montanha da Galileia, antes de subir à plenitude da Luz, deixou a promessa mais reconfortante de todas: 'Vão e ensinem o amor a todos os povos. E lembrem-se: Eu estou com vocês todos os dias, até a consumação dos séculos!'"
                ),
                "quick_box": "» PROMESSA ETERNA (MATEUS 28:20): 'Eis que Eu estou com vocês todos os dias!' — nunca caminhamos sozinhos!",
                "seed_4_6": "Na praia do lago da Galileia, Jesus preparou pão e peixinho assado para tomar café da manhã com seus amigos, abraçou Pedro com todo o perdão e prometeu para sempre: 'Eu estarei com vocês todos os dias!'",
                "explorer_dialogue": (
                    "Sentado na areia morna da praia ao lado do barco cheio de peixes, Pedro olhou para Jesus com o coração lavado de paz:\n"
                    "— Senhor, você sabe todas as coisas; você sabe que eu sou seu amigo e o amo!\n"
                    "— Então apascente os meus cordeirinhos e cuide das minhas ovelhas! — encorajou Jesus. A falha do passado havia se transformado numa nova missão de cuidado!"
                ),
                "arq_title": "AS TRÊS PERGUNTAS JUNTO AO FOGO DE BRASAS",
                "arq_text": "Observe que detalhe literário emocionante do Evangelho de João: Pedro havia negado Jesus três vezes perto de um fogo de brasas (João 18:18), e Jesus preparou outro fogo de brasas na praia (João 21:9) para restaurar Pedro três vezes pelo amor!",
                "family_question": "Como é bom saber que Jesus perdoa os nossos tropeços e ainda confia em nós para cuidarmos dos outros!"
            }
        ]
    },

    # =========================================================================
    # VOLUME 10 — A LUZ CONTINUA (Atos dos Apóstolos, Cartas do Amor e Nova Criação)
    # =========================================================================
    {
        "num": 10,
        "slug": "Volume-10-A-Luz-Continua",
        "md_file": "Volume10_A_Luz_Continua_Roteiro_e_Storyboard.md",
        "title": "A LUZ CONTINUA",
        "subtitle": "Como pequenos grupos espalharam esperança pelo mundo",
        "biblical_range": "Atos dos Apóstolos 1–28; 1 Coríntios 13; Apocalipse 21–22",
        "cover_base_prefix": "vol10_capa_base_aventura",
        "hero_art_prefix": "vol10_cap6_arvore_vida",
        "intro_text": (
            "Bem-vindo ao décimo e último volume da coleção A Grande História da Luz! A história que começou em Gênesis com o chamado 'Faça-se a Luz!' chega agora ao seu grande horizonte: como pequenos grupos de amigos cheios do Sopro de Deus espalharam a mensagem de amor, paz e fraternidade por todo o Mediterrâneo!\n\n"
            "Acompanhe o vento luminoso de Pentecostes, a generosidade dos primeiros cristãos, a transformação de Paulo, o hino ao Amor de 1 Coríntios 13 e a visão final da Árvore da Vida e do Rio Cristalino em Apocalipse 21–22!"
        ),
        "map_title": "MAPA DO MEDITERRÂNEO: DE JERUSALÉM A ANTIOQUIA, CORINTO E ROMA",
        "archaeology_section_title": "1. ARQUEOLOGIA DAS VIAGENS PELO MEDITERRÂNEO",
        "archaeology_full": (
            "• A Casa de Lídia em Filipos e os Teares de Púrpura (Atos 16): Filipos era uma cidade macedônia cortada pela famosa estrada romana Via Egnatia; junto ao rio Gangites reuniam-se mulheres trabalhadoras como Lídia, comerciante de tecidos tingidos de púrpura.\n\n"
            "• Os Navios Mercantes de Grãos do Mediterrâneo (Atos 27): Os navios a vela em que Paulo e o médico Lucas viajaram até a ilha de Malta tinham cerca de 40 metros de comprimento e transportavam trigo de Alexandria para Roma.\n\n"
            "• O Arco Completo da Bíblia (De Gênesis 1–2 a Apocalipse 21–22): A Bíblia inteira forma uma obra de arte perfeita: começa com a Luz, o Rio e a Árvore da Vida no começo de Gênesis e termina com o Rio da Água da Vida, a Árvore da Vida curando as nações e a Luz eterna em Apocalipse 22!"
        ),
        "glossary_full": (
            "• PENTECOSTES: Festa em que o Sopro Divino (Ruach / Espírito Santo) encheu os amigos de Jesus de coragem e alegria.\n"
            "• COMUNHÃO (KOINONIA): Viver como uma grande família solidária onde todos repartem o que têm com quem precisa.\n"
            "• EPÍSTOLA (CARTA): Mensagem escrita em papiro e enviada por mensageiros para encorajar as comunidades distantes.\n"
            "• ÁGAPE (AMOR): O amor paciente, bondoso e generoso descrito no capítulo 13 de 1 Coríntios.\n"
            "• NOVA CRIAÇÃO: A promessa bíblica de um mundo totalmente renovado pela justiça, pela paz e pela Luz de Deus."
        ),
        "char_notes": (
            "• PEDRO, JOÃO, BARNABÉ, LÍDIA, PRISCILA, ÁQUILA E PAULO: Retratados com autenticidade histórica do século I no mundo mediterrâneo (judeus, sírios, africanos, gregos e romanos unidos como irmãos).\n\n"
            "• CRIANÇAS DE TODAS AS NAÇÕES NO JARDIM DA LUZ (CAPÍTULO 6): Encerramento apoteótico da coleção unindo os pequenos exploradores diante do Rio da Vida e da Árvore da Vida sob o feixe dourado e safira do Criador."
        ),
        "back_cover_synopsis": (
            "'O Amor é paciente, o Amor é bondoso... Agora permanecem a fé, a esperança e o amor, estes três; mas o maior destes é o Amor!'\n\n"
            "Neste décimo volume escrito por Fábio Motta e Silva, celebramos o fechamento luminoso da coleção A Grande História da Luz, descobrindo que cada criança e cada família hoje é chamada a continuar escrevendo os capítulos do amor e da paz na Terra!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "O VENTO DA CORAGEM E TODAS AS LÍNGUAS DO MUNDO",
                "ref": "Base Bíblica: Atos dos Apóstolos 2:1–47",
                "dark_mode": True,
                "art_source": "vol1_cap1_cena2_fiat_lux.png",
                "main_narrative": (
                    "No dia da festa de Pentecostes em Jerusalém, enquanto os amigos e amigas de Jesus oravam juntos no mesmo lugar, ouviu-se de repente um som vindo do céu como um vento suave e poderoso que encheu toda a casa! Pequenas chamas de luz dourada pousaram sobre cada um deles.\n\n"
                    "Cheios do Sopro de Deus, saíram à praça falando das grandezas do Criador de tal modo que peregrinos vindos de todas as nações compreendiam em sua própria língua materna! E formaram uma comunidade alegre onde todos repartiam o pão e cuidavam uns dos outros."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Se em Babel (Vol. 1) o orgulho afastou os povos, em Pentecostes (Vol. 10) o Amor uniu todas as línguas!",
                "seed_4_6": "No dia de Pentecostes, um vento cheio de luz soprou do céu e encheu o coração dos amigos de Jesus de muita coragem! Pessoas do mundo inteiro entenderam a mensagem do amor em sua própria língua e passaram a repartir tudo como irmãos!",
                "explorer_dialogue": (
                    "— Como é possível que cada um de nós os escute falar em nossa própria língua materna sobre as maravilhas de Deus? — admiravam-se os viajantes do Egito, da Ásia, da Mesopotâmia e de Roma.\n"
                    "Naquela nova família, ninguém passava necessidade: quem tinha demais repartia com alegria com quem tinha de menos!"
                ),
                "arq_title": "OS BANHOS RITUAIS (MIKVAOT) AO SUL DO TEMPLO",
                "arq_text": "Escavações junto às escadarias sul do Monte do Templo revelaram dezenas de piscinas de pedra ('mikvaot') do século I, onde milhares de peregrinos puderam ser batizados em um único dia, como relata Atos 2:41!",
                "family_question": "Como a generosidade de repartir o que temos com quem precisa transforma uma vizinhança ou escola numa comunidade mais feliz?"
            },
            {
                "num": 2,
                "title": "LEVANTE-SE E ANDE! PEDRO, JOÃO, ESTÊVÃO E FILIPE",
                "ref": "Base Bíblica: Atos 3:1–10; 6:1–7; 8:26–40",
                "dark_mode": False,
                "art_source": "vol1_cap6_torre_babel.jpg",
                "main_narrative": (
                    "Subindo ao Templo às três horas da tarde, Pedro e João viram à Porta Formosa um homem que nunca havia conseguido andar e pedia uma moeda. Pedro olhou bem nos olhos dele e disse: 'Não tenho prata nem ouro, mas o que tenho eu lhe dou: em nome de Jesus Cristo, o Nazareno, levante-se e ande!' Segurando-o pela mão direita, o homem levantou-se saltando e louvando a Deus!\n\n"
                    "Logo escolheram sete diáconos — como o bondoso Estêvão e Filipe — para cuidar diariamente das viúvas, e na estrada de Gaza Filipe anunciou a boa notícia da Luz a um viajante africano da Etiópia, que seguiu viagem cheio de alegria!"
                ),
                "quick_box": "» VOCÊ PERCEBEU? Um olhar de atenção, uma mão estendida e a esperança valem muito mais do que prata e ouro!",
                "seed_4_6": "Na porta do Templo, Pedro e João seguraram a mão de um homem que não podia andar e disseram: 'Em nome de Jesus, levante-se!' O homem ficou curado na hora e entrou pulando de alegria! E na estrada, Filipe ensinou o amor de Deus a um viajante da África!",
                "explorer_dialogue": (
                    "Sentado em sua carruagem na estrada que descia para o sul, o tesoureiro da rainha Candace, da Etiópia, lia o rolo do profeta Isaías quando Filipe se aproximou:\n"
                    "— Você compreende o que está lendo? — perguntou Filipe com respeito.\n"
                    "Ao ouvir como Isaías falava do amor de Jesus, o viajante viu uma fonte de água fresca à beira do caminho, foi batizado ali mesmo e levou a semente da Luz até o coração da África!"
                ),
                "arq_title": "O REINO DE MEROÉ (ETIÓPIA / NÚBIA) NO SÉCULO I",
                "arq_text": "No século I, o título 'Candace' ('Kandake') designava as rainhas-mães governantes do próspero reino africano de Cuxe/Meroé, ao sul do Egito, famoso por sua cultura e comércio internacional.",
                "family_question": "Pedro olhou nos olhos de quem ninguém notava na porta. Como podemos tratar todas as pessoas que trabalham perto de nós com carinho e dignidade?"
            },
            {
                "num": 3,
                "title": "A LUZ NA ESTRADA DE DAMASCO E A CASA DE CORNÉLIO",
                "ref": "Base Bíblica: Atos 9:1–31; 10:1–48",
                "dark_mode": True,
                "art_source": "vol2_cap3_escada_jaco.jpg",
                "main_narrative": (
                    "Saulo de Tarso perseguia os seguidores de Jesus achando que estava fazendo o certo. Mas, na estrada de Damasco, ao meio-dia, uma Luz do céu mais brilhante que o sol envolveu Saulo e transformou completamente o seu coração! Acolhido pelo corajoso Ananias e pelo amigo Barnabé ('Filho da Consolação'), Saulo tornou-se o apóstolo Paulo, o maior mensageiro da graça!\n\n"
                    "Ao mesmo tempo, na cidade costeira de Cesareia, Pedro visitou a casa do bondoso centurião Cornélio e compreendeu uma verdade libertadora: 'Reconheço por verdade que Deus não faz acepção de pessoas, mas acolhe em qualquer nação quem O ama e pratica a justiça!'"
                ),
                "quick_box": "» O QUE VOCÊ FARIA? Barnabé acreditou na mudança de Paulo quando todos ainda tinham medo dele — e ganhou um grande irmão!",
                "seed_4_6": "Na estrada de Damasco, uma Luz fortíssima brilhou sobre Saulo e mudou seu coração: ele deixou de brigar com os cristãos e virou o apóstolo Paulo, grande amigo de Jesus! E Pedro aprendeu que Deus ama igualmente as pessoas de todos os países!",
                "explorer_dialogue": (
                    "Entrando numa casa na Rua Direita, em Damasco, o discípulo Ananias colocou as mãos com brandura sobre os ombros de Saulo e disse:\n"
                    "— Irmão Saulo, o Senhor Jesus, que lhe apareceu na luz pelo caminho, enviou-me para que você volte a enxergar e fique cheio do Espírito Santo!\n"
                    "Chamado de 'irmão' por aqueles que antes perseguia, Paulo dedicou o resto da vida a construir pontes entre os povos."
                ),
                "arq_title": "A 'RUA DIREITA' DE DAMASCO E O PORTO DE CESAREIA",
                "arq_text": "A famosa 'Via Recta' (Rua Direita) mencionada em Atos 9:11 atravessa até hoje o centro histórico de Damasco de leste a oeste por 1.500 metros, preservando arcos romanos do século I!",
                "family_question": "Barnabé tinha o apelido de 'Filho do Encorajamento' porque sempre animava os outros. Como você pode encorajar alguém hoje?"
            },
            {
                "num": 4,
                "title": "VIAGENS PELO MAR, A CASA DE LÍDIA E AS CARTAS NA TEMPESTADE",
                "ref": "Base Bíblica: Atos 16:11–40; 18:1–4; 27:13–44",
                "dark_mode": True,
                "art_source": "vol3_cap4_travessia_mar.jpg",
                "main_narrative": (
                    "Navegando pelo mar Mediterrâneo com Barnabé, Silas, Timóteo e o médico Lucas, Paulo levou a mensagem da Luz a muitas cidades. Em Filipos, a generosa comerciante Lídia abriu sua casa à beira do rio para acolher a comunidade; em Corinto, o casal de artesãos Priscila e Áquila trabalhou fazendo tendas ao lado de Paulo.\n\n"
                    "Anos depois, quando o navio em que Paulo viajava enfrentou quatorze dias de tempestade no mar rumo a Malta, Paulo partiu o pão no convés e encorajou a todos os 276 passageiros: 'Tenham bom ânimo! Nenhum de vocês se perderá!' E todos chegaram salvos à praia!"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Mulheres sábias como Lídia, Priscila e Febe foram líderes fundamentais das primeiras comunidades!",
                "seed_4_6": "Paulo e seus amigos viajaram de navio levando o amor de Jesus para muitas cidades! Eles conheceram amigas generosas como Lídia e Priscila e, mesmo durante uma grande tempestade no mar, mantiveram a calma e ajudaram todos do navio a chegar seguros à ilha de Malta!",
                "explorer_dialogue": (
                    "Sentados na oficina de couro e lona em Corinto, Priscila, Áquila e Paulo costuravam tendas enquanto conversavam com os moradores da cidade:\n"
                    "— O trabalho das nossas mãos sustenta a casa — dizia Priscila sorrindo —, e a nossa mesa aberta mostra que na família de Cristo não há divisão entre povos: somos todos um!"
                ),
                "arq_title": "A ILHA DE MALTA E A BAÍA DE SÃO PAULO",
                "arq_text": "Os detalhes náuticos de Atos 27 (escritos pelo médico Lucas, que estava a bordo!) descrevem com precisão cirúrgica os ventos do Mediterrâneo e as profundidades medidas pela sonda na costa da ilha de Malta.",
                "family_question": "No meio da tempestade no navio, Paulo acalmou 276 pessoas com palavras de fé e repartindo o pão. Como a calma de uma pessoa ajuda todo o grupo?"
            },
            {
                "num": 5,
                "title": "O SEGREDO MAIOR DO UNIVERSO: O HINO AO AMOR",
                "ref": "Base Bíblica: 1 Coríntios 13:1–13; Filipenses 4:4–8; 1 João 4:7–8",
                "dark_mode": False,
                "art_source": "vol2_cap2_riso_isaque.jpg",
                "main_narrative": (
                    "Para ensinar às famílias e comunidades como viver em harmonia, os apóstolos escreveram cartas preciosas em rolos de papiro. Na primeira carta aos Coríntios, Paulo escreveu o poema mais belo de toda a história sobre o verdadeiro Amor:\n\n"
                    "— Ainda que eu falasse a língua dos homens e dos anjos, se não tivesse Amor, nada seria! O Amor é paciente, o Amor é bondoso. Não tem inveja, não é orgulhoso, não é grosseiro, não procura apenas os seus próprios interesses, não guarda rancor e não se alegra com a injustiça, mas se alegra com a verdade! E o apóstolo João resumiu tudo numa frase: 'Amados, amemo-nos uns aos outros, porque Deus é Amor!'"
                ),
                "quick_box": "» PARA GUARDAR NO CORAÇÃO (1 CORÍNTIOS 13:4): 'O Amor é paciente, o Amor é bondoso!'",
                "seed_4_6": "Nas cartinhas que escreveram para as famílias, Paulo e João ensinaram o maior segredo da Bíblia inteira: 'O Amor é paciente, o Amor é bondoso, não tem inveja nem guarda mágoa — porque Deus é Amor!'",
                "explorer_dialogue": (
                    "— Tudo o que é verdadeiro, tudo o que é respeitável, tudo o que é justo, tudo o que é puro, tudo o que é amável e de boa fama — escreveu Paulo na carta aos amigos de Filipos —, nisso pensem e isso pratiquem, e o Deus da paz estará sempre com vocês!"
                ),
                "arq_title": "AS CARTAS EM PAPIRO E A PORTADORA FEBE (ROMANOS 16:1)",
                "arq_text": "As cartas do Novo Testamento eram ditadas a um escriba em folhas de papiro e levadas em mãos por mensageiros de confiança — como Febe, de Cencreia, que atravessou o mar para entregar a carta aos Romanos!",
                "family_question": "Escolha uma qualidade do amor de 1 Coríntios 13 (paciência, bondade, não ter inveja, perdoar rápido) para praticar de um jeito especial hoje!"
            },
            {
                "num": 6,
                "title": "O RIO DA VIDA E A LUZ QUE NUNCA SE APAGA",
                "ref": "Base Bíblica: Apocalipse 21:1–5; 22:1–5 (O Grande Horizonte da Nova Criação)",
                "dark_mode": False,
                "art_source": "HERO_VOL10",
                "main_narrative": (
                    "Na ilha de Patmos, o idoso apóstolo João contemplou em visão o grande horizonte final preparado pelo Criador para toda a existência: um Novo Céu e uma Nova Terra banhados de paz, onde Deus habita com a família humana e enxuga dos olhos toda lágrima!\n\n"
                    "No centro da Cidade da Luz corre o Rio da Água da Vida, claro como cristal, e em suas duas margens floresce a Árvore da Vida, dando doze colheitas de frutos doces e cujas folhas servem para a cura e a paz de todas as nações! Ali nunca mais haverá escuridão nem medo, porque a própria Presença do Senhor Deus ilumina tudo para sempre — e a Grande História da Luz continua hoje em cada coração que escolhe amar!"
                ),
                "quick_box": "» ARCO COMPLETO DA COLEÇÃO: De Gênesis 1 ('Faça-se a Luz!') a Apocalipse 22 ('O Senhor os iluminará!'), o Amor venceu!",
                "seed_4_6": "No final da Bíblia, o velho amigo João viu o lindo jardim da Nova Criação: um rio brilhante como cristal e a Árvore da Vida cheia de frutos doces e folhas que trazem paz para todas as crianças e famílias do mundo! E a Luz de Deus brilha hoje dentro do seu coração!",
                "explorer_dialogue": (
                    "Olhando juntos para o horizonte banhado de luz dourada e azul-safira, os dois pequenos exploradores da nossa coleção fecharam o último pergaminho com um sorriso:\n"
                    "— Você viu como tudo se conecta desde o primeiro capítulo? — disse a menina.\n"
                    "— A história não acabou no livro — respondeu o menino, estendendo a mão para você, leitor. — Toda vez que cuidamos da natureza, dizemos a verdade, perdoamos um irmão e ajudamos quem precisa, nós fazemos a Luz de Deus continuar brilhando na Terra!"
                ),
                "arq_title": "A SIMETRIA PERFEITA DA BÍBLIA: DO ÉDEN À NOVA JERUSALÉM",
                "arq_text": "Os dois primeiros capítulos da Bíblia (Gênesis 1–2) e os dois últimos (Apocalipse 21–22) funcionam como duas capas gêmeas de uma sinfonia: a luz, os rios cristalinos e a Árvore da Vida do princípio retornam agora abertos para todas as nações da Terra!",
                "family_question": "Parabéns, Pequeno Explorador! Depois de viajar pelos 10 volumes de 'A Grande História da Luz', qual foi a sua história favorita de toda a coleção?"
            }
        ]
    }
]
