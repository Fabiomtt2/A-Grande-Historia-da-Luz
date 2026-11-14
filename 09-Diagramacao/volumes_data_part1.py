#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banco de Dados Literário, Histórico e Pedagógico — Volumes 4 a 10
Coleção: A Grande História da Luz — A Bíblia Ilustrada para Pequenos Exploradores
Autor: Fábio Motta e Silva (Publicação Independente / Autônoma)
Contém os roteiros completos em Dupla Camada (4-6 anos e 6-10 anos), diálogos,
descobertas arqueológicas, perguntas familiares e storyboards de 64 páginas dos Volumes 4 a 10.
"""

VOLUMES_DATA = [
    # =========================================================================
    # VOLUME 4 — CORAGEM PARA MUDAR O MUNDO (Josué, Juízes, Rute, Samuel, Davi e Salomão)
    # =========================================================================
    {
        "num": 4,
        "slug": "Volume-4-Coragem-para-Mudar-o-Mundo",
        "md_file": "Volume4_Coragem_para_Mudar_o_Mundo_Roteiro_e_Storyboard.md",
        "title": "CORAGEM PARA MUDAR O MUNDO",
        "subtitle": "Juízes, amigos fiéis, pastores e reis",
        "biblical_range": "Josué, Juízes, Rute, 1 e 2 Samuel e 1 Reis 1–10",
        "cover_base_prefix": "vol4_capa_base_aventura",
        "hero_art_prefix": "vol4_cap4_davi_harpa",
        "intro_text": (
            "Bem-vindo ao quarto volume da coleção A Grande História da Luz! Depois da longa caminhada pelo deserto, o povo finalmente atravessou o rio Jordão e chegou às colinas verdes da Terra Prometida.\n\n"
            "Aqui você vai conhecer líderes corajosos como Josué e a sábia juíza Débora, a emocionante amizade de Rute e Noemi nos campos de trigo de Belém, o menino Samuel que ouviu a Voz da Luz à noite, o jovem pastor Davi com sua harpa e o sábio rei Salomão!"
        ),
        "map_title": "MAPA HISTÓRICO: DO RIO JORDÃO A BELÉM E JERUSALÉM",
        "archaeology_section_title": "1. ARQUEOLOGIA DA TERRA DE ISRAEL (IDADE DO FERRO)",
        "archaeology_full": (
            "• As Pedras do Rio Jordão e Jericó: Uma das cidades mais antigas do mundo, Jericó ficava num oásis fértil cercado de palmeiras perto do rio Jordão, protegida por muralhas de pedra e tijolos de barro.\n\n"
            "• A Colheita de Cevada em Belém (Livro de Rute): Na antiguidade bíblica, a lei do Criador ordenava que os donos dos campos deixassem espigas nas bordas da plantação para que os pobres, as viúvas e os estrangeiros pudessem colher com dignidade.\n\n"
            "• A Harpa de Davi (Kinor): O instrumento tocado por Davi nos campos de Belém era o 'kinor', uma pequena lira portátil de madeira com cordas de fibra, cuja música acalmava o coração."
        ),
        "glossary_full": (
            "• JORDÃO: O principal rio da Terra Prometida, que corre do Mar da Galileia até o Mar Morto.\n"
            "• JUÍZES: Líderes levantados para defender o povo e ensinar a justiça antes de existirem reis.\n"
            "• RESPIGAR: Recolher as espigas de trigo e cevada deixadas no campo após a colheita principal.\n"
            "• KINOR (HARPA): Instrumento musical de cordas tocado pelo pastor Davi para compor os Salmos.\n"
            "• SABEDORIA: O dom de ouvir, compreender o coração das pessoas e escolher o caminho justo."
        ),
        "char_notes": (
            "• JOSUÉ E DÉBORA: Vestem túnicas de linho e mantos de lã tecida característicos das colinas de Efraim; Débora atende o povo à sombra de uma grande tamareira.\n\n"
            "• RUTE E NOEMI: Trajes simples de caminhada e colheita em tons terrosos e ocre, carregando feixes dourados de cevada nos campos de Belém.\n\n"
            "• DAVI E SALOMÃO: Davi aparece na juventude como pastor ruivo-moreno de olhos vivos com sua harpa de madeira e funda de couro; Salomão veste linho real bordado em azul e ouro no Templo de Jerusalém."
        ),
        "back_cover_synopsis": (
            "'Seja forte e corajoso! Não tenha medo, pois a Luz do Senhor estará com você por onde quer que vá!'\n\n"
            "Neste quarto volume escrito por Fábio Motta e Silva, crianças de 4 a 10 anos descobrem que a verdadeira coragem não depende da força física nem da altura, mas de um coração fiel, amigo e cheio de sabedoria.\n\n"
            "NO PRÓXIMO VOLUME (VOLUME 5 — VOZES DE SABEDORIA E ESPERANÇA):\n"
            "Acompanhe os profetas Elias, Isaías, Jonas e Daniel, a corajosa rainha Ester e a poesia dos Salmos!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "AS DOZE PEDRAS NO RIO E A PALMEIRA DE DÉBORA",
                "ref": "Base Bíblica: Josué 1–4; Juízes 4–5",
                "dark_mode": False,
                "art_source": "vol3_cap6_terra_prometida.jpg",
                "main_narrative": (
                    "Quando o povo atravessou o rio Jordão a pé enxuto com Josué, doze pedras foram erguidas na margem como um memorial: quando os filhos perguntassem no futuro 'O que significam estas pedras?', os pais contariam como a Luz de Deus abriu o caminho!\n\n"
                    "Mais tarde, nos dias dos Juízes, uma mulher sábia e corajosa chamada Débora sentava-se debaixo de uma grande palmeira para ouvir o povo, promover a paz e cantar a vitória da justiça."
                ),
                "quick_box": "» VOCÊ PERCEBEU? As doze pedras de Gilgal funcionavam como um livro de memória ao ar livre para as crianças!",
                "seed_4_6": "Josué guiou as famílias para atravessar o rio Jordão e pediu para guardarem doze pedras na margem como lembrança do cuidado de Deus! Anos depois, debaixo de uma palmeira fresquinha, a sábia Débora ajudava todo o povo a viver em paz.",
                "explorer_dialogue": (
                    "— Papai, por que vocês estão empilhando estas doze pedras redondas aqui na margem? — perguntou uma menina curiosa.\n"
                    "— Para que você e seus filhos nunca se esqueçam deste dia! — sorriu Josué. — Toda vez que olharem para elas, lembrarão que o Criador secou as águas do Jordão assim como fez no Mar Vermelho!\n"
                    "E sob a sombra da palmeira nas montanhas de Efraim, a profetisa Débora ensinava com firmeza: quando o povo caminha unido na luz da justiça, nenhum exército opressor pode vencer a esperança!"
                ),
                "arq_title": "A PALMEIRA DE DÉBORA E OS MEMORIAIS DE PEDRA",
                "arq_text": "Na cultura bíblica, erguer pilhas de pedras naturais ('ebenezer' ou memoriais) era uma forma visual de ensinar história às crianças que passavam pelas estradas.",
                "family_question": "Qual objeto, foto ou lembrança especial da sua casa ajuda a família a recordar um dia muito feliz?"
            },
            {
                "num": 2,
                "title": "RUTE E NOEMI: A AMIZADE NOS CAMPOS DE BELÉM",
                "ref": "Base Bíblica: Rute 1–4",
                "dark_mode": False,
                "art_source": "vol1_cap4_caim_abel.jpg",
                "main_narrative": (
                    "Quando a viúva Noemi precisou voltar sozinha e triste para a cidade de Belém, sua nora Rute recusou-se a abandoná-la e disse uma das frases mais bonitas da Bíblia: 'Aonde você for, eu irei; o seu povo será o meu povo, e o seu Deus será o meu Deus!'\n\n"
                    "Nos campos dourados de cevada em Belém, o bondoso Boaz viu o carinho com que Rute cuidava de Noemi e a acolheu em sua família — tornando Rute bisavó do rei Davi!"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Belém significa 'Casa do Pão' em hebraico, por causa de seus campos férteis de trigo e cevada!",
                "seed_4_6": "Noemi estava muito triste e sozinha, mas sua grande amiga Rute segurou sua mão e disse: 'Eu nunca vou deixar você sozinha!' Juntas elas foram para Belém, onde Rute colheu espigas de trigo e encontrou uma nova família cheia de amor!",
                "explorer_dialogue": (
                    "Sob o sol morno da manhã em Belém, Rute juntava com paciência as espigas de cevada deixadas pelos trabalhadores para levar pão à sua sogra Noemi.\n"
                    "Boaz aproximou-se com respeito e disse a ela:\n"
                    "— Contaram-me tudo o que você tem feito por sua sogra Noemi desde que deixou a sua terra natal. Que o Senhor recompense a sua bondade, e que você encontre abrigo debaixo das asas do Deus de Israel!"
                ),
                "arq_title": "A LEI DA SOLIDARIEDADE NA COLHEITA (LEVÍTICO 19:9)",
                "arq_text": "No antigo Israel, os agricultores não colhiam os cantos do campo nem voltavam para pegar espigas caídas: tudo isso ficava reservado gratuitamente para alimentar os órfãos, as viúvas e os viajantes.",
                "family_question": "Rute mostrou que um amigo de verdade fica ao nosso lado mesmo nos dias difíceis. Quem é um grande exemplo de amizade na sua vida?"
            },
            {
                "num": 3,
                "title": "FALA, SENHOR! O CHAMADO DO PEQUENO SAMUEL",
                "ref": "Base Bíblica: 1 Samuel 1–3",
                "dark_mode": True,
                "art_source": "vol3_cap3_noite_liberdade.jpg",
                "main_narrative": (
                    "O menino Samuel cresceu ajudando o idoso sacerdote Eli na tenda sagrada de Siló. Certa noite, enquanto a lâmpada de azeite ainda brilhava suave no silêncio, uma Voz carinhosa chamou: 'Samuel! Samuel!'\n\n"
                    "Três vezes o menino correu até Eli achando que o velho mestre o chamava, até que Eli compreendeu o mistério e o ensinou a responder: 'Fala, Senhor, porque o teu servo está ouvindo!' E a Luz de Deus fez de Samuel um grande profeta."
                ),
                "quick_box": "» CONVERSE COMIGO: Deus conhece até o nome de uma criança pequena e fala ao coração que sabe ouvir!",
                "seed_4_6": "De noite, enquanto todo mundo dormia, o pequeno Samuel ouviu uma Voz doce chamando seu nome três vezes! O velho Eli sorriu e explicou que era a Voz de Deus. Então Samuel respondeu: 'Pode falar, Senhor, eu estou ouvindo!'",
                "explorer_dialogue": (
                    "Samuel esfregou os olhos e correu descalço pelo tapete até o quarto do idoso Eli:\n"
                    "— Aqui estou, senhor! O senhor me chamou pela terceira vez!\n"
                    "Eli abriu um sorriso sereno sob a luz dourada da lamparina de barro:\n"
                    "— Meu filho, é a Presença do Senhor quem está chamando você! Volte a deitar-se e, quando ouvir o chamado outra vez, diga no seu coração: 'Fala, Senhor, porque o teu pequeno servo está ouvindo!'"
                ),
                "arq_title": "AS LAMPARINAS DE AZEITE DE OLIVA",
                "arq_text": "Antes da eletricidade, as casas e o santuário de Israel eram iluminados à noite por pequenas lâmpadas de cerâmica abastecidas com azeite puro de oliva prensado e um pavio de linho.",
                "family_question": "Como podemos fazer um pouquinho de silêncio no nosso dia agitado para ouvir a voz da sabedoria e da bondade no coração?"
            },
            {
                "num": 4,
                "title": "O JOVEM PASTOR, A HARPA E O GIGANTE",
                "ref": "Base Bíblica: 1 Samuel 16–17",
                "dark_mode": False,
                "art_source": "HERO_VOL4",
                "main_narrative": (
                    "Quando Samuel foi a Belém ungir o novo rei, aprendeu um segredo eterno: 'As pessoas olham para a aparência de fora, mas o Senhor olha para o coração!' O escolhido foi Davi, o filho caçula que cuidava das ovelhas cantando salmos na harpa.\n\n"
                    "Diante do guerreiro gigante Golias, que assustava todo o exército com sua armadura pesada, o jovem Davi avançou apenas com seu cajado, cinco pedrinhas do riacho e uma confiança inabalável na Luz de Deus, trazendo paz ao vale!"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: 'O Senhor não vê como o homem vê: o homem olha a aparência, mas Deus vê o coração!' (1 Sm 16:7).",
                "seed_4_6": "Davi era o irmão mais novo e cuidava das ovelhinhas tocando sua harpa no campo. Quando um gigante grandalhão assustou todo mundo, Davi não teve medo: ele confiou na proteção de Deus e mostrou que a coragem do coração é maior que qualquer armadura!",
                "explorer_dialogue": (
                    "No vale de Elá, o rei Saul tentou vestir Davi com um capacete de bronze e uma couraça pesada, mas o menino mal conseguia dar dois passos:\n"
                    "— Eu não consigo caminhar com tudo isso — disse Davi, tirando a armadura. — O mesmo Deus que me protegeu das garras do leão e do urso quando eu defendia minhas ovelhas em Belém também guardará o nosso povo hoje!\n"
                    "E com coragem serena, Davi provou que a fé vale mais do que espadas e lanças."
                ),
                "arq_title": "O VALE DE ELÁ E A CIDADE DE QUIRBET QEIYAFA",
                "arq_text": "Escavações arqueológicas recentes nas colinas que margeiam o Vale de Elá descobriram uma cidade fortificada do século X a.C. (época do rei Davi) com duas portas monumentais e inscrições em hebraico antigo!",
                "family_question": "Por que a bondade, a honestidade e a coragem dentro do coração de uma pessoa são muito mais importantes do que a altura ou a força dela?"
            },
            {
                "num": 5,
                "title": "A AMIZADE DE DAVI E JÔNATAS E O REI POETA",
                "ref": "Base Bíblica: 1 Samuel 18–20; 2 Samuel 5 e 9; Salmo 23",
                "dark_mode": True,
                "art_source": "vol1_cap1_cena8_descanso_luz.png",
                "main_narrative": (
                    "No palácio, Davi ganhou um amigo leal como um irmão: o príncipe Jônatas, filho de Saul. Mesmo sabendo que Davi seria o próximo rei, Jônatas nunca sentiu inveja; ao contrário, protegeu Davi e fez com ele uma aliança eterna de amizade!\n\n"
                    "Quando se tornou rei em Jerusalém, Davi honrou sua promessa acolhendo na mesa real o filho de Jônatas, Mefibosete, que tinha os pés feridos, e escreveu belas canções como o Salmo 23: 'O Senhor é o meu Pastor, nada me faltará!'"
                ),
                "quick_box": "» VOCÊ PERCEBEU? Ao contrário dos irmãos de José, o príncipe Jônatas venceu qualquer ciúme com uma amizade verdadeira!",
                "seed_4_6": "O príncipe Jônatas e o pastor Davi se tornaram os melhores amigos do mundo! Eles prometeram sempre cuidar da família um do outro. Quando Davi virou rei, ele compôs lindas músicas chamadas Salmos lembrando que Deus cuida de nós como um bom pastor!",
                "explorer_dialogue": (
                    "Sentado à mesa do palácio de Jerusalém, o rei Davi olhou com ternura para o jovem Mefibosete, filho de seu falecido amigo Jônatas:\n"
                    "— Não tenha medo, Mefibosete! Por amor ao seu pai Jônatas, devolvo a você todas as terras de sua família, e a partir de hoje você comerá sempre aqui à minha mesa, como um dos meus próprios filhos!\n"
                    "A promessa da amizade havia atravessado os anos sem se quebrar."
                ),
                "arq_title": "A INSCRIÇÃO DA 'CASA DE DAVI' EM TEL DAN",
                "arq_text": "Em 1993, arqueólogos encontraram no norte de Israel uma estela de basalto do século IX a.C. que menciona explicitamente em escrita aramaica antiga a 'Casa de Davi' (Beit David), confirmando a linhagem histórica do rei poeta!",
                "family_question": "No Salmo 23, Davi diz que Deus nos guia para águas tranquilas e pastos verdinhos. O que traz paz ao seu coração quando você está cansado?"
            },
            {
                "num": 6,
                "title": "O PEDIDO DE SALOMÃO E A CASA DE LUZ",
                "ref": "Base Bíblica: 1 Reis 3:5–14; 6 e 8",
                "dark_mode": False,
                "art_source": "vol1_cap6_torre_babel.jpg",
                "main_narrative": (
                    "Quando o jovem Salomão, filho de Davi, subiu ao trono, a Presença Luminosa do Criador falou com ele num sonho em Gibeão: 'Peça o que você quiser que Eu lhe dê!' Em vez de pedir ouro, fama ou vitória sobre inimigos, Salomão pediu um coração sábio que soubesse ouvir e julgar com justiça.\n\n"
                    "Alegre com essa escolha, Deus deu a Salomão imensa sabedoria para escrever provérbios, estudar as plantas e os animais e erguer em Jerusalém o belo Templo dedicado ao nome do Senhor!"
                ),
                "quick_box": "» O QUE VOCÊ FARIA? Se você pudesse pedir um dom especial para ajudar as pessoas, qual sabedoria você escolheria?",
                "seed_4_6": "Quando Salomão se tornou rei, Deus perguntou em sonho o que ele gostaria de ganhar. Salomão não pediu brinquedos nem ouro: pediu um coração sábio para ajudar as pessoas com bondade! E no monte de Jerusalém ele construiu uma linda casa de oração.",
                "explorer_dialogue": (
                    "— Senhor meu Deus — orou o jovem Salomão de joelhos —, eu ainda sou muito jovem e não sei como governar um povo tão grande. Dá ao teu servo um coração que saiba escutar, para distinguir entre o bem e o mal!\n"
                    "E quando o Templo de pedra branca e madeira perfumada de cedro ficou pronto em Jerusalém, uma nuvem resplandecente de luz dourada encheu todo o pátio, mostrando que a Presença Divina habita onde há justiça e oração."
                ),
                "arq_title": "OS CEDROS DO LÍBANO E AS PEDRAS DE JERUSALÉM",
                "arq_text": "Para construir o Templo sem barulho de martelos de ferro no local sagrado, as pedras calcárias brancas (chamadas 'meleke') eram talhadas sob medida nas pedreiras subterrâneas de Jerusalém antes de serem encaixadas!",
                "family_question": "Salomão pediu um 'coração que sabe escutar'. Por que ouvir com atenção o que o outro está sentindo é o primeiro passo da sabedoria?"
            }
        ]
    },

    # =========================================================================
    # VOLUME 5 — VOZES DE SABEDORIA E ESPERANÇA (Elias, Jonas, Isaías, Daniel, Ester, Salmos)
    # =========================================================================
    {
        "num": 5,
        "slug": "Volume-5-Vozes-de-Sabedoria-e-Esperanca",
        "md_file": "Volume5_Vozes_de_Sabedoria_e_Esperanca_Roteiro_e_Storyboard.md",
        "title": "VOZES DE SABEDORIA E ESPERANÇA",
        "subtitle": "Poetas, profetas e guardiões da justiça",
        "biblical_range": "1 Reis 17–19; Jonas; Isaías; Daniel; Ester; Salmos e Provérbios",
        "cover_base_prefix": "vol5_capa_base_aventura",
        "hero_art_prefix": "vol5_cap4_daniel_ester",
        "intro_text": (
            "Bem-vindo ao quinto volume da coleção A Grande História da Luz! Ao longo dos séculos, sempre que os reis e o povo se esqueciam de cuidar dos pobres e de andar na verdade, a Luz do Criador levantava mensageiros corajosos chamados Profetas.\n\n"
            "Neste livro você ouvirá a brisa suave que consolou Elias na caverna, mergulhará no mar com Jonas, sonhará com o mundo de paz de Isaías, entrará na cova dos leões com Daniel e verá a coragem da rainha Ester!"
        ),
        "map_title": "MAPA HISTÓRICO: DE ISRAEL A NÍNIVE, BABILÔNIA E SUSÃ",
        "archaeology_section_title": "1. ARQUEOLOGIA DOS PROFETAS E DOS IMPÉRIOS ANTIGOS",
        "archaeology_full": (
            "• O Grande Rolo de Isaías (Manuscritos do Mar Morto): Encontrado numa caverna em Qumran em 1947, o rolo completo do profeta Isaías em pergaminho tem mais de 2.100 anos e preserva as mesmas palavras de esperança e paz que lemos hoje!\n\n"
            "• Os Leões nos Murais da Babilônia (Porta de Ishtar): Os palácios da antiga Babilônia (época de Daniel) tinham avenidas inteiras decoradas com tijolos vitrificados azuis e relevos dourados de leões reais.\n\n"
            "• O Palácio de Inverno em Susã (Livro de Ester): Arqueólogos escavaram na antiga Pérsia as colunas monumentais e os pátios reais de Susã exatamente como descritos na história de Ester e Mardoqueu."
        ),
        "glossary_full": (
            "• PROFETA: Mensageiro que fala em nome de Deus para chamar o povo de volta ao amor, à verdade e à justiça.\n"
            "• COMPAIXÃO: Sentimento profundo de carinho que deseja ajudar e perdoar quem está sofrendo ou arrependido.\n"
            "• PROVÉRBIO: Frase curta e sábia que ensina como tomar boas decisões no dia a dia.\n"
            "• EXÍLIO: Período em que muitas famílias de Judá viveram longe de sua terra, na Babilônia, mantendo viva a fé.\n"
            "• PONTES DA HISTÓRIA: O período entre o Antigo e o Novo Testamento (época persa, grega e romana)."
        ),
        "char_notes": (
            "• ELIAS E ISAÍAS: Elias veste manto rústico de lã de pastor nas montanhas do Carmelo e Horebe; Isaías aparece em Jerusalém com rolo de pergaminho e túnica de linho.\n\n"
            "• DANIEL E SEUS AMIGOS: Jovens judeus na corte babilônica mantendo a serenidade, a oração diária na janela voltada para Jerusalém e a integridade.\n\n"
            "• RAINHA ESTER: Jovem judia órfã criada por seu primo Mardoqueu, vestindo trajes reais persas em tons de safira, turquesa e fios dourados no palácio de Susã."
        ),
        "back_cover_synopsis": (
            "Onde está a voz de Deus? Não no vento destruidor, nem no terremoto, nem no fogo — mas na brisa mansa e suave que fala ao coração!\n\n"
            "Neste quinto volume escrito por Fábio Motta e Silva, encerramos a jornada pelo Antigo Testamento conhecendo os grandes profetas, a coragem de Daniel e da rainha Ester e a sabedoria poética que preparou o mundo para o nascimento de Jesus no Volume 6!"
        ),
        "chapters": [
            {
                "num": 1,
                "title": "ELIAS E O SUSSURRO DA BRISA SUAVE",
                "ref": "Base Bíblica: 1 Reis 17–19; 2 Reis 2",
                "dark_mode": True,
                "art_source": "vol3_cap2_sarca_luz.jpg",
                "main_narrative": (
                    "Quando o profeta Elias sentiu-se cansado, triste e sozinho numa caverna no monte Horebe, a Presença Divina cuidou dele primeiro com pão quente assado sobre brasas, uma bilha de água fresca e um bom descanso.\n\n"
                    "Depois, lá fora, soprou um vento fortíssimo, houve um terremoto e brilhou um fogo intenso — mas o Senhor não estava na violência. Então veio o som de uma brisa mansa, suave e luminosa, que renovou a coragem de Elias e o levou a treinar seu amigo Eliseu!"
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Quando estamos exaustos, Deus cuida até do nosso descanso, da nossa sede e do nosso alimento!",
                "seed_4_6": "O profeta Elias estava muito cansado e triste numa caverna. Primeiro Deus mandou pão quentinho e água fresca para ele descansar! Depois, em vez de falar no barulho da tempestade, Deus falou com Elias numa brisa bem calminha e suave.",
                "explorer_dialogue": (
                    "Na entrada da caverna do monte Horebe, Elias envolveu o rosto no manto ao sentir a brisa luminosa e mansa:\n"
                    "— O que você está fazendo aqui, Elias? — perguntou a Voz suave.\n"
                    "— Eu fiquei sozinho tentando defender a verdade! — desabafou o profeta.\n"
                    "— Você não está sozinho! — consolou a Luz. — Ainda há milhares de corações fiéis, e o jovem Eliseu caminhará ao seu lado como um filho!"
                ),
                "arq_title": "AS CAVERNAS DO MONTE CARMELO E DO SINAI",
                "arq_text": "As montanhas calcárias de Israel e os vales graníticos do Sinai possuem centenas de cavernas naturais frescas que serviam de abrigo para pastores, viajantes e profetas.",
                "family_question": "Por que uma conversa calma e carinhosa funciona muito melhor para tocar o coração de alguém do que gritos e barulho?"
            },
            {
                "num": 2,
                "title": "JONAS E O MAR DA SEGUNDA CHANCE",
                "ref": "Base Bíblica: Jonas 1–4",
                "dark_mode": True,
                "art_source": "vol1_cap1_cena4_estrelas_e_vida.png",
                "main_narrative": (
                    "Quando Deus enviou o profeta Jonas para chamar os moradores da grande cidade de Nínive ao arrependimento, Jonas quis fugir num barco para a direção oposta! No meio da tempestade no mar, um grande peixe serviu de abrigo para salvar a vida de Jonas e levá-lo de volta à praia.\n\n"
                    "Ao pregar em Nínive, toda a cidade mudou de atitude e foi perdoada! E debaixo de uma plantinha que dava sombra, Jonas aprendeu que a compaixão de Deus abraça todos os povos e até os animais."
                ),
                "quick_box": "» O QUE VOCÊ FARIA? Jonas descobriu que o amor de Deus dá uma segunda chance tanto ao profeta fujão quanto à cidade inteira!",
                "seed_4_6": "Jonas tentou fugir num navio para não ir à cidade de Nínive, mas um grande peixe o salvou no fundo do mar e o levou até a praia! Quando as pessoas de Nínive ouviram Jonas e pediram desculpas pelos seus erros, Deus perdoou todo mundo com alegria!",
                "explorer_dialogue": (
                    "Sentado a leste da cidade de Nínive, Jonas reclamava do calor quando ouviu a pergunta sábia e paciente da Luz do Criador:\n"
                    "— Jonas, você ficou tão triste por causa de uma simples planta que nasceu numa noite e secou na outra... E Eu não teria compaixão de Nínive, uma cidade tão grande onde vivem mais de cento e vinte mil crianças pequeninas e tantos animais?"
                ),
                "arq_title": "O PORTO DE JOPE E A GRANDE CIDADE DE NÍNIVE",
                "arq_text": "Jope (atual Jafa, em Israel) é um dos portos marítimos mais antigos do Mediterrâneo; já Nínive ficava às margens do rio Tigre, na Mesopotâmia, cercada por imensos jardins e canais.",
                "family_question": "Por que é tão importante acreditar que as pessoas podem mudar para melhor e dar a elas uma nova oportunidade?"
            },
            {
                "num": 3,
                "title": "ISAÍAS E O SONHO DO MUNDO EM PAZ",
                "ref": "Base Bíblica: Isaías 6; 9:2, 6; 11:6–9; 40:31",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena5_animais_jardim.jpg",
                "main_narrative": (
                    "Em tempos de medo e ameaça de guerra em Jerusalém, o profeta Isaías respondeu ao chamado da Luz dizendo: 'Eis-me aqui, envia-me a mim!' Ele anunciou que o povo que caminhava no escuro veria uma Grande Luz: nasceria um Menino chamado Príncipe da Paz!\n\n"
                    "Isaías pintou com palavras o sonho mais belo para a Terra: o dia em que os povos transformarão espadas em arados de plantar trigo, o lobo e o cordeiro descansarão juntos, e uma criança pequena os guiará em segurança."
                ),
                "quick_box": "» VOCÊ PERCEBEU? Isaías 11 retoma a harmonia pacífica do Jardim do Éden e anuncia o caminho de Jesus!",
                "seed_4_6": "O profeta Isaías escreveu palavras cheias de luz! Ele prometeu que nasceria um Menino chamado Príncipe da Paz e que um dia o lobo, o leão e o cordeirinho vão brincar juntos na grama, guiados por uma criancinha feliz!",
                "explorer_dialogue": (
                    "Abrindo seu grande rolo de pergaminho diante das famílias de Jerusalém, Isaías recitou com voz firme e luminosa:\n"
                    "— Não tenham medo! Aqueles que esperam no Senhor renovam as suas forças: sobem com asas como águias, correm e não se cansam, caminham e não desfalecem! A Luz da paz vencerá toda escuridão!"
                ),
                "arq_title": "TRANSFORMAR ESPADAS EM ARADOS (ISAÍAS 2:4)",
                "arq_text": "Esta famosa profecia de Isaías está gravada em letras gigantes no muro em frente à sede das Nações Unidas (ONU), como símbolo mundial do desejo de substituir as guerras pelo cultivo da vida!",
                "family_question": "Se você pudesse desenhar um mundo totalmente em paz, como seriam as ruas, as escolas e os parques desse mundo?"
            },
            {
                "num": 4,
                "title": "DANIEL E SEUS AMIGOS NA TERRA DISTANTE",
                "ref": "Base Bíblica: Daniel 1, 3 e 6",
                "dark_mode": True,
                "art_source": "HERO_VOL5",
                "main_narrative": (
                    "Levados muito jovens para a Babilônia, Daniel e seus três amigos — Hananias, Misael e Azarias — decidiram manter o coração limpo, bondoso e fiel a Deus, alimentando-se com simplicidade e estudando com dedicação.\n\n"
                    "Anos depois, quando conselheiros invejosos criaram uma lei proibindo Daniel de orar e o lançaram na cova dos leões, a Presença Luminosa do Criador fechou a boca das feras durante toda a noite! Ao amanhecer, o rei Dario tirou Daniel são e salvo, glorificando o Deus vivo."
                ),
                "quick_box": "» PEQUENA GRANDE DESCOBERTA: Mesmo morando longe de casa, Daniel abria a janela todos os dias para agradecer e orar!",
                "seed_4_6": "Daniel amava conversar com Deus três vezes por dia perto da janela. Quando homens maus o colocaram numa cova cheia de leões, a Luz de Deus acalmou os leões como gatinhos mansos, e Daniel saiu de manhã sem nenhum arranhão!",
                "explorer_dialogue": (
                    "Assim que o sol raiou, o rei Dario correu aflito até a beira da cova de pedra e chamou com voz trêmula:\n"
                    "— Daniel, servo do Deus vivo! Será que o Deus a quem você serve com tanta fidelidade pôde livrá-lo dos leões?\n"
                    "Lá de baixo, cercado pela luz dourada da manhã e pelos leões em repouso, Daniel sorriu:\n"
                    "— Viva o rei! O meu Deus enviou a Sua luz e fechou a boca dos leões, porque viu que não fiz mal a ninguém!"
                ),
                "arq_title": "BABILÔNIA E A EDUCAÇÃO DOS JOVENS SÁBIOS",
                "arq_text": "Tabuinhas cuneiformes da Babilônia registram como o império reunia jovens talentosos de várias nações para aprender matemática, astronomia e línguas nos palácios reais.",
                "family_question": "Daniel continuou fazendo o que era certo mesmo quando outros quiseram impedi-lo. O que ajuda você a ser fiel aos seus bons valores na escola?"
            },
            {
                "num": 5,
                "title": "A CORAGEM DA RAINHA ESTER: PARA UM TEMPO COMO ESTE",
                "ref": "Base Bíblica: Ester 1–10",
                "dark_mode": True,
                "art_source": "HERO_VOL5",
                "main_narrative": (
                    "Na cidade persa de Susã, a jovem órfã judia Hadassa — conhecida como Ester — foi criada com amor por seu primo Mardoqueu e tornou-se rainha da Pérsia. Quando um ministro orgulhoso chamado Hamã planejou destruir todas as famílias do povo de Ester, Mardoqueu enviou a ela uma mensagem decisiva:\n\n"
                    "— Quem sabe se não foi exatamente para um tempo como este que você chegou à posição de rainha? Com muita coragem e sabedoria, Ester falou ao rei, desfez a injustiça e salvou seu povo!"
                ),
                "quick_box": "» O QUE VOCÊ FARIA? Ester usou sua voz e sua posição para defender quem estava em perigo!",
                "seed_4_6": "A rainha Ester precisou de muita coragem para falar com o rei da Pérsia e defender as famílias do seu povo contra um plano malvado. Ela confiou em Deus, falou a verdade no momento certo e transformou um dia de medo numa grande festa de alegria!",
                "explorer_dialogue": (
                    "Depois de três dias em que todas as famílias oraram unidas por ela, Ester vestiu seus trajes reais e entrou no pátio interno do palácio de Susã.\n"
                    "O rei estendeu o cetro dourado em direção a ela e perguntou:\n"
                    "— O que você deseja, rainha Ester? Qual é o seu pedido?\n"
                    "Com sabedoria e coragem, Ester pediu pela vida e pela proteção do seu povo, trazendo paz e livramento a todas as províncias!"
                ),
                "arq_title": "A FESTA DE PURIM E OS ROLOS DE ESTER (MEGUILÁ)",
                "arq_text": "Até hoje, famílias judaicas do mundo inteiro celebram a coragem de Ester na alegre festa de Purim, lendo o rolo ilustrado de Ester, enviando doces aos amigos e presentes aos pobres!",
                "family_question": "Como podemos usar a nossa voz na escola ou na vizinhança para defender um colega que está sofrendo injustiça?"
            },
            {
                "num": 6,
                "title": "CANÇÕES DE LUZ E PONTES ENTRE OS TESTAMENTOS",
                "ref": "Base Bíblica: Salmos 19, 100, 119:105; Provérbios 3; Esdras e Neemias",
                "dark_mode": False,
                "art_source": "vol1_cap1_cena3_ceu_mar_terra.png",
                "main_narrative": (
                    "De volta a Jerusalém com Esdras e Neemias, o povo reconstruiu os muros da cidade e reuniu o grande tesouro poético de Israel: os Salmos ('Lâmpada para os meus pés é a Tua palavra, e luz para o meu caminho!') e os Provérbios da Sabedoria.\n\n"
                    "Nos séculos seguintes — o período entre os Testamentos —, mesmo passando pelos impérios persa, grego e romano, as famílias guardaram nas sinagogas a promessa de que a Luz de Deus logo visitaria a Terra de um jeito novo!"
                ),
                "quick_box": "» PONTES DA HISTÓRIA: Entre o fim do Antigo Testamento e o nascimento de Jesus passaram-se cerca de 400 anos de história!",
                "seed_4_6": "O povo voltou para casa cantando os Salmos, que dizem: 'A Palavra de Deus é uma lâmpada brilhante para os meus passos e uma luz no meu caminho!' Agora tudo estava pronto para o próximo volume: a chegada do menino Jesus em Belém!",
                "explorer_dialogue": (
                    "Na praça das Águas em Jerusalém, famílias inteiras com suas crianças ouviam Esdras ler o livro da Lei desde o amanhecer:\n"
                    "— Não fiquem tristes — disse Neemias à multidão —, porque a alegria do Senhor é a nossa força!\n"
                    "NOTA HISTÓRICA (LIVROS DEUTEROCANÔNICOS): Neste período persa e helenístico também foram escritos livros como Tobias, Judite, Sabedoria, Eclesiástico (Ben Sirá) e Macabeus, presentes nas Bíblias Católicas e Ortodoxas e estudados como valiosos registros históricos e sapienciais."
                ),
                "arq_title": "O CILINDRO DE CIRO E O RETORNO A JERUSALÉM",
                "arq_text": "O famoso Cilindro de Ciro (peça de argila persa do século VI a.C., hoje no Museu Britânico) confirma historicamente o decreto real que permitiu aos povos exilados voltarem às suas terras e reconstruírem seus templos!",
                "family_question": "Qual versículo, música ou ensinamento de sabedoria funciona como uma lanterna acesa para guiar os seus passos?"
            }
        ]
    }
]
