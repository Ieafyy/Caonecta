# Caonecta
Sistema desenvolvido para o teste prático da empresa DTI Digital

<a href='http://leafyyyy.pythonanywhere.com/'>(acesse rapidamente por aqui!)</a>

Com base no problema informado, foi pedido para desenvolver um sistema na qual dado uma data e a quantidade de cães grandes e pequenos, calcule qual o melhor petshop dentre os informados (Meu Canino Feliz, Vai Rex e ChowChawgas).

Para desenvolvimento do sistema utilizei Python com o framework Flask (backend) e javascript com Jquery (para o frontend). Toda personalização da página foi feita usando HTML e CSS juntamente com o Stylesheet do Tailwind CSS.


![image](https://github.com/Ieafyy/Caonecta/assets/70926962/fcffbfeb-e288-4912-90fe-41abf8324cab)

<h2>Armazenando dados</h2>

Como o problema dado afirma, o usuário alvo do site é Eduardo, dono de um canil e que precisa de um sistema para encontrar qual o melhor petshop da região para realizar o banho de seus cães da melhor forma possível, levando como variáveis principais a distância e o preço do banho com base no porte do cão. Assim sendo, os dados informados sobre os petshops foram armazenados no arquivo dados.py da seguinte forma: 

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/38e0c1f3-1fa4-4e2b-b17d-28b5372b7a03)

<h2>Fazendo a lógica</h2>

Indo para a lógica do sistema, o arquivo funcs.py tem o papel de realizar as formatações, ajustes e comparações necessárias. Optei por separa-lo do arquivo main.py pra maior organização e legibilidade

Já o main.py é o centro do sistema, onde todos os arquivos irão conversar entre si. Aqui usando o framework Flask desenvolvido para Web, realizei todas as comunicações necessárias entre user-server. Os endpoints não podiam ser mais simples: o raiz (/) e /dataget. 

<h2>Endpoints: Raiz</h2>

O raiz é o endpoint acessado pelo usuário e todas as funções de input e output final são mostradas nesse endpoint. Suporta apenas requisições do tipo GET.

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/ca1724b3-00e2-4764-8865-97c6ad539d2d)
----------------------------------------------------

<h2>Endpoints: getdata</h2>

O /getdata é responsável pela comunicação entre os dados passados pelo user com o server. Aqui recebemos um POST contendo dados da data, número de cachorros grande e número de cachorros pequenos.

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/d6a9711f-914c-43b1-95c4-d67ea2673f45)

Depois de todas as informações serem tratadas ele retorna um dicionário (que é interpretado pelo JS como um objeto similar ao JSON)

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/09289c42-3b01-46bb-8715-bdaba41ccf72)
--------------------------------------------------

<h2>Frontend: JS e Jquery</h2>

A principal função exercida pelo Jquery nesse projeto deve-se ao AJAX, que vem nativo junto do Jquery e permite requisições de forma rápida, prática e simples. 

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/e6eeb7e1-ee08-4b1d-8c93-8a91482d3b45)

Aqui realizei um POST para o endpoint /getdata contendo a data (dt), número de cachorros grande (ncg) e número de cachorros pequeno (ncp). O returno dessa request é justamente o petshop que melhor se adequa aos valores digitados (como dito na explanação sobre o main.py).

Fora isso, o JS foi usado para funções para melhorar a experiência do usuário, como adicionando pequenas animações, validando dados para evitar inputs inconsistenstes e afins.
-------------------------------------------------------------------------

<h2>Frontend: HTML e CSS</h2>

Agora por fim a parte visual do sistema construido com HTML, CSS e Tailwind CSS.

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/a014a192-144e-40f4-b9a4-9fee6ff34a26)
-----------------------------------------------------------

<h2>Escolha das tecnologias</h2>

Por deixar em aberto a tecnologia que podia ser usada, fiz minhas escolhas justamente por vivência com tais linguagens. Python é extremamente versatil e é a linguagem que mais possuo domínio, já o framework Flask é muito popular e tido como um dos melhores quando o assunto é web.

JS é o pilar da maioria das aplicações web frontend e Jquery é um framework bem sólido e já há muito esturturado, sendo muito robusto e útil.

HTML e CSS são indispensáveis para o layout da página e escolhi Tailwind CSS por ser prático.

<h2>Fotos</h2>

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/979adc86-973d-412d-bf42-2dcc4d03ea44)
![image](https://github.com/Ieafyy/Caonecta/assets/70926962/b7de115b-44c7-4421-b608-349c418044f1)
![image](https://github.com/Ieafyy/Caonecta/assets/70926962/8fae451d-9b75-40cc-9f10-0b2090a6ff81)

O sistema também é responsivo e mantem a forma mesmo no mobile

![mobile](https://github.com/Ieafyy/Caonecta/assets/70926962/73771959-fd7a-4dad-b235-bf5cf73db6fe)
-------------------------------------------------------------

<h2>Como acessar?</h2>

O sistema está hospedado no servidor da PythonAnywhere e pode ser acessado <a href='http://leafyyyy.pythonanywhere.com/'>por aqui</a>

Caso o servidor por algum motivo apresente alguma instabilidade, o sistema pode ser executado de forma local bastando possuir Python 3.10 e Flask atualizado na máquina. Para isso basta executar o arquivo main.py

![image](https://github.com/Ieafyy/Caonecta/assets/70926962/70cffd36-6ea6-4a65-bd4b-fd5639527e40)

Após isso só acessar o endereço local http://127.0.0.1:5000 



