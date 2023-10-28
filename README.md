# Caonecta
Sistema desenvolvido para o teste prático da empresa DTI Digital

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


